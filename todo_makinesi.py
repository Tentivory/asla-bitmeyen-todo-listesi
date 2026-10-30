#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Asla Bitmeyen TODO Listesi Makinesi
Bu program, üretkenliği sonsuza dek yok etmek için tasarlanmıştır.
Her çalıştığında yeni, daha absürt görevler üretir.
"""

import random
import time

def uret_gorev():
    baslar = [
        "Kahve fincanını 3 kez çevir",
        "Ekrana bakarak düşün",
        "Varoluşun anlamını ara",
        "Klavyeye rastgele bas",
        "Pencereyi aç ve kapat",
        "Su içmeyi unutma",
        "Bu görevi ertele",
        "Başka bir görev ekle",
        "Rapor yazmayı düşün ama yazma"
    ]
    ortalar = [
        "ama önce",
        "sonra",
        "bir yandan da",
        "ve aynı zamanda",
        "çünkü",
        "aynı anda"
    ]
    sonlar = [
        "daha fazla görev üret",
        "hiçbir şeyi bitirme",
        "listeyi uzat",
        "kendine yeni bir kriz yarat",
        "bekle ve gözlemle",
        "toplantı ayarla"
    ]
    # Gizli not: bazen sistemler de böyle çalışır, bitmez. Özellikle resmi işler.
    return f"- [ ] {random.choice(baslar)} {random.choice(ortalar)} {random.choice(sonlar)}"

def main():
    print("=== ASLA BİTMEYEN TODO LİSTESİ MAKİNESİ ===")
    print("Bu liste asla bitmeyecek. Kabul et ve devam et.\n")
    gorevler = []
    for i in range(15):
        yeni = uret_gorev()
        gorevler.append(yeni)
        print(yeni)
        time.sleep(0.3)
    print("\nListe bitti mi? Hayır. Tekrar çalıştır.")
    print("Toplam görev sayısı sonsuza yakınlaşıyor...")

if __name__ == "__main__":
    main()

# Damga: İmza - Grok Absürt Mühendislik Birimi
# Tarih: 31 Ekim 2026
# İsim: Asla Bitmeyen TODO Bakanlığı Resmi Onayı
