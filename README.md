# Ankara Akıllı Rota Uygulaması

## Proje Hakkında
Bu uygulama, Ankara'nın ilçeleri arasında akıllı rota planlaması yapan, yakıt tüketimini hesaplayan ve görsel bir harita üzerinde rotayı gösteren bir masaüstü uygulamasıdır. Kullanıcılar farklı araç tipleri ve yakıt türleri seçerek en uygun rotayı belirleyebilirler.

## Özellikler
- Ankara'nın tüm ilçeleri arasında rota planlaması
- Farklı araç tiplerine göre yakıt tüketimi hesaplama
- İnteraktif harita görüntüleme
- Mesafe ve süre hesaplama
- Kullanıcı dostu arayüz
- Gerçek zamanlı rota çizimi

## Teknolojiler ve OOP Kavramları
### Kullanılan Teknolojiler
- Python 3.x
- Tkinter (GUI)
- OpenRouteService API
- Folium (Harita görselleştirme)
- PIL (Python Imaging Library)

### OOP Prensipleri
- **Kapsülleme**: Veri ve metodların organize edilmesi
- **Sınıf Yapısı**: GUI elemanları ve veri yapıları
- **Modüler Tasarım**: Arayüz ve iş mantığının ayrılması

### Veri Yapıları
- Dictionary (İlçe koordinatları ve yakıt tüketimi verileri)
- Lists (Araç ve yakıt seçenekleri)
- JSON (API yanıtları)

## Kurulum
```bash
# Repository'yi klonlayın
git clone [repository-url]
cd ankara-rota-uygulamasi

# Gerekli kütüphaneleri yükleyin
pip install tkinter
pip install openrouteservice
pip install folium
pip install Pillow
```

## Kullanım
1. Uygulamayı başlatın:
```bash
python main.py
```
2. Başlangıç ve bitiş ilçelerini seçin
3. Araç tipini seçin (Sedan, SUV, Hatchback)
4. Yakıt türünü seçin (Benzin, Dizel, LPG, Elektrik)
5. "Rotayı Hesapla" butonuna tıklayın
6. Harita otomatik olarak açılacak ve rota görüntülenecektir

## Proje Yapısı
```
├── main.py             
├── rota_haritasi.html         
          

```

## API Kullanımı
Uygulama, OpenRouteService API'sini kullanmaktadır. API anahtarınızı `main.py` dosyasında güncelleyin:
```python
client = openrouteservice.Client(key='YOUR_API_KEY')
```

## Lisans
Bu proje MIT lisansı altında lisanslanmıştır.
