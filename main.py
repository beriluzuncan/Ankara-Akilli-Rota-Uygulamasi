import tkinter as tk
from tkinter import messagebox
import openrouteservice
import folium
import webbrowser
from PIL import Image, ImageTk  # Arka plan resmi için

# OpenRouteService API anahtarı
client = openrouteservice.Client(key='5b3ce3597851110001cf624853e8fb08ee1041e49e20f933561c2ad4')

# İlçe koordinatları
ilce_koordinatlari = {
    "Akyurt": (33.0865, 40.1286),
    "Altındağ": (32.8597, 39.9417),
    "Ayaş": (32.3442, 40.0139),
    "Bala": (33.1203, 39.5483),
    "Beypazarı": (31.9216, 40.1679),
    "Çamlıdere": (32.4722, 40.4944),
    "Çankaya": (32.8597, 39.9208),
    "Çubuk": (33.0333, 40.2381),
    "Elmadağ": (33.2297, 39.9208),
    "Etimesgut": (32.6833, 39.9615),
    "Gölbaşı": (32.8048, 39.7975),
    "Güdül": (32.2047, 40.2103),
    "Haymana": (32.4958, 39.4258),
    "Kahramankazan": (32.6833, 40.2311),
    "Kalecik": (33.4089, 40.0972),
    "Keçiören": (32.8663, 39.9602),
    "Kızılcahamam": (32.6500, 40.4697),
    "Mamak": (32.8998, 39.9208),
    "Nallıhan": (31.3522, 40.1872),
    "Polatlı": (32.1458, 39.5778),
    "Pursaklar": (32.8889, 40.0183),
    "Şereflikoçhisar": (33.5389, 38.9389),
    "Sincan": (32.5833, 39.9667),
    "Yenimahalle": (32.8093, 39.9615)
}

# Araç ve yakıt seçenekleri
arac_secenekleri = ["Sedan", "SUV", "Hatchback"]
yakit_secenekleri = ["Benzin", "Dizel", "LPG", "Elektrik"]

# Yakıt tüketimi hesaplama (araba türüne göre)
yakıt_tüketimi = {
    "Sedan": 7,  # L/100km
    "SUV": 10,
    "Hatchback": 6
}

# Tkinter GUI
root = tk.Tk()
root.title("Akıllı Rota Uygulaması")
root.geometry("620x500")  

# Arka plan resmi ekleme
canvas = tk.Canvas(root, width=800, height=800)
canvas.pack(fill="both", expand=True)
bg_image = ImageTk.PhotoImage(Image.open("C:/Users/beril/Downloads/istockphoto-1151367251-612x612.jpg"))
canvas.create_image(0, 0, image=bg_image, anchor="nw")

# Başlangıç mesajı
giris_mesaji = canvas.create_text(300, 50, text="Akıllı Rota Uygulamasına Hoşgeldiniz", font=("Poppins,", 20, "bold"), fill="#002b5b")


# İlçe seçimleri
ilce_bir_label = tk.Label(root, text="Başlangıç İlçesi:", font=("Poppins", 12), bg="#002b5b", fg="white")
canvas.create_window(200, 100, window=ilce_bir_label)

ilce_bir_combobox = tk.StringVar()
ilce_bir_combobox.set("Seçiniz")
ilce_bir_menu = tk.OptionMenu(root, ilce_bir_combobox, *ilce_koordinatlari.keys())
canvas.create_window(400, 100, window=ilce_bir_menu)

ilce_iki_label = tk.Label(root, text="Bitiş İlçesi:", font=("Poppins", 12), bg="#002b5b", fg="white")
canvas.create_window(200, 150, window=ilce_iki_label)

ilce_iki_combobox = tk.StringVar()
ilce_iki_combobox.set("Seçiniz")
ilce_iki_menu = tk.OptionMenu(root, ilce_iki_combobox, *ilce_koordinatlari.keys())
canvas.create_window(400, 150, window=ilce_iki_menu)

# Araç ve yakıt seçenekleri
arac_label = tk.Label(root, text="Araç Tipi Seçin:", font=("Poppins", 12), bg="#002b5b", fg="white")
canvas.create_window(200, 200, window=arac_label)

arac_combobox = tk.StringVar()
arac_combobox.set("Seçiniz")
arac_menu = tk.OptionMenu(root, arac_combobox, *arac_secenekleri)
canvas.create_window(400, 200, window=arac_menu)

yakit_label = tk.Label(root, text="Yakıt Türü Seçin:", font=("Poppins", 12), bg="#002b5b", fg="white")
canvas.create_window(200, 250, window=yakit_label)

yakit_combobox = tk.StringVar()
yakit_combobox.set("Seçiniz")
yakit_menu = tk.OptionMenu(root, yakit_combobox, *yakit_secenekleri)
canvas.create_window(400, 250, window=yakit_menu)

# Sonuçları göstermek için label
sonuc_label = tk.Label(root, text="", font=("Poppins", 12), bg="#002b5b", fg="white", justify="left", wraplength=600)
canvas.create_window(300, 450, window=sonuc_label)

# Rota hesaplama butonu
def rota_hesapla():
    try:
        baslangic_ilcesi = ilce_bir_combobox.get()
        bitis_ilcesi = ilce_iki_combobox.get()
        
        if baslangic_ilcesi == bitis_ilcesi:
            messagebox.showerror("Hata", "Başlangıç ve bitiş ilçesi aynı olamaz.")
            return
        
        start = ilce_koordinatlari[baslangic_ilcesi]
        end = ilce_koordinatlari[bitis_ilcesi]
        
        route = client.directions(coordinates=[start, end], profile='driving-car', format='geojson')
        distance = route['features'][0]['properties']['segments'][0]['distance'] / 1000  # km
        duration = route['features'][0]['properties']['segments'][0]['duration'] / 60  # dakika
        
        arac_tipi = arac_combobox.get()
        yakit_tuketimi_orani = yakıt_tüketimi[arac_tipi]
        yakit_tuketimi = (distance * yakit_tuketimi_orani) / 100
        
        m = folium.Map(location=[(start[1] + end[1]) / 2, (start[0] + end[0]) / 2], zoom_start=12)
        folium.Marker(location=start, popup=f"Başlangıç: {baslangic_ilcesi}", icon=folium.Icon(color="green")).add_to(m)
        folium.Marker(location=end, popup=f"Bitiş: {bitis_ilcesi}", icon=folium.Icon(color="red")).add_to(m)
        route_coords = [(coord[1], coord[0]) for coord in route['features'][0]['geometry']['coordinates']]
        folium.PolyLine(locations=route_coords, color="blue", weight=2.5, opacity=1).add_to(m)
        m.save("rota_haritasi.html")
        webbrowser.open("rota_haritasi.html")
        
        sonuc_label.config(text=f"Mesafe: {distance:.2f} km\nTahmini Süre: {duration:.2f} dakika\nYakıt Tüketimi: {yakit_tuketimi:.2f} L")
    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {e}")

hesapla_button = tk.Button(root, text="Rotayı Hesapla", command=rota_hesapla, bg="#002b5b", fg="white", font=("Poppins", 16, "bold"))
canvas.create_window(300, 350, window=hesapla_button)

# Uygulamayı çalıştır
root.mainloop()
