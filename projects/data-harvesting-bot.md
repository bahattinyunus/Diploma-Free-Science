# 🕷️ Proje: Data Harvesting Bot (Veri Hasadı)

**Zorluk**: 🟡 Orta
**Alan**: Veri Bilimi / Python
**Tahmini Süre**: 1 Hafta

## 🎯 Amaç
Veri, yeni petroldür. Ancak bu petrol kuyuları (sosyal medya, haber siteleri) kilitlidir. Bu projede, kendi Yapay Zeka modelimizi eğitmek için web'den etik sınırlar içinde veri toplayan (scrape) bir bot yazacağız.

## 🧰 Araçlar
1.  **Python**
2.  **BeautifulSoup4**: Statik HTML analizi için.
3.  **Selenium / Playwright**: JavaScript çalıştıran dinamik siteler için.
4.  **SQLite**: Veriyi kaydetmek için.

## 🛠️ Adımlar

### 1. Hedef Belirleme
Hangi veriye ihtiyacınız var?
-   Haber manşetleri? (Duygu analizi için)
-   İkinci el araba fiyatları? (Piyasa tahmini için)
-   Bilimsel makale özetleri? (LLM eğitimi için)

### 2. Robot Etiği (robots.txt)
-   Hedef sitenin `domain.com/robots.txt` dosyasına bakın. "Disallow" (İzin verilmez) denilen yerlere girmeyin.
-   İstekler arasına 2-5 saniye bekleme süresi koyun (`time.sleep()`). Sunucuyu çökertmeyin (DDoS yapmayın).

### 3. Kodlama (Basit Örnek)
```python
import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for item in soup.select('.titleline > a'):
    print(item.text)
```

### 4. Veri Temizleme & Kayıt
-   HTML etiketlerini temizleyin.
-   Veriyi temiz bir CSV veya JSON formatında kaydedin.

## 🚀 Meydan Okuma
-   Botunuzu bir Raspberry Pi üzerinde 7/24 çalışacak şekilde, verileri her gün güncelleyip bir Dashboard'da gösterecek hale getirin (Grafana veya Streamlit).
