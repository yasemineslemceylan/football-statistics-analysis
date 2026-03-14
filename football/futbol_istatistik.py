# -*- coding: utf-8 -*-

from collections import defaultdict

takimlar = {
    "Galatasaray": {"puan": 0, "gol_atilan": 0, "gol_yenilen": 0, "galibiyet": 0, "beraberlik": 0, "maglubiyet": 0},
    "Fenerbahçe": {"puan": 0, "gol_atilan": 0, "gol_yenilen": 0, "galibiyet": 0, "beraberlik": 0, "maglubiyet": 0},
    "Beşiktaş": {"puan": 0, "gol_atilan": 0, "gol_yenilen": 0, "galibiyet": 0, "beraberlik": 0, "maglubiyet": 0},
    "Trabzonspor": {"puan": 0, "gol_atilan": 0, "gol_yenilen": 0, "galibiyet": 0, "beraberlik": 0, "maglubiyet": 0},
}

oyuncular = {
    "Mauro Icardi": {"takim": "Galatasaray", "gol": 18, "asist": 5},
    "Edin Džeko": {"takim": "Fenerbahçe", "gol": 15, "asist": 7},
    "Vincent Aboubakar": {"takim": "Beşiktaş", "gol": 12, "asist": 4},
    "Anastasios Bakasetas": {"takim": "Trabzonspor", "gol": 10, "asist": 8},
    "Kerem Aktürkoğlu": {"takim": "Galatasaray", "gol": 8, "asist": 11},
    "Sebastian Szymański": {"takim": "Fenerbahçe", "gol": 6, "asist": 9},
}

maclar = [
    ("Galatasaray", 3, "Fenerbahçe", 1),
    ("Beşiktaş", 2, "Trabzonspor", 2),
    ("Fenerbahçe", 2, "Galatasaray", 2),
    ("Trabzonspor", 1, "Galatasaray", 2),
    ("Beşiktaş", 0, "Fenerbahçe", 1),
    ("Trabzonspor", 2, "Fenerbahçe", 1),
]


def puan_hesapla():
    for ev_sahibi, ev_gol, deplasman, dep_gol in maclar:
        takimlar[ev_sahibi]["gol_atilan"] += ev_gol
        takimlar[ev_sahibi]["gol_yenilen"] += dep_gol
        takimlar[deplasman]["gol_atilan"] += dep_gol
        takimlar[deplasman]["gol_yenilen"] += ev_gol
        if ev_gol > dep_gol:
            takimlar[ev_sahibi]["puan"] += 3
            takimlar[ev_sahibi]["galibiyet"] += 1
            takimlar[deplasman]["maglubiyet"] += 1
        elif ev_gol < dep_gol:
            takimlar[deplasman]["puan"] += 3
            takimlar[deplasman]["galibiyet"] += 1
            takimlar[ev_sahibi]["maglubiyet"] += 1
        else:
            takimlar[ev_sahibi]["puan"] += 1
            takimlar[deplasman]["puan"] += 1
            takimlar[ev_sahibi]["beraberlik"] += 1
            takimlar[deplasman]["beraberlik"] += 1


def cizgi(uzunluk=50):
    print("═" * uzunluk)


def baslik_yaz(baslik):
    cizgi()
    print(f"  {baslik}")
    cizgi()


def puan_durumu():
    baslik_yaz("LİG PUAN DURUMU")
    sirali = sorted(takimlar.items(), key=lambda x: (-x[1]["puan"], -x[1]["gol_atilan"] - x[1]["gol_yenilen"]))
    print(f"{'Sıra':<5} {'Takım':<15} {'O':<4} {'G':<4} {'B':<4} {'M':<4} {'A':<4} {'Y':<4} {'Puan':<6}")
    print("─" * 55)
    for i, (takim, istatistik) in enumerate(sirali, 1):
        o = istatistik["galibiyet"] + istatistik["beraberlik"] + istatistik["maglubiyet"]
        print(f"{i:<5} {takim:<15} {o:<4} {istatistik['galibiyet']:<4} {istatistik['beraberlik']:<4} "
              f"{istatistik['maglubiyet']:<4} {istatistik['gol_atilan']:<4} {istatistik['gol_yenilen']:<4} {istatistik['puan']:<6}")
    print()


