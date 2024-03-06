import requests


# Örnek olarak tanımlanan enlem, boylam, yarıçap değerleri
lat = 39.28923
lon = 35.324
# 'radius' nm(deniz mili) cinsinden hesaplanır. (1 nm = 1852,2 m)
radius = 250

# API endpoint URL , değişken
url = f"https://api.adsb.lol/v2/point/{lat}/{lon}/{radius}"

# GET isteği gönderme
response = requests.get(url)

# Yanıtı kontrol etme
if response.status_code == 200:
    # Yanıtı JSON formatına dönüştürme
    data = response.json()

    # Uçaklar listesini alma
    aircrafts = data.get("ac", [])

    # Her bir uçak için bilgileri yazdırma
    # Buradaki for föngüsü içinde yapılan işlemler örnek teşkil etmektedir.
    for aircraft in aircrafts:
        flight = aircraft.get("flight", "Bilinmiyor")
        lat = aircraft.get("lat", 0)
        lon = aircraft.get("lon", 0)
        alt = aircraft.get("alt_geom", 0)
        print(f"Uçuş: {flight}, Enlem: {lat}, Boylam: {lon}, Yükseklik: {alt}")
else:
    print("API'ye erişimde bir hata oluştu. Hata kodu:", response.status_code)
