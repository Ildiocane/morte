# Extend the 11.8 s TikTok sound to the full 50.13 s video: intro + 6 four-bar loops of the main section + natural ending,
# joined on beats with short crossfades, then stretched by ~1% (rubberband) to land exactly on the video length.
import numpy as np, soundfile as sf, subprocess
y, sr = sf.read("assets/song-snippet.wav")
A, B = 4.191, 10.472                       # loop = 16 beats of the main section (152 BPM)
VIDEO = 50.1333
seg = lambda a, b: y[int(a * sr):int(b * sr)]
parts = [seg(0, A)] + [seg(A, B) for _ in range(6)] + [seg(A, len(y) / sr)]
xf = int(0.04 * sr)
out = parts[0]
for p in parts[1:]:
    fade = np.linspace(0, 1, xf)[:, None]
    out = np.concatenate([out[:-xf], out[-xf:] * (1 - fade) + p[:xf] * fade, p[xf:]])
sf.write("/tmp/music_raw.wav", out, sr)
ratio = (len(out) / sr) / VIDEO
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "/tmp/music_raw.wav", "-af",
                f"rubberband=tempo={ratio:.5f}:pitchq=quality,afade=t=out:st={VIDEO - 1.0:.3f}:d=1.0", "-t", f"{VIDEO:.4f}", "-ar", "48000", "assets/music.wav"], check=True)
print("raw", round(len(out) / sr, 3), "s  tempo ratio", round(ratio, 4))
# beat grid in output time (for glitch hits): beats of each piece mapped through the concatenation + stretch