def gol_krali():
    baslik_yaz("GOL KRALLIĞI (En çok gol atan oyuncular)")
    sirali = sorted(oyuncular.items(), key=lambda x: -x[1]["gol"])[:5]
    for i, (isim, veri) in enumerate(sirali, 1):
        print(f"  {i}. {isim:<22} {veri['takim']:<15} {veri['gol']} gol")
    print()


def asist_ligi():
    baslik_yaz("ASİST LİDERLERİ")
    sirali = sorted(oyuncular.items(), key=lambda x: -x[1]["asist"])[:5]
    for i, (isim, veri) in enumerate(sirali, 1):
        print(f"  {i}. {isim:<22} {veri['takim']:<15} {veri['asist']} asist")
    print()


def takim_ozet():
    baslik_yaz("TAKIM ÖZET İSTATİSTİKLERİ")
    for takim, istatistik in sorted(takimlar.items(), key=lambda x: -x[1]["puan"]):
        o = istatistik["galibiyet"] + istatistik["beraberlik"] + istatistik["maglubiyet"]
        print(f"\n  {takim}")
        print(f"     Oynanan: {o} maç  |  Galibiyet: {istatistik['galibiyet']}  |  Beraberlik: {istatistik['beraberlik']}  |  Mağlubiyet: {istatistik['maglubiyet']}")
        print(f"     Attığı gol: {istatistik['gol_atilan']}  |  Yediği gol: {istatistik['gol_yenilen']}  |  Averaj: {istatistik['gol_atilan'] - istatistik['gol_yenilen']:+d}")
    print()


def mac_sonuclari():
    baslik_yaz("MAÇ SONUÇLARI")
    for ev_sahibi, ev_gol, deplasman, dep_gol in maclar:
        print(f"  {ev_sahibi:<15} {ev_gol} - {dep_gol}  {deplasman}")
    print()


def takim_oyuncu_liste():
    baslik_yaz("TAKIMLARA GÖRE OYUNCULAR")
    takim_oyuncu = defaultdict(list)
    for isim, veri in oyuncular.items():
        takim_oyuncu[veri["takim"]].append((isim, veri["gol"], veri["asist"]))
    for takim in sorted(takim_oyuncu.keys()):
        print(f"\n  {takim}")
        for isim, gol, asist in sorted(takim_oyuncu[takim], key=lambda x: -x[1]):
            print(f"     • {isim}  →  {gol} gol, {asist} asist")
    print()


def menu():
    print("\n  [1] Puan durumu")
    print("  [2] Gol krallığı")
    print("  [3] Asist liderleri")
    print("  [4] Takım özet istatistikleri")
    print("  [5] Maç sonuçları")
    print("  [6] Takımlara göre oyuncular")
    print("  [7] Tüm raporu göster")
    print("  [0] Çıkış")
    return input("\n  Seçiminiz (0-7): ").strip()


def tum_rapor():
    puan_durumu()
    gol_krali()
    asist_ligi()
    takim_ozet()
    mac_sonuclari()
    takim_oyuncu_liste()


def main():
    puan_hesapla()
    print("\n")
    baslik_yaz("FUTBOL İSTATİSTİK ANALİZ PROGRAMI")
    print("  Hoş geldiniz! Aşağıdaki menüden analiz türünü seçebilirsiniz.\n")
    while True:
        secim = menu()
        if secim == "1":
            puan_durumu()
        elif secim == "2":
            gol_krali()
        elif secim == "3":
            asist_ligi()
        elif secim == "4":
            takim_ozet()
        elif secim == "5":
            mac_sonuclari()
        elif secim == "6":
            takim_oyuncu_liste()
        elif secim == "7":
            tum_rapor()
        elif secim == "0":
            baslik_yaz("İyi günler!")
            break
        else:
            print("\n  Geçersiz seçim. 0-7 arası bir sayı girin.\n")


if __name__ == "__main__":
    main()
