# Storyboard: what is on screen for every line of the script.
# Anchors: "s2d" chunk start · "s2d$" chunk end · "s2d:word" / "s2d:word#2" word start (prefix match, "=word" exact) · "+0.3"/"-0.2" offsets.
# BEATS fill the screen back to back (each lasts until the next one); POPS float over the b-roll.

BROLL_LEN = {"gym": 6, "squat": 7, "bench": 7, "row": 6, "bar": 5, "tired": 6, "sleep": 7, "eat": 6, "stress": 6, "physio": 7, "app": 7}
CHAPTERS = [("s2", "Cos'è uno scarico"), ("s3", "Lo studio del 2024"), ("s4", "Perché le prestazioni calano"), ("s5", "Tre casi"),
            ("s6", "Un esempio pratico"), ("s7", "Cosa osservare dopo"), ("s8", "Il metodo LB System")]

def chap(sid, num, title):
    return {"at": f"{sid}-1.75", "scene": "chapter", "p": {"num": num, "title": title}, "sfx": "whoosh"}

BEATS = [
    # ---------------- 1 · apertura ----------------
    {"at": 0, "broll": "bench", "zoom": (1.0, 1.1)},
    {"at": "s1a:primo-0.3", "broll": "tired", "zoom": (1.12, 1.02)},
    {"at": "s1b:sono-0.15", "scene": "stamp_word", "p": {"word": "Sovrallenamento?", "kick": "Oppure, peggio ancora", "size": 128}, "sfx": "slam"},
    {"at": "s1c", "scene": "compare_days", "p": {"right_at": "s1c:tre", "neq_at": "s1c:non", "noise_at": "s1d:rumore-0.3", "info_at": "s1d:un'informazione-0.4"}},
    {"at": "s1e", "scene": "crossed", "p": {"title": "In questo video, niente…", "items": [
        ("Scarico ogni 4 settimane", "cal", "s1e:regola-0.2", "s1e:settimane+0.3"),
        ("Diagnosi improvvisate", "med", "s1e:diagnosi-0.3", "s1e:sovrallenamento+0.2")]}},
    {"at": "s1f", "scene": "steps3", "p": {"kick": "Ti mostro come arrivare a", "title": "Una decisione motivata", "steps": [
        ("Cosa guardare", "eye", "s1f:cosa"), ("Quali domande farti", "q", "s1f:quali"), ("Come verificare", "check", "s1f:come#2")]}},
    {"at": "s1f$+0.25", "scene": "sting", "p": {"title": "Scarico: decidere, non indovinare", "sub": "quando serve davvero e come sceglierlo"}, "sfx": "bass-drop"},

    # ---------------- 2 · cos'è uno scarico ----------------
    chap("s2", "01", "Cos'è uno scarico"),
    {"at": "s2a", "broll": "gym", "zoom": (1.05, 1.15)},
    {"at": "s2b", "scene": "definition", "p": {"temp_at": "s2b:temporanea#2", "rid_at": "s2b:riduzione#2", "smett_at": "s2b:smettere"}},
    {"at": "s2c", "broll": "squat", "zoom": (1.0, 1.08)},
    {"at": "s2d", "scene": "three_ways", "p": {"c1": "s2d", "c1b": "s2d:quattro", "c2": "s2e", "c2b": "s2e:lasci", "c3": "s2f", "neq_at": "s2g:non", "st_at": "s2g:intercambiabili"}},
    {"at": "s2g:ridurre-0.2", "scene": "matrix", "p": {"rows": [
        ("Meno serie", ["gesto", "intensità"], [("fatica totale", "down")], "s2g:ridurre"),
        ("Serie meno difficili", ["volume"], [("stress di ogni serie", "down")], "s2h"),
        ("Stop completo", [], [("stimolo", "x"), ("pratica del movimento", "x")], "s2h:fermarsi")]}},
    {"at": "s2i", "scene": "quale", "p": {"q1": "s2i:funziona-0.6", "q2": "s2i:serve-0.4", "big_at": "s2i:quale"}},
    {"at": "s2j", "scene": "not_transfer", "p": {"l_at": "s2j:settimana", "r_at": "s2j:metà", "vv_at": "s2j:viceversa"}},
    {"at": "s2k", "broll": ["bar", "gym"], "zoom": (1.0, 1.1)},

    # ---------------- 3 · lo studio ----------------
    chap("s3", "02", "Lo studio del 2024"),
    {"at": "s3a", "scene": "study_card", "p": {"chips": [("Persone già allenate", "user", "s3b:persone"), ("9 settimane", "cal", "s3b:nove"), ("Allenamento supervisionato", "eye", "s3b:supervisionato")]}},
    {"at": "s3c", "scene": "design", "p": {"rowA_at": "s3c:un", "rowB_at": "s3c:l'altro", "gap_at": "s3c:completamente", "call_at": "s3d:qui"}},
    {"at": "s3e", "scene": "result_bars", "p": {"kick": "Risultato 1", "title": "Crescita muscolare delle gambe", "bars": [("Continuo", 420, "#e9e9ec"), ("Con pausa", 415, "#71717a")],
                                                "verdict": "≈ Simile: nessun vantaggio", "verdict_at": "s3e:nessun", "bars_at": "s3e:sulla"}},
    {"at": "s3f", "scene": "result_bars", "p": {"kick": "Risultato 2", "title": "Forza", "bars": [("Continuo", 470, "#e9e9ec"), ("Con pausa", 330, "#ef4b40")],
                                                "verdict": "Continuo > con pausa", "verdict_at": "s3f:maggiori", "bars_at": "s3f:il", "vcls": "r"}},
    {"at": "s3g", "scene": "errore", "p": {"err_at": "s3g:errore"}, "sfx": None},
    {"at": "s3h", "scene": "says", "p": {"kick": "Cosa dice lo studio", "title": "Una cosa precisa", "items": [
        ("Persone allenate, programma supervisionato", "s3h:persone"), ("Una settimana di stop, inserita a metà", "s3h:una#2"),
        ("Ipertrofia: nessun miglioramento", "s3h:migliorato-0.6"), ("Forza: guadagni ridotti rispetto alla continuità", "s3h:ridotto-0.3")]}},
    {"at": "s3i", "scene": "says", "p": {"kick": "Cosa NON dice", "title": "Nulla su…", "good": False, "items": [
        ("Uno scarico fatto con meno serie", "s3i:riducendo-0.5"), ("Uno scarico con più ripetizioni in riserva", "s3i:lasciando-0.5"),
        ("Chi dorme poco, ha tanto stress o dolori", "s3i:dormendo-0.5")]}},
    {"at": "s3j", "scene": "quote", "p": {"text": "Uno studio risponde alla domanda che ha posto.", "sub": "Non a tutte le domande che vorremmo fargli.", "sub_at": "s3j:non", "hl": "che ha posto"}},
    {"at": "s3k", "scene": "tool", "p": {"rit_at": "s3k:rituale-0.3", "str_at": "s3k:strumento-0.3", "first_at": "s3k:prima"}},

    # ---------------- 4 · perché le prestazioni calano ----------------
    chap("s4", "03", "Perché le prestazioni calano"),
    {"at": "s4a", "broll": "row", "zoom": (1.0, 1.1)},
    {"at": "s4a:prima-0.2", "scene": "causes_grid", "p": {"at": "s4a:almeno-0.3"}},
    {"at": "s4b", "broll": ["squat", "bar", "gym"], "zoom": (1.1, 1.02)},
    {"at": "s4c", "scene": "technique", "p": {"tech_at": "s4c:un'esecuzione-0.2", "end_at": "s4c:senza"}},
    {"at": "s4d", "scene": "volume_ramp", "p": {"bars_at": "s4d:aggiunto-0.3", "rec_at": "s4d:un", "fat_at": "s4d:accumulare"}},
    {"at": "s4e", "broll": ["sleep", "tired"], "zoom": (1.0, 1.12)},
    {"at": "s4f", "broll": ["eat", "bar"], "zoom": (1.0, 1.1)},
    {"at": "s4g", "broll": ["stress", "tired"], "zoom": (1.0, 1.1)},
    {"at": "s4h", "scene": "variability", "p": {"line_at": "s4h:le", "low_at": "s4h:una-0.2", "txt_at": "s4h:una"}},
    {"at": "s4i", "scene": "checklist", "p": {"kick": "Prima di cambiare programma", "title": "Le domande che mi faccio", "items": [
        ("Esecuzione cambiata?", "s4j"), ("Lavoro aumentato di recente?", "s4j:ho#2"), ("Come ho dormito?", "s4j:come"),
        ("Come ho mangiato?", "s4j:come#2"), ("Che periodo sto vivendo?", "s4j:che"), ("Una seduta, o diverse?", "s4j:calo-0.5")]}},
    {"at": "s4k", "scene": "cause_fix", "p": {"fix_at": "s4k:sistemare"}},

    # ---------------- 5 · tre casi ----------------
    chap("s5", "04", "Tre casi"),
    {"at": "s5a", "scene": "cases", "p": {"at": "s5a:tre"}},
    {"at": "s5b", "scene": "case1_log", "p": {"today_at": "s5b:oggi", "rest_at": "s5b:il"}},
    {"at": "s5c", "scene": "case1_steps", "p": {"s1": "s5c:annoti", "s2": "s5c:ti", "s3": "s5c:alla", "noise_at": "s5c:era"}},
    {"at": "s5d", "scene": "case2_chart", "p": {"line_at": "s5d:da", "sig": [("Inizi già stanco", "batt", "s5d:inizi"), ("Carichi più pesanti", "dumbbell", "s5d:carichi-0.2"), ("Poca voglia", "x", "s5d:poca")]}},
    {"at": "s5e", "broll": ["tired", "row"], "zoom": (1.1, 1.0)},
    {"at": "s5f", "scene": "two_steps", "p": {"kick": "Caso 2 · cosa fare", "kcol": "#f5b31b", "s1": "Controlla le cause", "s1_at": "s5f",
                                             "chips1": [("Sonno", "s5f:sonno"), ("Alimentazione", "s5f:alimentazione"), ("Stress", "s5f:stress"), ("Aumento del lavoro", "s5f:aumento")],
                                             "s2": "Valuta una riduzione temporanea dello stress allenante", "s2_at": "s5f:poi"}},
    {"at": "s5g", "broll": ["physio", "tired"], "zoom": (1.0, 1.1)},
    {"at": "s5h", "scene": "case3_paths", "p": {"mod_at": "s5h:puoi", "pro_at": "s5h:ma"}},
    {"at": "s5i", "scene": "loop_back", "p": {"back_at": "s5i:ma"}},
    {"at": "s5j", "scene": "cases", "p": {"at": "s5j", "verdicts": [("Osserva e riprova", "s5j:tre"), ("Indaga, poi riduci", "s5j:tre#2"), ("Professionista", "s5j:valutazioni")]}},

    # ---------------- 6 · esempio pratico ----------------
    chap("s6", "05", "Un esempio pratico"),
    {"at": "s6a", "scene": "stamp_word", "p": {"word": "Esempio illustrativo", "kick": "Un esempio pratico", "sub": "non una prescrizione da copiare", "sub_at": "s6a:non", "size": 104}, "sfx": None},
    {"at": "s6b", "broll": ["app", "row"], "zoom": (1.0, 1.06)},
    {"at": "s6c", "scene": "program", "p": {"rows_at": ["s6c:squat", "s6c:panca", "s6c:rematore", "s6c:più"], "red_at": "s6d:da", "rir_at": "s6d:tre-0.3", "same_at": "s6d:tenere", "title_at": "s6d:per"}},
    {"at": "s6e", "broll": ["squat", "bench"], "zoom": (1.12, 1.02)},
    {"at": "s6f", "scene": "stop_vs_reduce", "p": {"stop_at": "s6f:uno", "red_at": "s6f:ridurre"}},
    {"at": "s6g", "scene": "big", "p": {"kick": "Il punto fondamentale", "text": "Quantità e durata dipendono dal caso", "hl": "dal caso"}},
    {"at": "s6h", "scene": "sliders", "p": {"p1_at": "s6h:per", "p2_at": "s6h:per#3", "f_at": "s6h:dipende"}},
    {"at": "s6i", "scene": "nomagic", "p": {"p_at": "s6i:percentuale-0.3", "d_at": "s6i:durata-0.3"}},

    # ---------------- 7 · cosa osservare dopo ----------------
    chap("s7", "06", "Cosa osservare dopo"),
    {"at": "s7a", "broll": "app", "zoom": (1.12, 1.0)},
    {"at": "s7b", "scene": "monitors", "p": {"at": ["s7b:primo", "s7c", "s7d"],
                                            "qs": [["s7b:ti", "s7b:carichi-0.2", "s7b:tecnica-0.2"], ["s7c:quando", "s7c:o"], ["s7d:hai", "s7d:ti"]]}},
    {"at": "s7e", "scene": "confirm", "p": {"ok_at": "s7e:l'ipotesi"}},
    {"at": "s7f", "scene": "reconsider", "p": {"alt_at": None}},
    {"at": "s7g", "scene": "noid", "p": {"a_at": "s7g:=se", "b_at": "s7g:=se#2-0.2"}},

    # ---------------- 8 · LB System ----------------
    chap("s8", "07", "Il metodo LB System"),
    {"at": "s8a", "scene": "big", "p": {"kick": "In sintesi", "text": "Il valore sta nel confronto", "hl": "confronto"}},
    {"at": "s8b", "scene": "loop4", "p": {"nodes": ["s8b:dati", "s8b:contesto", "s8b:decisione", "s8b:verifica"]}},
    {"at": "s8c", "scene": "lbsystem", "p": {"f_at": ["s8c:la", "s8c:con#2", "s8c:l'assistenza-0.4"]}},
    {"at": "s8d", "scene": "endcard", "p": {"nexus_at": "s8d:allenarti-0.6", "sub_at": "s8e:iscriviti-0.2"}},
]

