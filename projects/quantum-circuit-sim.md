# ⚛️ Proje: Kuantum Devre Simülatörü

**Zorluk**: 🔴 Zor
**Alan**: Fizik / Bilgisayar Bilimi
**Tahmini Süre**: 2-3 Hafta

## 🎯 Amaç
Kuantum bilgisayarlarının nasıl çalıştığını anlamanın en iyi yolu, bir tane inşa etmektir (yazılımsal olarak). Bu projede, karmaşık kütüphaneler (Qiskit vb.) *kullanmadan*, saf Python ve Numpy ile kendi kuantum simülatörümüzü yazacağız.

## 🧰 Teori
Simülatörünüz şunları desteklemelidir:
1.  **State Vector (Durum Vektörü)**: Qubitlerin durumunu temsil eden kompleks sayı vektörleri.
2.  **Quantum Gates (Mantık Kapıları)**: Bu vektörleri değiştiren matrisler.
    -   Pauli-X (NOT Kapısı)
    -   Hadamard (Süperpozisyon yaratır)
    -   CNOT (Dolanıklık yaratır)

## 🛠️ Adımlar

### 1. Tek Qubit
-   Bir qubiti [1, 0] veya [0, 1] vektörü olarak tanımlayın.
-   Hadamard matrisi ile çarpıp süperpozisyona sokun.

### 2. Çoklu Qubitler (Tensor Product)
-   İki qubitin durumu, tek tek vektörlerin değil, onların **Tensör Çarpımı (Kronecker Product)** sonucudur.
-   `numpy.kron()` fonksiyonunu kullanın.

### 3. Ölçüm (Measurement)
-   Kuantum durumu (örneğin %50 |0> + %50 |1>) ölçüldüğünde çöker.
-   Olasılık genliklerinin karesini alarak rastgele bir sonuç (0 veya 1) döndüren fonksiyon yazın.

### 4. Algoritma Testi
-   Kendi simülatörünüzde **Bell Durumu** (Dolanıklık) oluşturun.
-   Grover'ın Arama Algoritmasını (küçük ölçekte) çalıştırın.

## 🚀 Meydan Okuma
-   Simülatörünüze bir arayüz ekleyin (sürükle-bırak kapılar).
-   Simülatörü C++ ile yeniden yazarak hızlandırın.
