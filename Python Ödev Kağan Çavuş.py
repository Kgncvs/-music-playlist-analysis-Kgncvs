# Toplam Süre
def toplam_sure_hesapla(sarkilar):
    toplam = 0
    # Listedeki her bir şarkıyı tek tek geziyer
    for sarki in sarkilar:
        # Şarkının süresini (saniye) toplama ekler
        toplam = toplam + sarki["sure"]
    return toplam

#  En Çok Dinlenen Şarkı 
def en_cok_dinlenen_sarkiyi_bul(sarkilar):
    en_cok_dinlenen = sarkilar[0] 
    
    # Tüm şarkıları tek tek kontrol eder
    for sarki in sarkilar:
        # Eğer sıradaki şarkı, elindeki 'en_cok_dinlenen'den daha çok dinlenmişse:
        if sarki["dinlenme_sayisi"] > en_cok_dinlenen["dinlenme_sayisi"]:
            # Artık yeni en cok dinlenen sarkidır 
            en_cok_dinlenen = sarki 
            
    return en_cok_dinlenen

# Ortalama Süre
def ortalama_sure_hesapla(sarkilar):
    # Eğer liste boşsa hata almamak için kontrol eder
    if len(sarkilar) == 0:
        return 0
        
    toplam_sure = toplam_sure_hesapla(sarkilar)
    ortalama = toplam_sure / len(sarkilar)
    return ortalama

# 4. Listeyi Ekrana Yazdırma
def calma_listesini_yazdir(sarkilar):
    print("\n--- Çalma Listesi ---")
    for sarki in sarkilar:
        # Her şarkının bilgilerini basitçe yan yana yazdırır
        print(f"Şarkı: {sarki['sarki_adi']} | Sanatçı: {sarki['sanatci']} | Dinlenme: {sarki['dinlenme_sayisi']}")
    print("---------------------\n")


# En Uzun Şarkı 
def en_uzun_sarkiyi_bul(sarkilar):
    en_uzun = sarkilar[0]
    for sarki in sarkilar:
        if sarki["sure"] > en_uzun["sure"]:
            en_uzun = sarki
    return en_uzun

#  Sanatçıya Göre Filtreleme
def sanatciya_gore_filtrele(sarkilar, aranan_sanatci):
    # Filtrelenen şarkıları koymak için boş bir liste açar
    filtrelenmis_liste = []
    
    for sarki in sarkilar:
        # Eğer şarkının sanatçısı, aradığımız sanatçıya eşitse
        if sarki["sanatci"] == aranan_sanatci:
            # Şarkıyı yeni listeye ekle
            filtrelenmis_liste.append(sarki)
            
    return filtrelenmis_liste

#  Dinlenmeye Göre Sıralama için yardımcı fonksiyon
def dinlenme_sayisini_al(sarki):
    return sarki["dinlenme_sayisi"]

def dinlenme_sayisina_gore_sirala(sarkilar):
    # Orijinal listeyi bozmamak için listenin kopyasını alır
    sirali_sarkilar = list(sarkilar) 
    # Listeyi sıralar. reverse=True diyerek çoktan aza (büyükten küçüğe) olmasını sağlar
    sirali_sarkilar.sort(key=dinlenme_sayisini_al, reverse=True)
    return sirali_sarkilar


#  Ana Fonksiyon 
def main():
    # İçinde sözlükler olan basit bir liste 
    calma_listesi = [
        {"sarki_adi": "Sarki 1", "sanatci": "Sanatci 1", "sure": 220, "dinlenme_sayisi": 1200000},
        {"sarki_adi": "Sarki 2", "sanatci": "Sanatci 2", "sure": 233, "dinlenme_sayisi": 3400000},
        {"sarki_adi": "Sarki 3", "sanatci": "Sanatci 3", "sure": 200, "dinlenme_sayisi": 3800000},
        {"sarki_adi": "Sarki 4", "sanatci": "Sanatci 4", "sure": 390, "dinlenme_sayisi": 1200000},
        {"sarki_adi": "Sarki 5", "sanatci": "Sanatci 5", "sure": 230, "dinlenme_sayisi": 2100000}
    ]

    print(" MÜZİK SİSTEMİ BAŞLIYOR")

    # Methodları tek tek çağırıp sonuçları ekrana basıyoruz
    calma_listesini_yazdir(calma_listesi)

    toplam = toplam_sure_hesapla(calma_listesi)
    print(f"Toplam Süre: {toplam} saniye")

    ortalama = ortalama_sure_hesapla(calma_listesi)
    print(f"Ortalama Süre: {ortalama} saniye")

    en_cok_dinlenen = en_cok_dinlenen_sarkiyi_bul(calma_listesi)
    print(f"En Çok Dinlenen: {en_cok_dinlenen['sarki_adi']}")
    
    en_uzun_sarki = en_uzun_sarkiyi_bul(calma_listesi)
    print(f"En Uzun Şarkı: {en_uzun_sarki['sarki_adi']}")
    
    print("\nSadece 'Sanatci 3' Şarkıları:")
    sanatci_3_sarkilari = sanatciya_gore_filtrele(calma_listesi, "Sanatci 3")
    calma_listesini_yazdir(sanatci_3_sarkilari)

main()