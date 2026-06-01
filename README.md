# Akıllı Müşteri Yönetim ve Analiz Sistemi (Telco Senaryosu)

## Proje Hakkında

Bu proje, Python Programlama dersi dönem ödevi kapsamında Google Colab ortamında geliştirilmiştir.

Projenin amacı, telekomünikasyon sektöründeki müşterilerin abonelik verilerini Python programlama dili kullanarak analiz etmek, müşteri segmentasyonu yapmak ve müşteri kaybı (Churn) risklerini belirlemektir.

Proje kapsamında veri yapıları, fonksiyonlar, döngüler, kütüphane kullanımı, hata yönetimi ve temel veri analizi konuları uygulanmıştır.

## Kullanılan Teknolojiler

* Google Colab
* random kütüphanesi
* math kütüphanesi
* datetime kütüphanesi

## 1. Kısım: Veri Yapıları ve Temel Mantık

Bu bölümde:

* Müşteriye ait temel bilgiler değişkenler ile tanımlanmıştır.
* Şirket hizmetleri liste (List) yapısında tutulmuştur.
* Müşteri bilgileri sözlük (Dictionary) yapısında saklanmıştır.
* If-Else yapıları kullanılarak müşteri segmentasyonu yapılmıştır.
* VIP müşteri kontrolü gerçekleştirilmiştir.
* String işlemleri kullanılarak müşteri adı büyük harfe çevrilmiştir.
* Random kütüphanesi ile benzersiz müşteri kimliği (Customer ID) üretilmiştir.

### VIP Müşteri Kriterleri

Aşağıdaki koşullardan en az biri sağlanıyorsa müşteri VIP olarak değerlendirilmiştir:

* Aylık ücret 500 TL'den büyükse
* Sadakat süresi 24 aydan uzunsa

## 2. Kısım: Fonksiyonlar, Döngüler ve Kütüphaneler

Bu bölümde:

* Birden fazla müşteriden oluşan müşteri listesi oluşturulmuştur.
* Fonksiyon kullanılarak KDV dahil fatura hesaplanmıştır.
* For döngüsü ile müşteri kayıtları analiz edilmiştir.
* Math kütüphanesi kullanılarak tutarlar yukarı yuvarlanmıştır.
* Datetime kütüphanesi kullanılarak rapor tarihi oluşturulmuştur.
* Set veri yapısı kullanılarak benzersiz hizmet listesi elde edilmiştir.
* Churn (müşteri kaybı) risk analizi gerçekleştirilmiştir.

## Projede Kullanılan Veri Yapıları

* String
* Integer
* Float
* Boolean
* List
* Dictionary
* Set

## Kritik Soru 1

### Müşteri bilgilerini neden bir Liste yerine Sözlük içinde saklamayı tercih ettik? Avantajı nedir?

Listeler sıralı veriler için son derece kullanışlıdır ancak elemanlara sadece tam sayı indeksleri (0, 1, 2...) üzerinden erişim imkanı tanırlar. Gerçek zamanlı ve geniş ölçekli projelerde, abonenin adının veya fatura tutarının hangi indekste tutulduğunu akılda tutmak oldukça zordur. Bu durum kodun okunabilirliğini ve bakımını ciddi oranda zorlaştırır.

#### Sözlük (Dictionary) Kullanmanın Sağladığı Avantajlar

**Anlamsal İlişkilendirme (Key-Value Yapısı)**

Verilere indeks numaraları yerine "aylik_ucret", "sadakat_ayi" veya "isim_soyisim" gibi anlamlı anahtarlar ile erişilir. Bu sayede kod daha okunabilir ve anlaşılır hale gelir.

**Zaman Karmaşıklığı ve Performans**

Python sözlükleri arka planda Hash Table yapısını kullanır. Bu nedenle bir anahtara erişim ortalama olarak O(1) zaman karmaşıklığı ile gerçekleşir. Veri seti büyüse bile erişim süresi büyük ölçüde sabit kalır. Listelerde ise belirli bir veriyi bulmak için O(n) zaman karmaşıklığında arama yapılması gerekebilir. Bu nedenle müşteri kayıtlarının yönetiminde sözlük kullanımı daha verimli ve profesyonel bir çözümdür.

## Kritik Soru 2

### Yazdığınız döngü müşteri listesini gezerken hangi müşterilerin Churn (ayrılma) riskinde olduğunu nasıl tespit ettiniz? Mantığınızı açıklayın.

Geliştirilen döngü yapısı içerisinde müşteri kayıplarını önlemek ve tahmin etmek amacıyla telekomünikasyon sektöründe sıklıkla kullanılan iki aşamalı bir risk analizi mantığı uygulanmıştır.

### 1. Mevcut İlişik Kesme Kontrolü (Doğrudan Churn)

Döngü sırasında müşterinin "aktif" değeri kontrol edilir.

* Eğer değer False ise müşteri artık hizmet almıyor demektir.
* Bu durumda müşteri doğrudan "Churn (Ayrılmış)" olarak sınıflandırılır.

Mevcut veri setinde Mert Toptaş bu grupta yer almaktadır.

### 2. Zamana Dayalı Erken Evre Risk Analizi (Potansiyel Churn)

Telekomünikasyon sektöründe yeni müşterilerin ilk 90 günü (3 ay) ayrılma riskinin en yüksek olduğu dönemlerden biridir.

Bu nedenle:

* Müşteri aktif ise,
* Ancak sadakat süresi 3 ay veya daha düşük ise,

müşteri "Yüksek Churn Riski" grubuna alınmıştır.

Mevcut veri setinde:

* Mustafa Karga (2 ay)
* Hasan Artuk (1 ay)

henüz ayrılmamış olmalarına rağmen yüksek riskli müşteri olarak tespit edilmiştir.

Bu yaklaşım sayesinde hem ayrılmış müşteriler hem de gelecekte ayrılma ihtimali yüksek müşteriler belirlenebilmektedir.

## Çalıştırma

1. Google Colab ortamında notebook dosyasını açın.
2. Hücreleri sırasıyla çalıştırın.
3. Program müşteri analiz raporunu ve churn değerlendirmelerini ekrana yazdıracaktır.

## Dosyalar

* Python Dönem Ödevi Notebook Dosyası (.ipynb)
* README.md

## Geliştirici

Abdullah Sancak

## Ders Bilgisi

Python Programlama Dönem Ödevi

2025-2026 Eğitim Öğretim Yılı
