# Generate index.html from scripts/index.tpl.html + captions. No music/SFX: voice audio is kept untouched.
import json
caps = json.load(open('assets/captions-final.json'))
import subprocess
DUR = subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0','assets/edit.mp4'],capture_output=True,text=True).stdout.strip()
MAP = open('assets/timemap.json').read()
s = open('scripts/index.tpl.html').read().replace('__DUR__', DUR).replace('__MAP__', MAP).replace('__CAPS__', json.dumps(caps, ensure_ascii=False))
open('index.html', 'w').write(s)
print(len(caps), 'captions')
