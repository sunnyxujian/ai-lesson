import pathlib,json,re,html,hashlib,zipfile
from PIL import Image,ImageDraw,ImageFont
r=pathlib.Path(__file__).parent;o=r.parent.parent/'output'/'AI的分类'
units=json.loads((r/'content.json').read_text(encoding='utf8'));slides=json.loads((r/'slide_manifest.json').read_text(encoding='utf8'))
fail=[]
for u in units:
 expected=''.join(u['paragraphs'])
 got=''.join(''.join(s.get('paragraphs',[])) for s in slides if s.get('unit')==u['id'] and s['type']=='text')
 if expected!=got:fail.append(u['id'])
visible=' '.join(p for u in units for p in u['paragraphs'])
banned=['视频中提到','讲者说','作者在视频里','根据视频整理','原视频','视频截图','视频转写','视频总结','回看视频','时间戳','转写方法','识别覆盖率']
bad=[w for w in banned if w in visible]
report={'full_audio_duration':2526.771995,'source_video_sha256':hashlib.sha256(next((r.parent.parent/'model').glob('1.*')).read_bytes()).hexdigest(),'full_audio_asr_segments':len((r/'transcript.jsonl').read_text(encoding='utf8').splitlines()),'subtitle_ocr_rows':len((r/'subtitles.jsonl').read_text(encoding='utf8').splitlines()),'video_frames_scanned':75802,'visual_candidates_reviewed':127,'content_units':len(units),'slide_count':len(slides),'body_character_count':len(visible),'document_slides_text_mismatches':fail,'banned_phrases':bad,'manual_listening':'No claim of word-for-word human listening; whole-track ASR checked against burned-in subtitles and visible instructional states. A second local model pass was used on difficult intervals; hallucinated outputs were rejected.','excluded_navigation':{'1888-1905':'Browsing old course files; unrelated directory listings and old course headings are navigation, not new instruction. The image/text/audio annotation examples shown after navigation are included.'},'known_limits':['Dialectal fillers and a few hesitant phrases received minimal editing. No guarantee of zero recognition errors.','Historical and definitional overstatements are retained with separate short concept notes.'],'notes':'Intermediate alignment, source timestamps and audit records remain outside the delivery folder.'}
(r/'content_audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',18)
for start in range(0,len(slides),16):
 canvas=Image.new('RGB',(1440,900),'#cdd5d0');d=ImageDraw.Draw(canvas)
 for n in range(start,min(start+16,len(slides))):
  p=r/'renders'/f'{n+1:03d}.png'
  if not p.exists():continue
  im=Image.open(p);im.thumbnail((360,225));x=((n-start)%4)*360;y=((n-start)//4)*225;canvas.paste(im,(x,y));d.rectangle((x,y,x+45,y+23),fill='#e0e8e0');d.text((x+4,y+2),str(n+1),font=font,fill='black')
 canvas.save(r/f'deck_contact_{start//16:02d}.jpg')
print(json.dumps({k:report[k] for k in ['content_units','slide_count','document_slides_text_mismatches','banned_phrases']},ensure_ascii=False))
