# 1. KISIM: Veri Yapıları ve Temel Mantık (Hafta 1)

import random

abone_isim = "abdullah sancak"
aylik_sabit_ucret = 599.99
sadakat_suresi_ay = 34
abonelik_aktif_mi = True

telco_hizmet_katalogu = ["Mobil Data", "Evde Fiber", "IPTV", "Bulut Depolama", "SMS Paketi"]

abone_profil_sozluk = {
    "isim_soyisim": abone_isim,
    "aylik_ucret": aylik_sabit_ucret,
    "sadakat_ayi": sadakat_suresi_ay,
    "aktiflik_durumu": abonelik_aktif_mi
}

if abone_profil_sozluk["aylik_ucret"] > 500 or abone_profil_sozluk["sadakat_ayi"] > 24:
    print("Müşteri Segmenti: [VIP Müşteri] -> İndirim Tanımla")
else:
    print("Müşteri Segmenti: [Standart Müşteri]")

abone_profil_sozluk["isim_soyisim"] = abone_profil_sozluk["isim_soyisim"].upper()

rastgele_kod = random.randint(10000, 99999)
customerID = f"IST-2026-{rastgele_kod}"

print("-" * 40)
print(f"Müşteri ID: {customerID}")
print(f"Abone Adı: {abone_profil_sozluk['isim_soyisim']}")
print("-" * 40)


# 2. KISIM: Fonksiyonlar, Döngüler ve Kütüphaneler (Hafta 2)



import math  # Kütüphane Kullanımı
from datetime import datetime  # Kütüphane Kullanımı

# Veri Yapıları / Liste ve Sözlük Kullanımı
abone_havuzu = [
    {"ad": "Emir Sancak", "ucret": 450.0, "sadakat": 5, "aktif": True},
    {"ad": "Mert Toptaş", "ucret": 640.0, "sadakat": 30, "aktif": False},
    {"ad": "Mustafa Karga", "ucret": 370.0, "sadakat": 2, "aktif": True},
    {"ad": "Mehmet Şahbal", "ucret": 750.0, "sadakat": 12, "aktif": True},
    {"ad": "Hasan Artuk", "ucret": 180.0, "sadakat": 1, "aktif": True}
]

# Fonksiyon Tanımlama
def tutar_hesapla(aylik_ucret):
    toplam_tutar = aylik_ucret * 1.20  # Matematiksel Operatörler
    return toplam_tutar  # Fonksiyon Geri Dönüş Değeri

# Hata Denetimi ve Set Kullanımı
try:
    ham_hizmet_listesi = ["Mobil Data", "Evde Fiber", "Mobil Data", "IPTV", "SMS Paketi", "IPTV"]
    benzersiz_hizmetler = set(ham_hizmet_listesi)  # Set (Küme) Kullanımı
    print(f"Benzersiz Hizmetler: {benzersiz_hizmetler}\n")
except Exception as e:  # Hata Denetimi (Try-Except)
    print(f"Hata oluştu: {e}")

print("=== MÜŞTERİ ANALİZ RAPORU ===")

# Döngü Kullanımı
for abone in abone_havuzu:
    ham_fatura = tutar_hesapla(abone["ucret"])  # Fonksiyon Çağrısı
    kesinlesecek_fatura = math.ceil(ham_fatura)  # Kütüphane Kullanımı (Yukarı yuvarlama)

    # Koşullu İfadeler (If-Elif-Else)
    if not abone["aktif"]:
        churn_durumu = "Churn (Ayrılmış)"
    elif abone["sadakat"] <= 3:
        churn_durumu = "Yüksek Churn Riski (Yeni Abone)"
    else:
        churn_durumu = "Standart / Sadık"

    print(f"Müşteri: {abone['ad']} | Fatura: {kesinlesecek_fatura} TL | Durum: {churn_durumu}")

bugun = datetime.now().strftime("%d/%m/%Y")  # Kütüphane Kullanımı (Zaman yönetimi)
print("-" * 50)
print(f"Fatura Tarihi: {bugun}")
print("-" * 50)
