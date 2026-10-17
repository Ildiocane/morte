#!/usr/bin/env bash
# renders/v1.mp4 -> renders/final.mp4 (loudness -14 LUFS for YouTube, video copied) -> delivery copy in $1
set -euo pipefail
IN=${IN:-renders/v2.mp4}; OUT=renders/final.mp4
J=$(ffmpeg -hide_banner -i "$IN" -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
g() { echo "$J" | python3 -c "import json,sys; print(json.load(sys.stdin)['$1'])"; }
ffmpeg -y -loglevel error -i "$IN" -c:v copy -af "loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=$(g input_i):measured_TP=$(g input_tp):measured_LRA=$(g input_lra):measured_thresh=$(g input_thresh):offset=$(g target_offset):linear=true" -ar 48000 -c:a aac -b:a 192k -movflags +faststart "$OUT"
ffmpeg -hide_banner -i "$OUT" -af ebur128 -f null - 2>&1 | grep -E "^\s+I:" | tail -1
if [ -n "${1:-}" ]; then
  ffmpeg -y -loglevel error -i "$OUT" -c:v libx264 -preset slow -crf 24 -tune animation -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart "$1"
  ls -la "$1"
fi
