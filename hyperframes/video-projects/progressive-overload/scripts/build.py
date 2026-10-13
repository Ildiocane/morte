# Generate index.html from scripts/index.tpl.html + captions. No music/SFX: voice audio is kept untouched.
import json
caps = json.load(open('assets/captions-final.json'))
DUR = "166.6"
s = open('scripts/index.tpl.html').read().replace('__DUR__', DUR).replace('__CAPS__', json.dumps(caps, ensure_ascii=False))
open('index.html', 'w').write(s)
print(len(caps), 'captions')