POPS = [
    {"at": "s1a:mi-0.1", "to": "s1b:sono-0.2", "kind": "bubble", "pos": "center", "p": {"text": "«Mi serve uno scarico?»"}},
    {"at": "s2c:ridurre-0.2", "to": "s2c$+0.2", "p": {"title": "Ridurre lo stress allenante", "icon": "down", "lines": [("in modi molto diversi", "s2c:modi")]}},
    {"at": "s2k:studio-0.4", "to": "s2k$+0.3", "p": {"title": "Lo studio del 2024", "icon": "note", "lines": []}},
    {"at": "s4b+0.2", "to": "s4b$+0.1", "p": {"title": "1 · Condizioni di esecuzione", "icon": "sliders", "lines": [
        ("Palestra, macchinario, orario?", "s4b:palestra-0.3"), ("Riscaldamento diverso?", "s4b:riscaldamento-0.4"),
        ("Ordine degli esercizi?", "s4b:l'ordine-0.3"), ("Meno recupero tra le serie?", "s4b:recuperato-0.3")]}},
    {"at": "s4e+0.15", "to": "s4e$+0.1", "p": {"title": "3 · Sonno", "icon": "moon", "lines": [("Quante ore nelle ultime notti?", "s4e:quante"), ("Anche poche notti corte si sentono", "s4e:anche")]}},
    {"at": "s4f+0.15", "to": "s4f$+0.1", "p": {"title": "4 · Alimentazione", "icon": "food", "lines": [("Sei in deficit calorico?", "s4f:sei"), ("Mangiato poco prima?", "s4f:hai"), ("Proteine e carboidrati sufficienti?", "s4f:stai")]}},
    {"at": "s4g+0.15", "to": "s4g$+0.1", "p": {"title": "5 · Stress", "icon": "bolt", "lines": [("Lavoro · studio · relazioni", "s4g:lavoro"), ("Si somma all'allenamento", "s4g:si")]}},
    {"at": "s5e+0.15", "to": "s5e$+0.1", "pos": "left", "p": {"title": "Caso 2", "icon": "trend", "lines": [("Non più una seduta isolata", "s5e:non"), ("Più segnali, stessa direzione", "s5e:sono")]}},
    {"at": "s5g+0.15", "to": "s5g$+0.1", "p": {"title": "Caso 3 · dolore persistente", "icon": "pain", "lines": [("Spalla · ginocchio · schiena", "s5g:un"), ("Da giorni o settimane", "s5g:che"), ("Peggiora con certi esercizi", "s5g:peggiora")]}},
    {"at": "s6b+0.15", "to": "s6b$+0.1", "p": {"title": "Caso 2", "icon": "trend", "lines": [("Calo su più esercizi", "s6b:calo"), ("Recupero difficile", "s6b:recupero"), ("Cause ovvie già controllate", "s6b:cause-0.4")]}},
    {"at": "s6e+0.15", "to": "s6e$+0.1", "p": {"title": "Gesti familiari", "icon": "loop", "lines": [("Continui a praticare il movimento", "s6e:ti"), ("Non perdi il ritmo", "s6e:non"), ("Rientro naturale al lavoro pieno", "s6e:quando")]}},
    {"at": "s7a+0.1", "to": "s7a$+0.2", "p": {"title": "Dopo l'intervento", "icon": "eye", "lines": [("Cosa devi osservare?", "s7a:cosa")]}},
]

def SFX_EXTRA(T):
    return [("riser", T("s1f$") - 3.6)]
