# 📡 Proje: SDR Radyo Tarayıcı (SDR Hacking)

**Zorluk**: 🟢 Kolay / 🟡 Orta
**Alan**: Fizik / Elektronik / Haberleşme
**Tahmini Süre**: 1 Gün

## 🎯 Amaç
Çevremiz, gözle görmediğimiz radyo dalgalarıyla (RF) doludur. Uçaklar, polis telsizleri, hava durumu uyduları, araba anahtarları... Ucuz bir USB dongle (RTL-SDR) kullanarak bu görünmez dünyayı "duyacağız" ve analiz edeceğiz.

## 🧰 Donanım
1.  **RTL-SDR Dongle V3**: Yaklaşık $30-40. (Realtek RTL2832U çipli herhangi bir TV alıcısı da olur ama V3 en iyisidir).
2.  **Anten**: Genelde dongle ile gelir (Teleskopik anten).
3.  **Bilgisayar**: Linux veya Windows yüklü herhangi bir PC.

## 🛠️ Adımlar

### 1. Yazılım Kurulumu (SDR# veya GQRX)
-   Windows için **SDR# (SDR Sharp)** en iyisidir.
-   Linux için **GQRX** veya **SDR++** kullanın.
-   Sürücüleri (Zadig ile) doğru yüklediğinizden emin olun.

### 2. FM Radyo Dinleme (Test)
-   Frekansı 88.0 MHz - 108.0 MHz arasına getirin.
-   Modülasyonu "WFM" (Wide FM) yapın.
-   Müzik duyuyorsanız cihaz çalışıyor demektir.

### 3. Hava Trafiği (ATC) Dinleme
-   Frekansı 118.0 MHz - 136.0 MHz arasına getirin (AM Modülasyonu).
-   Yakınızdaki havalimanının "Tower" veya "Approach" frekansını internetten bulun.
-   Pilotların kuleyle konuşmalarını dinleyin.

### 4. Dijital Sinyal Analizi (Araba Anahtarı)
-   Frekansı 433.92 MHz'e (ISM Bandı) getirin.
-   Araba anahtarınıza basın. Şelale ekranında (Waterfall) ani bir sıçrama göreceksiniz.
-   **Universal Radio Hacker (URH)** yazılımı ile bu sinyali kaydedip "replay" (tekrar oynatma) saldırılarını analiz edebilirsiniz. (⚠️ Kendi arabanızda deneyin!)

## 🚀 Meydan Okuma (NOAA Uyduları)
-   Başınızın üzerinden geçen NOAA hava durumu uydularından (137 MHz) canlı görüntü indirin. (Bunun için "V-Dipole" anten yapmanız gerekebilir).
