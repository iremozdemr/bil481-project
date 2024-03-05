import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import time

st.title(":blue[**our bil481 project**]")

option = st.selectbox('please choose the country for flight information:',('america', 'turkey', 'france'))

st.write('you selected:', option)

# API endpoint URL
url = "https://api.adsb.lol/v2/ladd"

@st.cache_data(ttl=10)  # 10 saniye cache süresi
def get_aircraft_data():
    # GET isteği gönderme
    response = requests.get(url)

    aircraft_list = []

    # Yanıtı kontrol etme
    if response.status_code == 200:
        # Yanıtı JSON formatına dönüştürme
        data = response.json()

        # Uçaklar listesini alma
        aircrafts = data.get("ac", [])

        # Her bir uçak için bilgileri liste içine ekleme
        for aircraft in aircrafts:
            lat = aircraft.get("lat", 0)
            lon = aircraft.get("lon", 0)
            
            # Her bir uçağın bilgilerini bir sözlükte toplama
            aircraft_info = {
                "lat": lat,
                "lon": lon
            }
            
            # Her bir uçağın bilgilerini liste içine ekleme
            aircraft_list.append(aircraft_info)

    return aircraft_list

# İlk haritayı oluşturmak için boş bir container oluşturalım
map_container = st.empty()

while True:
    aircraft_list = get_aircraft_data()
    df = pd.DataFrame(aircraft_list)
    
    # Önceki haritayı temizleyip yeni haritayı gösterme
    with map_container:
        st.map(df)
    
    time.sleep(10)  # 10 saniye bekleme süresi