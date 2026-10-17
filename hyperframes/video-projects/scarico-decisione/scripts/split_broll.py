# Cut the rendered b-roll reel (broll/renders/broll.mp4) into one clip per shot -> assets/broll/<name>.mp4
import subprocess, os
SHOTS = [("gym", 6), ("squat", 7), ("bench", 7), ("row", 6), ("bar", 5), ("tired", 6), ("sleep", 7), ("eat", 6), ("stress", 6), ("physio", 7), ("app", 7)]
os.makedirs("assets/broll", exist_ok=True); t = 0
for name, d in SHOTS:
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{t}", "-i", "broll/renders/broll.mp4", "-t", f"{d}", "-an", "-c:v", "libx264", "-preset", "medium",
                    "-crf", "16", "-g", "15", "-pix_fmt", "yuv420p", "-movflags", "+faststart", f"assets/broll/{name}.mp4"], check=True)
    t += d; print(name, "ok")
