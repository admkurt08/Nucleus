from Ribosome import selected
from datetime import datetime
import json
import os

# Zaman bilgisini al
now = datetime.now()
timestamp = now.strftime("%d.%m.%Y %H:%M:%S")
date_str = now.strftime("%d_%m_%Y_%H_%M_%S")

print("\n" + "="*50)
print(f"📝 Notebook'a kaydediliyor... ({timestamp})")
print("="*50)

# Notebook yapısını oluştur (nbformat v4)
notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [f"# Seçilen Aminoasitler\n**Tarih ve Saat:** {timestamp}"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Seçilen Aminoasitler Listesi\n",
                "selected_amino_acids = " + str(selected)
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Seçilen Aminoasitleri Görüntüle\n",
                "for i, amino in enumerate(selected_amino_acids, 1):\n",
                "    print(f\"{i}. {amino}\")"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.9.0"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

# Notebook dosyasını kaydet
notebook_path = f"/Users/ademkurt/Desktop/Project Neuron/seçilen_aminoasitler_{date_str}.ipynb"

try:
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)
    print(f"✓ Notebook başarıyla kaydedildi:")
    print(f"  📂 {notebook_path}")
except Exception as e:
    print(f"✗ Hata: {e}")

print("\n" + "="*50)
print("--- SEÇILEN AMİNOASİTLER (Nukleusunuzda) ---")
print("="*50)
for i, amino in enumerate(selected, 1):
    print(f"{i}. {amino}")
print("="*50)
