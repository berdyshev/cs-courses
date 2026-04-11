#!/bin/bash
# Конвертує всі роздатки та домашні завдання у DOCX

for dir in lesson*/; do
    for md in "$dir"*.md; do
        out="${md%.md}.docx"
        echo "Конвертую $md → $out"
        pandoc "$md" -o "$out"
    done
done

echo "Готово! Відкрий .docx у LibreOffice і роздрукуй."
