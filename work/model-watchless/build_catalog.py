from pathlib import Path
import html
import json
import hashlib
import zipfile
from urllib.parse import quote, unquote, urlsplit
from html.parser import HTMLParser

WORKSPACE = Path(__file__).resolve().parents[2]
ROOT = WORKSPACE / 'outputs' / 'model-watchless-service'
COUNTS = json.loads((Path(__file__).parent / 'delivery-counts.json').read_text(encoding='utf-8'))

class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []
    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if value and ((tag == 'img' and name == 'src') or (tag == 'a' and name == 'href')):
                self.refs.append(value)

rows, checks, service_jobs = [], [], []
for source in sorted((WORKSPACE / 'model').glob('*.mp4')):
    project = ROOT / source.stem
    for transcript in (project / 'work' / 'video-use' / 'transcripts').glob('*.json'):
        metadata = json.loads(transcript.read_text(encoding='utf-8')).get('metadata', {})
        service_jobs.append({'video': source.name, 'provider': metadata.get('provider'), 'service': metadata.get('service'), 'job_id': metadata.get('job_id')})
    links = []
    artifacts = [*project.glob('share/*visual-explainer.html'),
                 *project.glob('share/*visual-explainer.pdf'),
                 *project.glob('share/*visual-explainer.md'),
                 *project.glob('*.zip')]
    decks = [p for p in project.rglob('*.html') if ('slides' in p.parts or 'deck' in p.stem) and 'work' not in p.parts]
    artifacts += decks
    labels = {'.html': '完整图文教程', '.pdf': 'PDF', '.md': 'Markdown', '.zip': '下载包'}
    for artifact in artifacts:
        label = '重点演示稿' if artifact in decks else labels[artifact.suffix]
        links.append(f'<a href="{quote(artifact.relative_to(ROOT).as_posix())}">{label}</a>')
        check = {'path': str(artifact), 'bytes': artifact.stat().st_size}
        if artifact.suffix == '.html':
            parser = References()
            parser.feed(artifact.read_text(encoding='utf-8'))
            missing = []
            for ref in parser.refs:
                url = urlsplit(ref)
                if url.scheme or url.netloc or not url.path:
                    continue
                if not (artifact.parent / unquote(url.path)).exists():
                    missing.append(ref)
            check['missing_local_references'] = missing
        if artifact.suffix == '.zip':
            with zipfile.ZipFile(artifact) as archive:
                check['zip_bad_member'] = archive.testzip()
                check['zip_entries'] = len(archive.namelist())
        checks.append(check)
    counts = COUNTS[source.stem.split('.')[0]]
    stats = f"{counts['scenes']} 个场景 · {counts['images']} 张配图 · PDF {counts['pdf_pages']} 页 · 演示稿 {counts['deck_slides']} 页"
    rows.append(f'<article><h2>{html.escape(source.stem)}</h2><p>{stats}</p><nav>{"".join(links) or "处理中"}</nav></article>')

baseline = json.loads((Path(__file__).parent / 'source-hashes.json').read_text(encoding='utf-8-sig'))
source_integrity = []
for row in baseline:
    path = Path(row['Path'])
    with path.open('rb') as stream:
        digest = hashlib.file_digest(stream, 'sha256').hexdigest().upper() if hasattr(hashlib, 'file_digest') else hashlib.sha256(stream.read()).hexdigest().upper()
    source_integrity.append({'path': str(path), 'unchanged': digest == row['Hash']})

page = '''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Agents 底层逻辑 · 课程资料</title><style>body{max-width:960px;margin:64px auto;padding:0 24px;background:#f5f4ef;color:#172b35;font:17px/1.7 system-ui,"Microsoft YaHei",sans-serif}h1{font-size:clamp(28px,5vw,46px);line-height:1.2}header{margin-bottom:40px}header p{color:#54636a}article{padding:22px 26px;margin:18px 0;background:white;border:1px solid #d9dfdf;border-radius:14px}h2{font-size:22px;margin:0 0 14px}nav{display:flex;gap:10px;flex-wrap:wrap}a{color:#086c71;border:1px solid #b7cdcb;border-radius:8px;padding:7px 14px;text-decoration:none}a:hover{background:#e5f1ef}footer{margin-top:36px;color:#54636a;font-size:14px}</style><header><p>WATCHLESS · 本地课程资料</p><h1>Agents 底层逻辑</h1><p>按课程顺序阅读完整图文教程，或使用配套重点演示稿。</p></header>'''
    
ROOT.mkdir(parents=True, exist_ok=True)
(ROOT / 'index.html').write_text(page + ''.join(rows) + '<footer>本批次使用更新后的 Watchless，通过本地 video-mate-pick 音画服务处理。原始视频保留不变。</footer></html>', encoding='utf-8')
(ROOT / 'batch-verification.json').write_text(json.dumps({'artifacts': checks, 'source_integrity': source_integrity, 'service_jobs': service_jobs, 'counts': COUNTS, 'known_limits': ['时间定位为音频块级近似值，未逐句听音核验。', '已依据原画面字幕和上下文修订明显识别问题，不确定项保留说明。', '运行环境不提供真实 token 和费用，均保持未知。']}, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'catalog': str(ROOT / 'index.html'), 'artifacts': len(checks), 'sources_unchanged': all(row['unchanged'] for row in source_integrity), 'missing_references': sum(len(row.get('missing_local_references', [])) for row in checks)}, ensure_ascii=False))
