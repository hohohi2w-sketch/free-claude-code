# Schaufenster: Portfolio und Demo-Websites

`index.html` ist die Portfolio-Seite von „Schaufenster“. Sie zeigt die drei Konzepte unten und verlinkt auf sie.

## Online stellen (kostenlos, ca. 5 Minuten)

1. Diesen Ordner `websites/` herunterladen (auf GitHub: Code → Download ZIP, dann entpacken).
2. Auf https://app.netlify.com/drop gehen, kostenlos registrieren (mit der neuen Gmail-Adresse).
3. Den Ordner `websites` in das Feld ziehen. Nach ein paar Sekunden ist die Seite online, z. B. unter `irgendwas.netlify.app`.
4. Unter Site configuration → Site name den Namen auf `schaufenster` ändern (falls frei), dann heißt die Adresse `schaufenster.netlify.app`.
5. Damit das Kontaktformular funktioniert: unter Forms die Formularerkennung (Form detection) einschalten und den Ordner noch einmal hochladen. Nachrichten erscheinen dann im Netlify-Dashboard, auf Wunsch auch per E-Mail.
6. Die Adresse bei Instagram unter Profil bearbeiten → Links eintragen.

Vor dem Veröffentlichen: E-Mail-Adresse in `index.html` prüfen (`schaufenster.studio@gmail.com`) und Impressum sowie Datenschutzerklärung ergänzen.

## Demo-Websites

Drei eigenständige One-Pager, jeweils eine einzige `index.html` ohne Build-Schritt.
Zum Anschauen einfach im Browser öffnen, zum Veröffentlichen den Ordner auf einen
beliebigen Webspace hochladen (z. B. Netlify, GitHub Pages, Strato, IONOS).

| Ordner | Laden | Besonderheit |
| --- | --- | --- |
| `feinschliff/` | Nagel- & Beautystudio, Hamburg | Design-Konfigurator (Form, Farbe, Finish) füllt das Terminformular |
| `mahlgrad/` | Café & Backstube, Berlin | Steckbuchstaben-Tafel und „Jetzt geöffnet“ richten sich nach Wochentag und Uhrzeit |
| `halbschatten/` | Fotografin, München | Kontaktbogen-Galerie mit Filter und Großansicht |

Alle Namen, Adressen, Preise und Telefonnummern sind erfunden (die Nummern stammen aus
den Rufnummernblöcken, die die Bundesnetzagentur für Film und Fernsehen reserviert hat).

## Vor dem echten Einsatz anpassen

- Texte, Preise, Öffnungszeiten, Adresse und Telefonnummer ersetzen.
- Fußzeile: Hinweis „Demo-Website“ entfernen, Impressum (§ 5 DDG) und Datenschutzerklärung verlinken.
- Formulare verschicken noch nichts. Für echten Versand einen Formulardienst anbinden
  (z. B. Formspree, Netlify Forms oder ein eigenes PHP-Skript) und den `submit`-Handler im Skript anpassen.
- Fotografen-Seite: Die Bilder werden per Canvas erzeugt. Für echte Fotos die `<canvas>`-Elemente
  durch `<img>` ersetzen.
- Schriften kommen von Google Fonts. Für DSGVO-sauberen Betrieb die Schriften lokal einbinden.
