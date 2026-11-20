"""Simulierter Markttest: 100 fiktive Ladenbesitzer:innen in Aachen reagieren auf das Angebot
"Laden-Website 690 € einmalig + 15 €/Monat". Alle Personen sind erfunden; die Reaktionen sind
Einschätzungen, keine Umfragedaten."""
from collections import Counter, defaultdict
PREIS = 690
DATEN = """
Friseur|Pontviertel|alt|j|800|Kauf|Alte Seite, nicht handytauglich|Meine Seite sieht aus wie 2014. Wenn das unter 1.000 € bleibt, machen wir's.
Friseur|Burtscheid|keine|j|300|Nein|Instagram reicht|Termine laufen über Instagram und Telefon, das reicht mir.
Friseur|Innenstadt|gut|j|0|Nein|Hat schon eine gute Website|Wir haben eine Agentur, die das betreut.
Friseur|Brand|keine|n|500|Vielleicht|Preis zu hoch|Für 500 € sofort, für 690 € muss ich überlegen.
Friseur|Eilendorf|alt|n|400|Vielleicht|Will monatlich zahlen|Lieber 30 € im Monat als alles auf einmal.
Friseur|Frankenberger Viertel|keine|j|700|Kauf|Will Terminanfragen online|Wenn Kunden direkt Termine anfragen können, bin ich dabei.
Friseur|Laurensberg|alt|n|0|Nein|Keine Zeit|Ich hab keine Zeit, mich darum zu kümmern.
Friseur|Haaren|keine|j|250|Nein|Kein Budget|Gerade ist jeder Euro verplant.
Friseur|Ostviertel|keine|j|600|Vielleicht|Will echte Referenzen sehen|Zeig mir erst eine echte Seite, die du gemacht hast.
Friseur|Kornelimünster|gut|n|0|Nein|Hat schon eine gute Website|Läuft bei uns über ein Buchungsportal, das passt.
Barbershop|Innenstadt|keine|j|450|Vielleicht|Preis zu hoch|Für 450 € mit allem, dann ja.
Barbershop|Pontviertel|keine|j|0|Nein|Instagram reicht|Meine Kunden finden mich über TikTok und Insta.
Friseur|Forst|alt|n|900|Kauf|Alte Seite, nicht handytauglich|Ehrlich, meine Seite ist peinlich. Mach mir was Ordentliches.
Friseur|Richterich|keine|n|300|Nein|Familie macht das|Mein Neffe bastelt mir das irgendwann.
Nagelstudio|Innenstadt|keine|j|700|Kauf|Design-Konfigurator überzeugt|Das mit dem Design-Ausprobieren will ich genau so.
Nagelstudio|Burtscheid|keine|j|400|Vielleicht|Preis zu hoch|Sieht toll aus, aber 690 € ist für mich viel.
Nagelstudio|Eilendorf|keine|j|0|Nein|Instagram reicht|Meine Kundinnen buchen per DM.
Nagelstudio|Haaren|alt|j|600|Vielleicht|Will echte Referenzen sehen|Gefällt mir, aber du hast noch keine echten Kunden, oder?
Kosmetikstudio|Frankenberger Viertel|alt|n|1200|Kauf|Will bei Google gefunden werden|Ich will bei Google gefunden werden. Was kostet das komplett?
Kosmetikstudio|Laurensberg|gut|j|0|Nein|Macht es selbst mit Baukasten|Ich mach das selbst mit Wix, reicht.
Nagelstudio|Ostviertel|keine|j|350|Vielleicht|Will monatlich zahlen|Kann ich das in Raten zahlen?
Lash & Brow Studio|Innenstadt|keine|j|700|Kauf|Preisfragen per DM nerven|Ich beantworte jeden Tag 20-mal die gleiche Preisfrage. Ja, bitte.
Kosmetikstudio|Brand|alt|n|500|Vielleicht|Will Inhalte selbst ändern|Nur wenn ich Preise selbst ändern kann.
Nagelstudio|Pontviertel|keine|j|200|Nein|Kein Budget|Ich hab gerade erst eröffnet, kein Geld dafür.
Kosmetikstudio|Kornelimünster|keine|n|0|Nein|Keine Zeit|Ich arbeite allein, für sowas hab ich keinen Kopf.
Nagelstudio|Hörn|keine|j|550|Vielleicht|Später|Frag mich im Januar nochmal.
Café|Pontviertel|keine|j|900|Kauf|Ständige Fragen nach Öffnungszeiten|Leute fragen ständig, ob wir offen haben. Die Jetzt-geöffnet-Anzeige will ich.
Café|Frankenberger Viertel|alt|j|600|Vielleicht|Will echte Referenzen sehen|Gefällt mir. Hast du schon ein echtes Café gemacht?
Bäckerei|Brand|gut|n|0|Nein|Kette oder Zentrale macht das|Wir sind Filiale, das macht die Zentrale.
Café|Innenstadt|keine|j|1100|Kauf|Tafel-Idee überzeugt|Die Tafel mit dem Kuchen des Tages ist genau unser Ding.
Bäckerei|Eilendorf|alt|n|400|Vielleicht|Will Inhalte selbst ändern|Wenn ich die Preise selbst anpassen kann, vielleicht.
Café|Burtscheid|keine|j|0|Nein|Google-Eintrag reicht|Google Maps zeigt schon alles an.
Konditorei|Innenstadt|alt|n|1500|Kauf|Will Vorbestellungen online|Wenn man darüber Torten vorbestellen kann, sofort.
Café|Ostviertel|keine|j|300|Nein|Kein Budget|Wir kämpfen gerade mit den Energiekosten.
Bäckerei|Richterich|keine|n|0|Nein|Hört bald auf|Ich höre in zwei Jahren auf, das lohnt sich nicht mehr.
Café|Laurensberg|keine|j|500|Vielleicht|Preis zu hoch|Für 500 hätte ich direkt ja gesagt.
Eiscafé|Pontviertel|keine|j|0|Nein|Instagram reicht|Im Sommer läuft's von allein.
Café|Haaren|alt|n|700|Vielleicht|Später|Erst nach dem Weihnachtsgeschäft.
Restaurant|Innenstadt|alt|n|1200|Kauf|Speisekarte online veraltet|Unsere Karte online ist drei Jahre alt. Das muss weg.
Imbiss|Ostviertel|keine|n|0|Nein|Lieferportal reicht|Wir sind auf Lieferando, das reicht.
Pizzeria|Burtscheid|alt|n|300|Nein|Kein Budget|Für so was geb ich nicht so viel aus.
Restaurant|Pontviertel|gut|j|0|Nein|Hat schon eine gute Website|Haben wir, mit Reservierung.
Restaurant|Frankenberger Viertel|keine|j|800|Vielleicht|Will Reservierung oder Buchung|Nur mit Online-Reservierung.
Dönerladen|Haaren|keine|n|0|Nein|Kein Interesse|Brauch ich nicht.
Restaurant|Kornelimünster|alt|n|1000|Vielleicht|Will echte Referenzen sehen|Zeig mir was Echtes aus der Gastro, dann reden wir.
Imbiss|Eilendorf|keine|n|200|Nein|Kein Budget|Zu teuer für einen Imbiss.
Restaurant|Laurensberg|alt|j|1500|Kauf|Will mehr Feiern und Events|Wir wollen mehr Feiern buchen. Dafür brauchen wir eine gute Seite.
Asiatisches Restaurant|Innenstadt|keine|j|500|Vielleicht|Will zweisprachig|Geht das auch zweisprachig?
Weinbar|Pontviertel|alt|j|650|Vielleicht|Preis zu hoch|Bei 650 wäre ich sofort dabei.
Restaurant|Brand|keine|n|0|Nein|Familie macht das|Meine Tochter macht das.
Boutique|Innenstadt|alt|j|900|Vielleicht|Will Onlineshop|Ohne Onlineshop bringt mir das wenig.
Buchladen|Frankenberger Viertel|alt|n|600|Vielleicht|Will Inhalte selbst ändern|Ich will Lesungen selbst eintragen.
Second-Hand-Laden|Pontviertel|keine|j|300|Nein|Instagram reicht|Unsere Teile verkaufen wir über Insta-Stories.
Fahrradladen|Burtscheid|alt|n|1000|Kauf|Will Terminanfragen online|Werkstatt-Termine online, das spart uns viele Anrufe.
Unverpacktladen|Ostviertel|keine|j|500|Vielleicht|Will monatlich zahlen|Monatlich zahlen wäre besser.
Spielwarenladen|Innenstadt|gut|n|0|Nein|Hat schon eine gute Website|Wir haben einen Shopify-Shop.
Optiker|Brand|gut|n|0|Nein|Kette oder Zentrale macht das|Läuft über unseren Verbund.
Weinhandel|Laurensberg|alt|n|800|Vielleicht|Will echte Referenzen sehen|Interessant. Wer hat das schon bei dir gemacht?
Geschenkeladen|Kornelimünster|keine|j|400|Vielleicht|Preis zu hoch|Unter 500 € bin ich dabei.
Plattenladen|Pontviertel|keine|j|0|Nein|Instagram reicht|Unsere Leute sind auf Insta und Discogs.
Schreinerei|Eilendorf|alt|n|1500|Kauf|Will bei Google gefunden werden|Wenn ich bei Google oben stehe, rechnet sich das mit einem Auftrag.
Malerbetrieb|Haaren|keine|n|800|Vielleicht|Später|Ich hab die Bücher voll, frag in drei Monaten.
Elektrobetrieb|Richterich|alt|n|1000|Kauf|Sucht Azubis und Personal|Wir suchen Azubis, dafür brauchen wir eine moderne Seite.
Fliesenleger|Brand|keine|n|0|Nein|Läuft über Empfehlungen|Läuft alles über Empfehlung.
Goldschmiede|Innenstadt|alt|j|1200|Kauf|Will Galerie für Arbeiten|Meine Stücke müssen gut aussehen. Galerie wie beim Fotografen, bitte.
Änderungsschneiderei|Burtscheid|keine|n|300|Nein|Kein Budget|Zu teuer für eine Änderungsschneiderei.
Dachdecker|Laurensberg|gut|n|0|Nein|Hat schon eine gute Website|Haben wir schon.
Kfz-Werkstatt|Eilendorf|alt|n|700|Vielleicht|Zweifel, ob es zur Branche passt|Du machst ja eher Cafés und Nagelstudios, oder?
Gärtnerei|Kornelimünster|keine|n|600|Vielleicht|Will echte Referenzen sehen|Zeig mal was für Gärtner.
Raumausstatter|Frankenberger Viertel|alt|n|600|Vielleicht|Preis zu hoch|Für 600 ja.
Physiotherapie|Burtscheid|alt|n|1200|Kauf|Sucht Azubis und Personal|Wir suchen Therapeuten und brauchen eine Seite, die nicht nach 2010 aussieht.
Heilpraktikerin|Frankenberger Viertel|keine|j|500|Vielleicht|Rechtliche Bedenken|Bei Heilberufen gibt es Werberegeln. Kennst du dich da aus?
Ergotherapie|Haaren|gut|n|0|Nein|Hat schon eine gute Website|Haben wir.
Logopädie|Laurensberg|alt|n|800|Vielleicht|Will barrierefrei|Muss barrierefrei sein.
Massagepraxis|Innenstadt|keine|j|400|Vielleicht|Preis zu hoch|Für 400 sofort.
Hebammenpraxis|Ostviertel|keine|j|600|Vielleicht|Später|Klingt gut, aber wir haben gerade keine Zeit.
Psychotherapie|Burtscheid|keine|n|0|Nein|Portal oder Verzeichnis reicht|Ich bin über die Kammer und Doctolib gelistet.
Zahnarztpraxis|Innenstadt|gut|n|0|Nein|Hat schon eine gute Website|Das macht unsere Agentur.
Yogastudio|Frankenberger Viertel|alt|j|800|Kauf|Will Inhalte selbst ändern|Einen Kursplan, den ich selbst ändere? Dann ja.
Boxstudio|Pontviertel|keine|j|300|Nein|Instagram reicht|Instagram ist unsere Website.
Pilatesstudio|Burtscheid|keine|j|600|Vielleicht|Will Reservierung oder Buchung|Nur mit Buchungssystem.
Fitnessstudio|Eilendorf|gut|n|0|Nein|Kette oder Zentrale macht das|Kette, macht die Zentrale.
Tanzschule|Laurensberg|alt|n|1200|Kauf|Alte Seite, nicht handytauglich|Wir verlieren Anmeldungen, weil die Seite auf dem Handy nicht geht.
Personal Trainer|Innenstadt|keine|j|350|Vielleicht|Preis zu hoch|Für 350 € direkt.
Fotografin|Burtscheid|alt|j|900|Kauf|Konzept passt genau|Das Halbschatten-Konzept ist genau mein Stil.
Fotograf|Innenstadt|gut|j|0|Nein|Macht es selbst mit Baukasten|Ich mache meine Seite selbst mit Squarespace.
Hochzeitsfotografin|Brand|alt|j|700|Vielleicht|Will echte Referenzen sehen|Wie viele Seiten hast du schon live?
Fotostudio|Pontviertel|keine|n|500|Vielleicht|Preis zu hoch|Für 500 € ja.
Blumenladen|Burtscheid|keine|j|700|Kauf|Will Vorbestellungen online|Wenn Kunden Sträuße vorbestellen können: sofort.
Blumenladen|Eilendorf|alt|n|300|Nein|Kein Budget|Blumen sind knapp kalkuliert.
Floristin|Frankenberger Viertel|keine|j|500|Vielleicht|Später|Nach Muttertag.
Blumenladen|Brand|keine|n|0|Nein|Hört bald auf|Ich bin 67, das lohnt sich nicht mehr.
Tattoostudio|Pontviertel|keine|j|0|Nein|Instagram reicht|Tattoo läuft komplett über Instagram.
Tattoostudio|Innenstadt|alt|j|800|Vielleicht|Will genauen Preis vorher|Mit Galerie und Anfrageformular, ja. Was kostet das genau?
Fahrschule|Haaren|alt|n|900|Kauf|Will Anmeldungen online|Schüler wollen sich online anmelden. Mach das.
Nachhilfe|Laurensberg|keine|j|300|Nein|Kein Budget|Zu teuer für mich als Einzelperson.
Hundesalon|Eilendorf|keine|j|500|Vielleicht|Preis zu hoch|Für 500 bin ich dabei.
Textilreinigung|Innenstadt|alt|n|0|Nein|Kein Interesse|Meine Kunden kommen sowieso vorbei.
Musikschule|Burtscheid|alt|n|1000|Vielleicht|Will Inhalte selbst ändern|Nur wenn ich Kurse selbst eintragen kann.
Kiosk|Ostviertel|keine|n|0|Nein|Kein Interesse|Ein Kiosk braucht keine Website.
"""
leute = [dict(zip("branche stadtteil website insta budget reaktion grund zitat".split(), z.split("|"))) for z in DATEN.strip().splitlines()]
for p in leute: p["budget"] = int(p["budget"])
assert len(leute) == 100
# Plausibilität: Kauf nur, wenn das Budget den Preis deckt
assert all(p["budget"] >= PREIS for p in leute if p["reaktion"] == "Kauf")

