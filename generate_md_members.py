import csv
import html
import os

# Nome del file CSV
csv_filename = "docs" + os.sep + "_data" + os.sep + "candidate_pages.csv"
# Crea la cartella per le pagine se non esiste
os.makedirs("docs" + os.sep + "people", exist_ok=True)


def clean_text(text):
    """Sostituisce i caratteri speciali con i rispettivi codici HTML."""
    if text:
        # Converti i caratteri speciali in codici HTML
        text = html.escape(text)
        # Rispetta gli a capo
        text = text.replace("\n", "<br/>")
        text = text.replace(":", "&#58;")
    return text

with open(csv_filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')

    for row in reader:
        print(row)
        # Genera il permalink dal nome
        permalink = "/" + row['name'].lower().replace(" ", "_")
        namefile = row['name'].lower().replace(" ", "_")

        # Crea il nome del file
        filename = "docs" + os.sep + "people" + os.sep + namefile + ".md"

        # Crea il contenuto del file Markdown
        content = f"""---
layout: personal_page
member: {clean_text(row['name'])}
permalink: {permalink}
namefile: {namefile}
cv: {clean_text(row['cv'])}
records: {clean_text(row['records'])}
photo: {clean_text(row['photo'].replace(".jpg", ".png"))}
desc: {clean_text(row['desc'])}
facebook: {clean_text(row['facebook'])}
instagram: {clean_text(row['instagram'])}
linkedin: {clean_text(row['linkedin'])}
video_instagram: {clean_text(row['video'])}
slogan: {clean_text(row['slogan'])}
---
"""

        # Scrivi il contenuto nel file Markdown
        with open(filename, "w", encoding="utf-8") as mdfile:
            mdfile.write(content)

print("Pagine generate con successo!")
