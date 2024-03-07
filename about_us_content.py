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
            st.write("Text for Hüseyin Arda Tuz")
        elif character == "İrem Özdemir":
            st.write("Text for İrem Özdemir")
        elif character == "Kayrahan Toprak Tosun":
            st.write("Text for Kayrahan Toprak Tosun")
        elif character == "Nisa Eylül Çintiriz":
            st.write("I'm Nisa Eylül Çintiriz and here is my Linkedin")
            if st.button("Linkedin"):
               webbrowser.open("http://www.example.com")
            
        elif character == "Tuna Kodal":
            st.write("Text for Tuna Kodal")
    elif page == "Main page":
        st.title("Main Page")
        st.write("This is the Main page content.")

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
            
        


