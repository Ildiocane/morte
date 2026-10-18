# Audio bed: the reference TikTok sound (assets/music.wav, beat-looped to the video length) + a 3-shot photo-shutter burst
# at the start of every sequence (same times as the visual snaps in compose.py). The original clip audio is not used.
import numpy as np, soundfile as sf
CUTS = [0.0, 12.0667, 20.6, 30.7333, 40.6333]; SNAPS = [0.0, 0.2, 0.4]; DUR = 50.1333   # = 1504 source frames
mu, sr = sf.read("assets/music.wav", dtype="float32"); sh, sr2 = sf.read("assets/shutter.wav", dtype="float32")
assert sr == sr2 == 48000
n = int(round(DUR * sr)); out = np.zeros((n, 2), np.float32); out[:min(n, len(mu))] = mu[:n] * 0.72
for c in CUTS:
    for j, o in enumerate(SNAPS):
        i = int(round((c + o) * sr)); g = (1.5, 1.25, 1.05)[j]
        seg = sh[: n - i] * g; out[i:i + len(seg)] += seg
        d0, d1 = i, min(n, i + int(0.12 * sr))                     # brief music dip under each click so it reads
        out[d0:d1] -= mu[d0:d1] * 0.72 * 0.35 if d1 <= len(mu) else 0
sf.write("renders/mix-raw.wav", out, sr, subtype="FLOAT")
print("peak", float(np.abs(out).max()))
