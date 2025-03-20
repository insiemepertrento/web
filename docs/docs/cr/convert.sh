#!/bin/bash

# Legge tutti i file PDF nella directory corrente
for file in *.pdf; do
    # Ottiene il nome del file senza estensione
    basename="${file%.pdf}"
    # Controlla se il nome del file è tutto in maiuscolo
    if [[ "$basename" =~ ^[A-Z_]+$ ]]; then
        # Converte il nome in minuscolo
        lowercase="$(echo "$basename" | tr 'A-Z' 'a-z')"
        # Rinomina il file
        mv "$file" "$lowercase.pdf"
        echo "Rinominato: $file -> $lowercase.pdf"
    fi
done

echo "Rinomina completata."

