import pandas as pd
import numpy as np

def main():
    # 600 satırlık veri oluşturacağız
    n_samples = 600
    
    # Aynı sonuçları üretebilmek için seed belirliyoruz
    np.random.seed(42)

    # 1. Sütun: ID (1'den 600'e kadar)
    ids = np.arange(1, n_samples + 1)

    # 2. Sütun: Reklam Gideri (Normal dağılım 5 ile 50 arası)
    # 5 ile 50'nin ortası: 27.5. Standart sapmayı 7.5 seçerek verilerin büyük çoğunluğunun (%99.7)
    # bu aralığa düşmesini sağlıyoruz.
    gider_ortalama = 27.5
    gider_sapma = 7.5
    reklam_gideri = np.random.normal(loc=gider_ortalama, scale=gider_sapma, size=n_samples)
    # Uç değerleri (5'ten küçük veya 50'den büyükleri) sınırlıyoruz
    reklam_gideri = np.clip(reklam_gideri, 5, 50)
    # Virgülden sonra 2 basamak olacak şekilde yuvarlıyoruz
    reklam_gideri = np.round(reklam_gideri, 2)

    # 3. Sütun: Reklam Geliri (Normal dağılım 50 ile 150 arası)
    # 50 ile 150'nin ortası: 100. Standart sapmayı 16.67 (50/3) seçerek verilerin bu aralığa yayılmasını sağlıyoruz.
    gelir_ortalama = 100
    gelir_sapma = 16.67
    reklam_geliri = np.random.normal(loc=gelir_ortalama, scale=gelir_sapma, size=n_samples)
    # Uç değerleri (50'den küçük veya 150'den büyükleri) sınırlıyoruz
    reklam_geliri = np.clip(reklam_geliri, 50, 150)
    # Virgülden sonra 2 basamak olacak şekilde yuvarlıyoruz
    reklam_geliri = np.round(reklam_geliri, 2)

    # Pandas DataFrame'i oluşturuyoruz
    df = pd.DataFrame({
        'ID': ids,
        'Reklam_Gideri': reklam_gideri,
        'Reklam_Geliri': reklam_geliri
    })

    # Veriyi CSV olarak kaydediyoruz
    dosya_adi = 'data.csv'
    df.to_csv(dosya_adi, index=False)
    
    print(f"BAŞARILI: {n_samples} kişilik, normal dağılımlı veri '{dosya_adi}' olarak kaydedildi.")

if __name__ == "__main__":
    main()
