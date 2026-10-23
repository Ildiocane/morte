# DeepFilterNet3 speech enhancement (denoise + dereverb). Shims torchaudio.backend removed in torchaudio>=2.1.
import sys, types
m = types.ModuleType("torchaudio.backend"); c = types.ModuleType("torchaudio.backend.common")
class AudioMetaData: pass
c.AudioMetaData = AudioMetaData; m.common = c
sys.modules["torchaudio.backend"] = m; sys.modules["torchaudio.backend.common"] = c
import torch, soundfile as sf, numpy as np, torchaudio
from df.enhance import enhance, init_df
model, state, _ = init_df(model_base_dir="/root/.cache/DeepFilterNet/DeepFilterNet3")
a, sr = sf.read(sys.argv[1], dtype="float32")
x = torch.from_numpy(a)[None]
if sr != state.sr(): x = torchaudio.functional.resample(x, sr, state.sr())
y = enhance(model, state, x, atten_lim_db=float(sys.argv[3]) if len(sys.argv) > 3 else None)
sf.write(sys.argv[2], y[0].numpy(), state.sr(), subtype="PCM_24")
print("done", state.sr())
