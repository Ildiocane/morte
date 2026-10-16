# Final audio: dialogue.wav sample-exact (no normalisation/compression), + music bed and SFX underneath (amix normalize=0).
import re, subprocess, sys
html = open('index.html').read()
sfx = re.findall(r'<audio id="sfx\d+" src="([^"]+)" data-start="([\d.]+)" data-duration="([\d.]+)" data-track-index="\d+" data-volume="([\d.]+)"', html)
inp = ['-i', 'assets/audio/dialogue.wav', '-i', 'assets/audio/music.mp3']
fc = ['[2]volume=0.09,atrim=0:48.25[m]']; lbl = ['[1]', '[m]']
for k, (src, st, du, vol) in enumerate(sfx):
    inp += ['-i', src]; d = int(float(st) * 1000)
    fc.append(f'[{k+3}]atrim=0:{du},volume={vol},adelay={d}|{d}[s{k}]'); lbl.append(f'[s{k}]')
fc.append(''.join(lbl) + f'amix=inputs={len(lbl)}:normalize=0:duration=first[a]')
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', sys.argv[1], *inp, '-filter_complex', ';'.join(fc),
                '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '320k', '-ar', '48000', '-movflags', '+faststart', sys.argv[2]], check=True)
