import streamlit as st
import subprocess

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("About us", "Main page")
)

if add_selectbox == "About us":
    subprocess.Popen(["streamlit", "run", "about_us.py"])
elif add_selectbox == "Main page":
    # Display content for the main page here
    subprocess.Popen(["streamlit", "run", "streamlit_app.py"])
    st.write("This is the Main page.")


st.header("About Us")
st.write("")
st.write("choose your character from the list below")

lst = ['Hüseyin Arda Tuz', "İrem Özdemir","Kayrahan Toprak Tosun", "Nisa Eylül Çintiriz","Tuna Kodal"]

s = ''

for i in lst:
    s += "- " + i + "\n"

st.markdown(s)

character = st.selectbox(
    "choose your character",
    ("Hüseyin Arda Tuz","İrem Özdemir","Kayrahan Toprak Tosun", "Nisa Eylül Çintiriz","Tuna Kodal")
)

if character == "Hüseyin Arda Tuz":
    st.write("Text for Hüseyin Arda Tuz")
elif character == "İrem Özdemir":
    st.write("Text for İrem Özdemir")
elif character == "Kayrahan Toprak Tosun":
    st.write("Text for Kayrahan Toprak Tosun")
elif character == "Nisa Eylül Çintiriz":
    st.write("Text for Nisa Eylül Çintiriz")
elif character == "Tuna Kodal":
    st.write("Text for Tuna Kodal")