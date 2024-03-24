import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import time
import DataManipulation
import GetFromAPI

from about_us_content import about_us_content
from about_us_content import about_our_project

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select Page", ("Main page", "About us", "About our project"))

about_us_content(page)
about_our_project(page)


def assign_data():
    longitudes = DataManipulation.get_longitudes()
    latitudes = DataManipulation.get_latitudes()
    return longitudes, latitudes


def assign_aircraft_list():
    aircraft_list = DataManipulation.get_aircrafts()
    return aircraft_list


if page == "Main page":
    st.title(":blue[*our bil481 project*]")

    option = st.selectbox('please choose the country for flight information:', ('World', 'New York', 'Washington',
                                                                                'Los Angeles', 'Istanbul', 'Roma',
                                                                                'Berlin'))

    st.write('you selected:', option)

    # First iteration
    GetFromAPI.load_flight_data()
    longitude, latitude = assign_data()

    if option == 'World':
        # Loads data for whole world
        GetFromAPI.load_flight_data()
        longitude, latitude = assign_data()
    else:
        # Loads data using city name
        GetFromAPI.load_precise_data(option)
        longitude, latitude = assign_data()

    # Empty container to draw the first map on
    map_container = st.empty()

    # Empty container to draw the first graph on
    figure_container = st.empty()

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(longitude, latitude, marker='o', color='blue')
    ax.set_xlabel('Boylam')
    ax.set_ylabel('Enlem')
    ax.set_title('Uçakların Konumu')
    ax.grid(True)

    # Show MatPlotLib Figure on Streamlit
    figure_container.pyplot(fig)

    while True:
        print(option)

        aircraft_list = assign_aircraft_list()
        df = pd.DataFrame(aircraft_list)

        if option == 'World':
            # Loads data for whole world
            GetFromAPI.load_flight_data()
            longitude, latitude = assign_data()
        else:
            # Loads data using city name
            GetFromAPI.load_precise_data(option)
            longitude, latitude = assign_data()

        # Repaint the map
        with map_container:
            st.map(df)

        # Repaint the graph
        with figure_container:
            figure_container.empty()
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.scatter(longitude, latitude, marker='o', color='blue')
            ax.set_xlabel('Boylam')
            ax.set_ylabel('Enlem')
            ax.set_title('Uçakların Konumu')
            ax.grid(True)
            figure_container.pyplot(fig)

        time.sleep(5)