r = Counter(p["reaktion"] for p in leute)
print("REAKTIONEN", dict(r))
print("\nNACH WEBSITE-STAND")
for w in ["keine", "alt", "gut"]:
    g = [p for p in leute if p["website"] == w]; c = Counter(p["reaktion"] for p in g)
    print(f"  {w:6} n={len(g):3}  Kauf {c['Kauf']:2}  Vielleicht {c['Vielleicht']:2}  Nein {c['Nein']:2}")
print("\nGRÜNDE NEIN"); [print(f"  {n:2}  {g}") for g, n in Counter(p["grund"] for p in leute if p["reaktion"] == "Nein").most_common()]
print("\nGRÜNDE VIELLEICHT"); [print(f"  {n:2}  {g}") for g, n in Counter(p["grund"] for p in leute if p["reaktion"] == "Vielleicht").most_common()]
print("\nGRÜNDE KAUF"); [print(f"  {n:2}  {g}") for g, n in Counter(p["grund"] for p in leute if p["reaktion"] == "Kauf").most_common()]
# Preiskurve: wer würde bei Preis X zahlen (Budget >= X), nur Personen ohne harten Nein-Grund
offen = [p for p in leute if p["reaktion"] != "Nein"]
print("\nPREISKURVE (Kauf + Vielleicht, Budget >= Preis)")
for preis in [390, 490, 590, 690, 790, 990, 1290]:
    n = sum(p["budget"] >= preis for p in offen)
    print(f"  {preis:5} €  {n:3} Kund:innen  Umsatz {n*preis:7,} €".replace(",", "."))
print("\nBRANCHEN MIT KAUF")
b = defaultdict(Counter)
for p in leute:
    key = p["branche"].split()[0] if p["branche"] not in ("Lash & Brow Studio",) else "Kosmetik"
    b[key][p["reaktion"]] += 1
for k, c in sorted(b.items(), key=lambda x: -x[1]["Kauf"]):
    if c["Kauf"]: print(f"  {k:22} Kauf {c['Kauf']}  von {sum(c.values())}")
print("\nUMSATZ BEI 690 €:", r["Kauf"] * PREIS, "€ einmalig +", r["Kauf"] * 15, "€ pro Monat")
with open("100-kunden.txt", "w", encoding="utf-8") as f:
    f.write("SIMULIERTER MARKTTEST – 100 erfundene Ladenbesitzer:innen in Aachen\nAngebot: Laden-Website 690 € + 15 €/Monat\nKeine echten Personen, keine echten Umfragedaten.\n\n")
    for i, p in enumerate(leute, 1):
        f.write(f"{i:3}. {p['reaktion'].upper():10} {p['branche']}, {p['stadtteil']} (Website: {p['website']}, Budget bis {p['budget']} €)\n     „{p['zitat']}“\n")
