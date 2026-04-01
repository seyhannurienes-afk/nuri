import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Veriyi yükle
    try:
        df = pd.read_csv('data.csv')
    except FileNotFoundError:
        print("HATA: data.csv dosyası bulunamadı.")
        return

    # Görselleştirme tarzını belirle (seaborn stili ile daha şık bir görünüm)
    sns.set_theme(style="whitegrid")

    # 1. Her iki değişkenin histogramları (Çan Eğrileri)
    plt.figure(figsize=(14, 6))

    # Reklam Gideri Histogramı
    plt.subplot(1, 2, 1)
    sns.histplot(df['Reklam_Gideri'], bins=30, kde=True, color='skyblue', edgecolor='black')
    plt.title('Reklam Gideri Dağılımı (Çan Eğrisi)', fontsize=14)
    plt.xlabel('Reklam Gideri', fontsize=12)
    plt.ylabel('Frekans', fontsize=12)

    # Reklam Geliri Histogramı
    plt.subplot(1, 2, 2)
    sns.histplot(df['Reklam_Geliri'], bins=30, kde=True, color='lightgreen', edgecolor='black')
    plt.title('Reklam Geliri Dağılımı (Çan Eğrisi)', fontsize=14)
    plt.xlabel('Reklam Geliri', fontsize=12)
    plt.ylabel('Frekans', fontsize=12)

    plt.tight_layout()
    plt.savefig('dagilimlar.png', dpi=300)
    print("KAYDEDİLDİ: 'dagilimlar.png'")

    # 2. Reklam Gideri vs Reklam Geliri (Scatter Plot)
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x='Reklam_Gideri', y='Reklam_Geliri', alpha=0.7, color='coral', edgecolor='black')
    
    # Ortalama değerleri gösteren çizgiler ekleyelim
    plt.axvline(df['Reklam_Gideri'].mean(), color='blue', linestyle='--', label='Ort. Gider')
    plt.axhline(df['Reklam_Geliri'].mean(), color='red', linestyle='--', label='Ort. Gelir')
    
    plt.title('Reklam Gideri ve Geliri İlişkisi', fontsize=14)
    plt.xlabel('Reklam Gideri', fontsize=12)
    plt.ylabel('Reklam Geliri', fontsize=12)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig('iliskisel_dagilim.png', dpi=300)
    print("KAYDEDİLDİ: 'iliskisel_dagilim.png'")

if __name__ == "__main__":
    main()
