import json, subprocess
caps = json.load(open('assets/captions.json'))
DUR = subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0','assets/edit.mp4'],capture_output=True,text=True).stdout.strip()
SFX = [("whoosh.mp3",0.08,0.6,0.15),("pop.mp3",0.58,0.5,0.14),("pop.mp3",3.18,0.5,0.14),("slam.mp3",4.08,1.1,0.16),("slam.mp3",11.08,1.1,0.14),
  ("whoosh.mp3",12.05,0.6,0.2),("pop.mp3",16.18,0.5,0.15),("pop.mp3",16.53,0.5,0.15),("swipe.mp3",17.75,0.8,0.12),("slam.mp3",22.48,1.1,0.16),
  ("click.wav",24.88,0.46,0.18),("slam.mp3",27.98,1.1,0.15),("whoosh.mp3",30.65,0.6,0.2),("click.wav",33.38,0.46,0.18),("slam.mp3",37.88,1.1,0.16),
  ("swipe.mp3",40.25,0.8,0.12),("pop.mp3",43.58,0.5,0.14),("click.wav",48.88,0.46,0.16),("slam.mp3",53.18,1.1,0.14),("whoosh.mp3",54.55,0.6,0.2),
  ("pop.mp3",58.08,0.5,0.15),("pop.mp3",60.38,0.5,0.15),("sparkle.mp3",62.98,1.6,0.14)]
tags = [f'<audio id="sfx{k}" src="assets/sfx/{f}" data-start="{t}" data-duration="{d}" data-track-index="{10+k}" data-volume="{v}"></audio>' for k,(f,t,d,v) in enumerate(SFX)]
tags.append(f'<audio id="music" src="assets/music.mp3" data-start="0" data-duration="{DUR}" data-track-index="2" data-volume="0.045"></audio>')
s = open('scripts/index.tpl.html').read().replace('__DUR__', DUR).replace('__CAPS__', json.dumps(caps, ensure_ascii=False)).replace('__SFX__', '\n      '.join(tags))
open('index.html','w').write(s); print(len(caps), DUR)
