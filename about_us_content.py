import streamlit as st
import webbrowser

def about_us_content(page):
    if page == "About us":
        st.title("About Us")
        st.write("")
        st.write("")



        lst = ['Hüseyin Arda Tuz', "İrem Özdemir","Kayrahan Toprak Tosun", "Nisa Eylül Çintiriz","Tuna Kodal"]

        for character in lst:
            st.write("- "+character)

        st.write("")

        character = st.selectbox("Choose your character from the list above", lst)

        if character == "Hüseyin Arda Tuz":
            st.write("I'm Hüseyin Arda Tuz and here is my contact info.")
            if st.button("Linkedin"):
               webbrowser.open("https://www.linkedin.com/in/hüseyin-arda-tuz-a0a773254/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app")
        elif character == "İrem Özdemir":
            st.write("I'm İrem Özdemir and here is my contact info.")
            if st.button("Linkedin"):
               webbrowser.open("https://www.linkedin.com/in/irem-ozdmr/")
        elif character == "Kayrahan Toprak Tosun":
            st.write("I'm Kayrahan Toprak Tosun and here is my contact info.")
            if st.button("Linkedin"):
               webbrowser.open("https://www.linkedin.com/in/kayrahantosun/")
        elif character == "Nisa Eylül Çintiriz":
            st.write("I'm Nisa Eylül Çintiriz and here is my contact info.")
            if st.button("Linkedin"):
               webbrowser.open("https://www.linkedin.com/in/eyllcintiriz/")   
        elif character == "Tuna Kodal":
            st.write("I'm Tuna Kodal and here is my contact info.")
            if st.button("Linkedin"):
               webbrowser.open("https://www.linkedin.com/in/tuna-kodal-15514a231/")   
    elif page == "Main page":
        st.title("")
        st.write("")

def about_our_project(page):
    if page == "About our project":
        st.title("About Our Project")
        st.write("")
        st.write("")
        st.write("Our website is a collaborative project that lets users explore planes in various cities. Using API structure, we built a modular system for seamless data retrieval. Teamwork and Kanban planning were key to our success, allowing us to efficiently manage tasks and achieve our project goals. ")
        st.write("")

        st.write("Our kanban plan that we followed through our teamwork:")

        if st.button("Kanban plan"):
               webbrowser.open("https://datadaredevils.teamhood.com/TUWO/Board/TUKO1?view=LIST")
            
        


