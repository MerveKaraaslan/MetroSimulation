from collections import deque
import heapq

class Istasyon:
    # Istasyon sınıfı: Her bir metro durağını temsil eder
    def __init__(self, isim):
        self.isim = isim
        self.komsular = {}

    def komsu_ekle(self, komsu, sure):
        self.komsular[komsu] = sure

class MetroAgi:
    # MetroAgi sınıfı: Metro ağını oluşturur ve rota bulma işlemlerini yönetir
    def __init__(self):
        self.istasyonlar = {}

    # Yeni bir istasyonu ağa ekler veya var olanı döndürür
    def istasyon_ekle(self, isim):
        if isim not in self.istasyonlar:
            self.istasyonlar[isim] = Istasyon(isim)
        return self.istasyonlar[isim]

    # İki istasyon arasında çift yönlü bağlantı kurar
    def baglanti_ekle(self, baslangic, bitis, sure):
        baslangic_ist = self.istasyon_ekle(baslangic)
        bitis_ist = self.istasyon_ekle(bitis)
        baslangic_ist.komsu_ekle(bitis_ist, sure)
        bitis_ist.komsu_ekle(baslangic_ist, sure)

    # BFS kullanarak en az aktarmalı rotayı bulur
    def en_az_aktarma_bul(self, baslangic, bitis):
        if baslangic not in self.istasyonlar or bitis not in self.istasyonlar:
            return None
        kuyruk = deque([(self.istasyonlar[baslangic], [baslangic])])
        ziyaret_edilen = set([baslangic])
        while kuyruk:
            mevcut_ist, yol = kuyruk.popleft()
            if mevcut_ist.isim == bitis:
                return yol
            for komsu in mevcut_ist.komsular:
                if komsu.isim not in ziyaret_edilen:
                    ziyaret_edilen.add(komsu.isim)
                    yeni_yol = yol + [komsu.isim]
                    kuyruk.append((komsu, yeni_yol))
        return None

    # A* kullanarak en hızlı rotayı ve süresini bulur
    def en_hizli_rota_bul(self, baslangic, bitis):
        if baslangic not in self.istasyonlar or bitis not in self.istasyonlar:
            return None
        oncelik_kuyrugu = [(0, baslangic, [baslangic])]
        heapq.heapify(oncelik_kuyrugu)
        maliyetler = {baslangic: 0}
        while oncelik_kuyrugu:
            toplam_sure, mevcut_isim, yol = heapq.heappop(oncelik_kuyrugu)
            if mevcut_isim == bitis:
                return yol, toplam_sure
            for komsu, sure in self.istasyonlar[mevcut_isim].komsular.items():
                yeni_sure = toplam_sure + sure
                if komsu.isim not in maliyetler or yeni_sure < maliyetler[komsu.isim]:
                    maliyetler[komsu.isim] = yeni_sure
                    yeni_yol = yol + [komsu.isim]
                    heapq.heappush(oncelik_kuyrugu, (yeni_sure, komsu.isim, yeni_yol))
        return None, None

# Test için metro ağı oluşturur ve algoritmaları çalıştırır
if __name__ == "__main__":
    metro = MetroAgi()
    metro.baglanti_ekle("A", "B", 10)
    metro.baglanti_ekle("B", "C", 15)
    metro.baglanti_ekle("A", "D", 20)
    metro.baglanti_ekle("D", "E", 5)
    metro.baglanti_ekle("E", "F", 8)
    metro.baglanti_ekle("B", "F", 25)
    metro.baglanti_ekle("F", "G", 7)
    metro.baglanti_ekle("C", "H", 12)
    metro.baglanti_ekle("G", "H", 10)

    print("A -> H:")
    rota = metro.en_az_aktarma_bul("A", "H")
    print("En az aktarmalı rota:", rota)
    rota, sure = metro.en_hizli_rota_bul("A", "H")
    print("En hızlı rota:", rota, "Süre:", sure)

    print("\nB -> G:")
    rota = metro.en_az_aktarma_bul("B", "G")
    print("En az aktarmalı rota:", rota)
    rota, sure = metro.en_hizli_rota_bul("B", "G")
    print("En hızlı rota:", rota, "Süre:", sure)

    print("\nD -> C:")
    rota = metro.en_az_aktarma_bul("D", "C")
    print("En az aktarmalı rota:", rota)
    rota, sure = metro.en_hizli_rota_bul("D", "C")
    print("En hızlı rota:", rota, "Süre:", sure)