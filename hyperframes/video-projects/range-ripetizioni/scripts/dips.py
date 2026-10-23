# Print the quietest 10ms frames (RMS, dB) inside each window: python3 dips.py audio.wav a-b [a-b ...]
import sys, wave, struct, math
w = wave.open(sys.argv[1]); sr = w.getframerate(); n = w.getnframes()
data = struct.unpack('<%dh' % n, w.readframes(n))
hop = sr // 100
def db(i):
    s = data[i*hop:(i+1)*hop]
    r = math.sqrt(sum(x*x for x in s) / max(len(s), 1)) or 1
    return 20 * math.log10(r / 32768)
for win in sys.argv[2:]:
    a, b = map(float, win.split('-'))
    frames = [(db(i), i / 100) for i in range(int(a*100), int(b*100))]
    best = sorted(frames)[:4]
    print(win, ' '.join(f'{t:.2f}s({d:.0f}dB)' for d, t in sorted(best, key=lambda x: x[1])))
