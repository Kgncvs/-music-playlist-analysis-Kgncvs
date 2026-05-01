# Müzik Çalma Listesi Analiz Sistemi

## Proje Amacı
Bu proje, Python'a giriş seviyesinde temel veri yapıları (listeler ve sözlükler) ve döngüler kullanılarak geliştirilmiş bir veri analizi uygulamasıdır. İçerisinde şarkı bilgilerini barındıran bir veri setinin işlenmesi, filtrelenmesi ve matematiksel hesaplamalarının yapılması amaçlanmıştır.

## Metot Açıklamaları
Proje içerisinde aşağıdaki fonksiyonlar aktif olarak kullanılmıştır:

* **`toplam_sure_hesapla(sarkilar)`:** Listede bulunan tüm şarkıların sürelerini saniye cinsinden toplar.
* **`en_cok_dinlenen_sarkiyi_bul(sarkilar)`:** Dinlenme sayısına göre en popüler şarkıyı tespit eder.
* **`ortalama_sure_hesapla(sarkilar)`:** Çalma listesinin ortalama şarkı süresini hesaplar.
* **`calma_listesini_yazdir(sarkilar)`:** Verileri ekranda düzenli ve okunabilir bir formatta listeler.
* **`en_uzun_sarkiyi_bul(sarkilar)` :** Süre bakımından en uzun şarkıyı bulur.
* **`sanatciya_gore_filtrele(sarkilar, aranan_sanatci)`:** Sadece istenilen sanatçıya ait şarkıları filtreleyerek yeni bir liste oluşturur.
* **`dinlenme_sayisina_gore_sirala(sarkilar)` :** Şarkıları dinlenme sayısına göre büyükten küçüğe doğru sıralar.

## Çalıştırma Bilgisi
Projeyi kendi bilgisayarınızda çalıştırmak için terminal (veya komut istemcisi) ekranında dosyanın bulunduğu dizine giderek aşağıdaki komutu çalıştırmanız yeterlidir:
```bash
