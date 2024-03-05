import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests

st.title(":blue[**our bil481 project**]")

option = st.selectbox('please choose the country for flight information:',('america', 'turkey', 'france'))

st.write('you selected:', option)

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

# API endpoint URL
url = "https://api.adsb.lol/v2/ladd"

# GET isteği gönderme
response = requests.get(url)

# DataFrame'i oluşturmak için boş bir liste oluşturalım
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

    # Liste ile DataFrame oluşturma
    df = pd.DataFrame(aircraft_list)

    st.map(df)
    # DataFrame'i yazdırma
    print(df)
else:
    print("API'ye erişimde bir hata oluştu. Hata kodu:", response.status_code)


#with open('style.css') as f:
#    css = f.read()

#st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

#video_file = open('background.mp4', 'rb')
#video_bytes = video_file.read()
#st.video(video_bytes)