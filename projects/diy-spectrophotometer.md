# 🧪 Proje: DIY Spektrofotometre

**Zorluk**: 🟢 Kolay
**Alan**: Fizik / Biyoloji / Elektronik
**Tahmini Süre**: 1 Hafta Sonu

## 🎯 Amaç
Profesyonel laboratuvar spektrofotometreleri binlerce dolar tutabilir. Beer-Lambert yasasını kullanarak, numunenin ışığı ne kadar soğurduğunu ölçen 20 dolarlık bir cihaz yapacağız. Bu cihazla bakteri kültürlerinin büyümesini (OD600) takip edebilirsiniz.

## 🧰 Malzemeler
1.  **Arduino Uno** (veya klonu)
2.  **Breadboard & Jumper Kablolar**
3.  **LED** (Belirli dalga boyunda, örn. 600nm turuncu/kırmızı)
4.  **LDR (Işığa Duyarlı Direnç)** veya **Fotodiyot**
5.  **Dirençler** (220Ω ve 10kΩ)
6.  **Küvet** (Numune kabı - şeffaf plastik kare kaplar) veya şeffaf lego parçaları.
7.  **Siyah Kutu** (Işık sızdırmazlık için - karton kutu + siyah bant).

## 🛠️ Adımlar

### 1. Devre Kurulumu
-   LED'i bir dijital pine bağlayın (Direnç kullanmayı unutmayın!).
-   LDR'yi analog pine bağlayın (Voltaj bölücü devre kurarak).
-   LED ve LDR birbirine tam karşıdan bakmalı. Aralarına küvet girecek kadar boşluk bırakın.

### 2. Kalibrasyon (Boş Küvet)
-   Arada sadece su dolu küvet varken sensörden okunan değeri kaydedin (`I_0`). Bu sizin referans ışık şiddetinizdir.

### 3. Ölçüm (Numune)
-   Renkli veya bulanık numuneyi koyun. Değeri okuyun (`I`).

### 4. Matematik (Beer-Lambert Yasası)
Absorbans (A) değerini hesaplayın:
$$ A = \log_{10} \left( \frac{I_0}{I} \right) $$

### 5. Yazılım
Arduino kodu ile seri porttan veriyi okuyun ve Python (Matplotlib) ile gerçek zamanlı grafik çizin.

## 🚀 Meydan Okuma
-   Cihazı 3D yazıcı ile basılmış bir kutuya koyun.
-   LCD ekran ekleyerek bilgisayarsız çalışmasını sağlayın.
