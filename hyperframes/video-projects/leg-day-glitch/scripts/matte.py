# Person alpha matte for the whole clip with RobustVideoMatting (TorchScript, CPU) -> assets/alpha.mkv (gray, lossless FFV1)
import subprocess, numpy as np, torch, time
W, H = 1080, 1920
torch.set_num_threads(4)
model = torch.jit.load("assets/rvm_mobilenetv3_fp32.torchscript").eval()
rd = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-i", "assets/src.mp4", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
wr = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "gray", "-s", f"{W}x{H}", "-r", "30", "-i", "-", "-c:v", "ffv1", "assets/alpha.mkv"], stdin=subprocess.PIPE)
rec = [None] * 4; n = 0; t0 = time.time()
with torch.no_grad():
    while True:
        buf = rd.stdout.read(W * H * 3)
        if len(buf) < W * H * 3: break
        x = torch.from_numpy(np.frombuffer(buf, np.uint8).reshape(H, W, 3)).permute(2, 0, 1).float().div(255).unsqueeze(0)
        fgr, pha, *rec = model(x, *rec, 0.25)
        wr.stdin.write((pha[0, 0].clamp(0, 1).mul(255).byte().numpy()).tobytes()); n += 1
        if n % 150 == 0: print(n, "frames", round(n / (time.time() - t0), 2), "fps", flush=True)
wr.stdin.close(); wr.wait(); print("done", n)
