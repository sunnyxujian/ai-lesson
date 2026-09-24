import base64,io,json,re
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools import subset
R=Path(__file__).resolve().parent
css=(R/'google-fonts-embedded.css').read_text(encoding='utf-8')
chars=(R/'authored-notes.json').read_text(encoding='utf-8')+(R/'build_deck.py').read_text(encoding='utf-8')+''.join(chr(x) for x in range(32,127))
for data in set(re.findall(r'base64,([A-Za-z0-9+/=]+)',css)):
    font=TTFont(io.BytesIO(base64.b64decode(data)))
    options=subset.Options();options.recalc_bounds=True
    sub=subset.Subsetter(options=options);sub.populate(text=chars);sub.subset(font)
    stream=io.BytesIO();font.flavor='woff2';font.save(stream)
    css=css.replace(data,base64.b64encode(stream.getvalue()).decode())
css=css.replace("format('truetype')","format('woff2')")
(R/'google-fonts-subset.css').write_text(css,encoding='utf-8')
print('font CSS bytes',len(css))
