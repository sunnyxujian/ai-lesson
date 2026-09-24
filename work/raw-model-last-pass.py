from pathlib import Path
p=Path('work/raw-model-build.py');s=p.read_text(encoding='utf-8');s=s.replace(r'学习路径\\A\\A',r'学习路径\\A \\A ');p.write_text(s,encoding='utf-8')
