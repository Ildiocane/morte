# transcript-raw.json (whisper on the untouched take, word level) + the hand-corrected text below -> captions.json
# Each corrected word takes the timing of the whisper word it aligns to (difflib); unmatched words are spread
# evenly inside their replace block. Captions: chunks of <= 3 words / 17 chars, uppercase (Jeff Nippard style: plain white).
import json, re, difflib
TEXT = """Per quanto sembrerà strano, il carico è l'unica cosa che ti deve interessare, o quasi l'unica roba. Perché se tu
hai della tecnica corretta, hai lo stesso range di movimento e recuperi adeguatamente, il carico deve aumentare. Se
aumenta, aumenta la tua forza; se la forza aumenta, aumenta l'ipertrofia. Lineare. Ok? Non vuoi sentire altro. Eh, però,
perché in realtà puoi diventare forte anche senza montagne di massa muscolare. È sempre un adattamento fisiologico e
sarà sempre in questo ordine: prima diventi forte e poi c'è il muscolo. Quindi meccanizza ogni singola ripetizione che
fai, recupera adeguatamente e non cancellare il ROM che hai acquisito durante le alzate, e crescerai. Basta. Devi
riuscire sempre ad aumentare quel chilo, quel chilo e mezzo, anche con i microcarichi, perché per quanto impercettibili
sono importanti. E non devi fare altro che continuare ad aggiungere carico e tenere quel range di ripetizioni
relativamente basso, dai 4 ai 10 colpi."""
norm = lambda w: re.sub(r"[^a-zàèéìòóù0-9]", "", w.lower())
d = json.load(open("assets/transcript-raw.json"))
W = [(s["offsets"]["from"] / 1000, s["offsets"]["to"] / 1000, s["text"].strip()) for s in d["transcription"] if norm(s["text"])]
T = TEXT.split()
times = [None] * len(T)
for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, [norm(w) for w in T], [norm(w[2]) for w in W], autojunk=False).get_opcodes():
    if op == "equal":
        for k in range(i2 - i1): times[i1 + k] = (W[j1 + k][0], W[j1 + k][1])
    elif op in ("replace", "delete") and i2 > i1:                  # text words whisper missed or misheard
        a = W[j1][0] if j1 < len(W) and j2 > j1 else (times[i1 - 1][1] if i1 else 0.0)
        b = W[j2 - 1][1] if j2 > j1 else (W[j2][0] if j2 < len(W) else a + 0.3)
        n = i2 - i1
        if b - a < 0.12 * n and i1 > 0:                              # no room left: borrow the 2nd half of the previous word
            p0, p1 = times[i1 - 1]; mid = (p0 + p1) / 2; times[i1 - 1] = (p0, mid); a = mid
        for k in range(n): times[i1 + k] = (a + (b - a) * k / n, a + (b - a) * (k + 1) / n)
words = [{"text": t, "start": round(s, 3), "end": round(e, 3)} for t, (s, e) in zip(T, times)]
json.dump(words, open("assets/transcript.json", "w"), ensure_ascii=False, indent=0)

FUNC = {"di", "a", "ad", "ai", "dai", "da", "in", "con", "su", "per", "tra", "il", "lo", "la", "le", "i", "gli", "un", "uno", "una", "dei", "del",
        "dello", "della", "al", "che", "e", "o", "se", "non", "mi", "vi", "ti", "quel", "quella", "è", "sono", "sarà", "stai"}
cw = []                                                                 # caption tokens: keep compound names whole
for w in words:
    if cw and (cw[-1]["text"].lower(), w["text"].lower().strip(",.")) in (("4", "ai"), ("ai", "10")):
        cw[-1] = {**cw[-1], "text": cw[-1]["text"] + " " + w["text"], "end": w["end"]}
    else: cw.append(w)
caps, cur = [], []
for k, w in enumerate(cw):
    cur.append(w); nxt = cw[k + 1] if k + 1 < len(cw) else None
    hard = re.search(r"[.,:;?!]$", w["text"]) or nxt is None or nxt["start"] - w["end"] > 0.3
    full = len(cur) >= 3 or len(" ".join(x["text"] for x in cur + ([nxt] if nxt else []))) > 17
    if hard: caps.append(cur); cur = []
    elif full:
        cut = len(cur)                                                   # never end on "di", "le", "che"...: carry them over
        while cut > 1 and cur[cut - 1]["text"].lower() in FUNC: cut -= 1
        if cur[cut - 1]["text"].lower() in FUNC: cut = len(cur)          # nothing but function words: keep as is
        caps.append(cur[:cut]); cur = cur[cut:]
out = []
for k, c in enumerate(caps):
    a = c[0]["start"]; b = caps[k + 1][0]["start"] if k + 1 < len(caps) else c[-1]["end"] + 0.4
    out.append({"a": round(a, 3), "w": [[re.sub(r"[,;:]$", "", x["text"]).upper(), round(x["start"], 3)] for x in c], "b": round(min(b, c[-1]["end"] + 0.6), 3)})
json.dump(out, open("assets/captions.json", "w"), ensure_ascii=False)
print(len(words), "words,", len(out), "captions")
