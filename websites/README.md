# Demo-Websites für lokale Läden

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
