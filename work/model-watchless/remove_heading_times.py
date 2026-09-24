from pathlib import Path
import re, sys, json, shutil, subprocess, zipfile
from datetime import datetime

sys.path.insert(0, r'C:\Users\micro\.codex\skills\watchless\scripts')
import windows_runtime
from video_notes_common import make_contact_sheet

ROOT = Path(r'C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service')
BACKUP = Path(__file__).parent / ('before-heading-time-removal-' + datetime.now().strftime('%Y%m%d-%H%M%S'))
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
TIME = re.compile(r'[（(]\s*\d{1,2}:\d{2}(?::\d{2})?\s*[-–—]\s*\d{1,2}:\d{2}(?::\d{2})?\s*[）)]')
ELEMENT = re.compile(r'(<(?:h[1-6]|a)\b[^>]*>)(.*?)(</(?:h[1-6]|a)>)', re.S | re.I)

def clean_elements(text):
    return ELEMENT.sub(lambda m: m[1] + TIME.sub('', m[2]) + m[3], text)

def run(args):
    return subprocess.run(args, check=True, capture_output=True).stdout.decode('utf-8', errors='replace')

report = []
for project in sorted(p for p in ROOT.iterdir() if p.is_dir()):
    html_path = next((project / 'share').glob('*-visual-explainer.html'))
    pdf_path = html_path.with_suffix('.pdf')
    old_pages = int(re.search(r'Pages:\s+(\d+)', run(['pdfinfo', str(pdf_path)]))[1])
    targets = [html_path, *(project / 'share').glob('*.md')]
    archive_path = next(project.glob('*-video-notes.zip'))
    for path in [*targets, pdf_path, archive_path]:
        dest = BACKUP / path.relative_to(ROOT)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, dest)
    changes = {}
    for path in targets:
        original = path.read_text(encoding='utf-8')
        cleaned = clean_elements(original)
        if path.suffix == '.md':
            cleaned = re.sub(r'^#{1,6}[^\r\n]*', lambda m: TIME.sub('', m[0]), cleaned, flags=re.M)
        changes[path.name] = len(TIME.findall(original)) - len(TIME.findall(cleaned))
        if path.suffix == '.html':
            assert re.findall(r'\b(?:id|href|src)=["\'][^"\']*["\']', original) == re.findall(r'\b(?:id|href|src)=["\'][^"\']*["\']', cleaned)
            old_body = ELEMENT.sub('', original)
            new_body = ELEMENT.sub('', cleaned)
            assert old_body == new_body, 'Non-heading body changed'
        assert not any(TIME.search(m[2]) for m in ELEMENT.finditer(cleaned))
        path.write_text(cleaned, encoding='utf-8')
    run([CHROME, '--headless=new', '--disable-gpu', '--allow-file-access-from-files',
         f'--print-to-pdf={pdf_path}', f'--user-data-dir={project / "work/chrome-no-heading-times"}',
         '--no-pdf-header-footer', html_path.as_uri()])
    new_pages = int(re.search(r'Pages:\s+(\d+)', run(['pdfinfo', str(pdf_path)]))[1])
    pdf_text = run([r'C:\Users\micro\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe', '-X', 'utf8', '-c',
                    'import sys; from pypdf import PdfReader; print("\\n".join(p.extract_text() or "" for p in PdfReader(sys.argv[1]).pages))', str(pdf_path)])
    assert not TIME.search(pdf_text), 'Visible time range remains in PDF'
    out = project / 'verify' / 'pdf-no-heading-times'
    out.mkdir(exist_ok=True)
    run(['pdftoppm', '-png', '-r', '70', str(pdf_path), str(out / 'page')])
    pages = sorted(out.glob('page-*.png'))
    assert len(pages) == new_pages
    make_contact_sheet(pages, [f'page {i+1}' for i in range(len(pages))],
                       project / 'verify/pdf-pages-contact-sheet.jpg', columns=4, thumb_width=280)
    modified = {str(p.relative_to(project)).replace('\\', '/'): p for p in [*targets, pdf_path]}
    temp_zip = archive_path.with_suffix('.tmp.zip')
    with zipfile.ZipFile(archive_path) as source, zipfile.ZipFile(temp_zip, 'w') as dest:
        for entry in source.infolist():
            data = modified[entry.filename].read_bytes() if entry.filename in modified else source.read(entry.filename)
            dest.writestr(entry, data)
    with zipfile.ZipFile(temp_zip) as packed:
        assert packed.testzip() is None
        for name, path in modified.items():
            assert packed.read(name) == path.read_bytes()
    temp_zip.replace(archive_path)
    result = {'project': project.name, 'removed_ranges': changes, 'old_pdf_pages': old_pages,
              'pdf_pages': new_pages, 'heading_and_toc_times_removed': True,
              'body_and_anchor_attributes_unchanged': True, 'zip_matches_current_files': True}
    (project / 'verify/heading-time-removal.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    report.append(result)
    print(json.dumps(result, ensure_ascii=False), flush=True)
(ROOT / 'heading-time-removal.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
counts_path = Path(__file__).parent / 'delivery-counts.json'
counts = json.loads(counts_path.read_text(encoding='utf-8'))
for item in report:
    counts[item['project'].split('.')[0]]['pdf_pages'] = item['pdf_pages']
counts_path.write_text(json.dumps(counts, ensure_ascii=False, indent=2), encoding='utf-8')
