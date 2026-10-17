# Writes youtube.md: title, description and chapter timestamps from assets/timing.json
import json
TIM = json.load(open("assets/timing.json")); SEC = TIM["sections"]
fmt = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
chap = [("0:00", "Una giornata storta o un segnale?")]
for sid, label in [("s2", "Cos'è uno scarico (e i 3 tipi)"), ("s3", "Lo studio del 2024 sulla settimana di stop"), ("s4", "Perché le prestazioni calano: 6 cause"),
                   ("s5", "Tre casi: seduta storta, calo ripetuto, dolore"), ("s6", "Un esempio pratico di scarico"), ("s7", "Cosa osservare dopo"), ("s8", "Il metodo LB System")]:
    chap.append((fmt(max(0, SEC[sid][0] - 1.7)), label))
md = f"""# Titolo
Scarico: quando serve davvero? (decidi, non indovinare)

# Descrizione
Una seduta storta non è sovrallenamento, e uno scarico non è un rituale da calendario.
In questo video ti mostro come decidere con criterio: cosa guardare, quali domande farti e come verificare se hai scelto bene.

📊 Studio citato: Coleman et al., 2024, PeerJ, "Gaining more from doing less? The effects of a one-week deload period during supervised resistance training on muscular adaptations".

👉 LB System (programmazione, app, assistenza diretta): [inserisci link]
🏋️ Allenati con me di persona: NEXUS Private Gym

⚠️ Contenuto informativo: in caso di dolore persistente rivolgiti a un medico o a un fisioterapista.

# Capitoli
""" + "\n".join(f"{t} {l}" for t, l in chap) + f"\n\nDurata: {fmt(TIM['dur'])}\n"
open("youtube.md", "w").write(md); print(md)
