# 🤝 Katkıda Bulunma Rehberi (Contributing Guidelines)

**Diploma-Free Science** ("Görünmez Üniversite") yaşayan, nefes alan bir bilgi havuzudur. Bu yapıyı güçlendirmek sizin elinizde.

## Nasıl Katkı Sağlayabilirsiniz?

### 1. Yeni Kaynak Ekleme
İnternetin derinliklerinde harika bir ücretsiz kurs, PDF veya video serisi mi buldunuz?
- `curriculum/roadmap.json` dosyasına gidin.
- İlgili "Level" ve "Resources" bölümünü bulun.
- Kaynağı ekleyin:
  ```json
  {
    "title": "Kaynağın Adı",
    "url": "https://...",
    "type": "Video/Makale/Kurs"
  }
  ```

### 2. Müfredat Geliştirme
Mevcut yollar (pathways) eksik mi? Yeni bir konu başlığı mı gerekli?
- Bir "Issue" açarak tartışma başlatın.
- Konunun neden gerekli olduğunu ve hangi sıraya ekleneceğini belirtin.

### 3. Kod ve Otomasyon
Repository'nin kalbi olan Python scriptlerini (`src/`) geliştirebilirsiniz.
- Pull Request (PR) göndermeden önce kodunuzu yerel ortamda test edin.
- `src/` içindeki scriptlerin UTF-8 uyumlu olduğundan emin olun.

## Pull Request Süreci

1.  Repoyu "Fork"layın.
2.  Yeni bir "Branch" oluşturun (`git checkout -b feature/YeniKaynak`).
3.  Değişikliklerinizi yapın ve detaylı bir "Commit" mesajı yazın.
4.  PR gönderin ve topluluğun geri bildirimini bekleyin.

---

*"Bilgi paylaştıkça çoğalır, saklandıkça çürür."*
