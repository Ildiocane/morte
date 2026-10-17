# Generate index.html from scripts/index.tpl.html + captions. Source video/audio are not modified.
import json, subprocess
caps = json.load(open('assets/captions-final.json'))
DUR = subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0','assets/source.mp4'],capture_output=True,text=True).stdout.strip()
s = open('scripts/index.tpl.html').read().replace('__DUR__', DUR).replace('__CAPS__', json.dumps(caps, ensure_ascii=False))
open('index.html', 'w').write(s)
print(len(caps), 'captions, dur', DUR)
