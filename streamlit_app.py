import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import time
import DataManipulation
import GetFromAPI
import pydeck as pdk

from about_us_content import about_us_content
from about_us_content import about_our_project

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select Page", ("Main page", "About us", "About our project"))

about_us_content(page)
about_our_project(page)

if "scatter" not in st.session_state:
    st.session_state.scatter = None


def assign_data():
    longitudes = DataManipulation.get_longitudes()
    latitudes = DataManipulation.get_latitudes()
    return longitudes, latitudes


def assign_aircraft_list():
    aircraft_list = DataManipulation.get_aircrafts()
    return aircraft_list


if page == "Main page":
    st.title(":blue[Our BİL481 Project]")

    option = st.selectbox('Please choose the country for flight information: (Please wait for "World" to load before '
                          'choosing)', ('World', 'New York', 'Washington',
                                        'Los Angeles', 'Istanbul', 'Roma',
                                        'Berlin'))

    st.write('You selected:', option)

    # First iteration
    GetFromAPI.load_flight_data()
    longitude, latitude = assign_data()
    altitude = DataManipulation.get_altitudes()
    time_passed = 1

    if option == 'World':
        # Loads data for whole world
        GetFromAPI.load_flight_data()
        longitude, latitude = assign_data()
        radius = 30000
    else:
        # Loads data using city name
        GetFromAPI.load_precise_data(option)
        longitude, latitude = assign_data()
        radius = 1000

    figure_container = st.empty()

    # Create initial scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    scatter = ax.scatter(longitude, latitude, marker='o', color='blue')
    ax.set_xlabel('Boylam')
    ax.set_ylabel('Enlem')
    ax.set_title('Uçakların Konumu')
    ax.grid(True)

    # Show MatPlotLib Figure on Streamlit
    with figure_container:
        st.pyplot(fig)

    # First map creation
    df = pd.DataFrame({'latitude': latitude, 'longitude': longitude})

    map_view = pdk.ViewState(
        latitude=np.mean(latitude),
        longitude=np.mean(longitude),
        zoom=7,
        min_zoom=7,
        max_zoom=7,
        pitch=20)

    scatter_layer = pdk.Layer(
        'ScatterplotLayer',
        data=df,
        get_position='[longitude, latitude]',
        get_radius=radius,
        get_fill_color='[255, 0, 0]',
        pickable=True,
        auto_highlight=True,
        interactive=False
    )

    map_chart = pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=map_view,
        layers=[scatter_layer],
    )

    if option == 'World':
        map_view.zoom = 1
        map_view.max_zoom = 1
        map_view.min_zoom = 1
        map_view.latitude = 0
        map_view.longitude = 0

    else:
        map_view.zoom = 9
        map_view.max_zoom = 9
        map_view.min_zoom = 9

    map_widget = st.pydeck_chart(map_chart)

    while True:
        print(option)

        aircraft_list = assign_aircraft_list()
        df = pd.DataFrame(aircraft_list)

        if option == 'World':
            # Loads data for whole world
            GetFromAPI.load_flight_data()
            time.sleep(5)
            longitude, latitude = assign_data()
            map_view.zoom = 1
            map_view.max_zoom = 1
            map_view.min_zoom = 1
            map_view.latitude = 0
            map_view.longitude = 0

        else:
            # Loads data using city name
            GetFromAPI.load_precise_data(option)
            time.sleep(5)
            longitude, latitude = assign_data()
            map_view.zoom = 9
            map_view.max_zoom = 9
            map_view.min_zoom = 9

            # Update scatter plot data
            scatter.remove()
            scatter = ax.scatter(longitude, latitude, marker='o', color='blue')

        with figure_container:
            # figure_container.empty()
            figure_container.pyplot(fig)

        # Update map data
        df = pd.DataFrame({'latitude': latitude, 'longitude': longitude})
        scatter_layer.data = df

        # Trigger rerun to update plot
        map_widget.pydeck_chart(map_chart)
