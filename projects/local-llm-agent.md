# 🤖 Proje: Yerel LLM Ajanı (Local LLM Agent)

**Zorluk**: 🟡 Orta
**Alan**: Yapay Zeka / Veri Bilimi
**Tahmini Süre**: 2 Hafta Sonu

## 🎯 Amaç
OpenAI veya Google'a veri göndermeden, tamamen kendi bilgisayarınızda çalışan, sizin pdf/markdown notlarınızla konuşabilen (RAG - Retrieval Augmented Generation) özel bir yapay zeka asistanı kurmak. "Gizlilik" odaklı bir araştırma asistanı.

## 🧰 Gereksinimler
1.  **Donanım**: En az 8GB RAM (16GB önerilir). NVIDIA GPU (4GB+ VRAM) büyük hız katar ama CPU ile de (yavaş) çalışır.
2.  **Yazılım**: Python, Docker (opsiyonel), Ollama.

## 🛠️ Adımlar

### 1. Ollama Kurulumu
`Ollama`, yerel modelleri çalıştırmanın en kolay yoludur.
-   [Ollama.ai](https://ollama.ai) adresinden indirin.
-   Terminalde `ollama run llama3` (veya `mistral`) yazarak modeli indirin ve konuşmaya başlayın.

### 2. Doküman Hazırlığı
-   Okumak istediğiniz PDF makaleleri veya Obsidian notlarınızı bir klasöre toplayın.
-   Python ile bu metinleri okuyup "küçük parçalara" (chunks) bölün.

### 3. Vektör Veritabanı (Embeddings)
-   `Chromadb` veya `FAISS` kullanarak metin parçalarını vektörlere dönüştürün ve kaydedin. (Burada `sentence-transformers` kütüphanesi kullanılır).

### 4. RAG Boru Hattı (Pipeline)
-   Kullanıcı sorusunu vektöre çevir -> Veritabanında en yakın metin parçalarını bul -> Bu parçaları LLM'e "bağlam" (context) olarak ver -> Cevabı üret.
-   `LangChain` veya basit Python scriptleri ile bu akışı kodlayın.

### 5. Arayüz (UI)
-   `Streamlit` veya `Chainlit` kullanarak tarayıcı üzerinden çalışan şık bir sohbet arayüzü yapın.

## 🚀 Meydan Okuma
-   Ajana "internet erişimi" verin (Google Search API kullanarak güncel olayları araştırabilsin).
-   Ajana "kod çalıştırma" yeteneği verin (Birlikte Python scripti yazıp debug edin).
