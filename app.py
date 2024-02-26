import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import pickle

model = pickle.load(open("reg.pkl", "rb"))
pre_model = pickle.load(open("preprocessor.pkl", "rb"))

st.set_page_config("wide")
selected = option_menu("Main menu", ["home", "Diamond Price Predictor","Info"], icons=["house", "diamond","Info"],
                       orientation="horizontal")

with st.sidebar:
    st.header(":blue[About Me] :man:")
    st.write("I am an AI and Data Science Student. Passionate about Data science and ML")
    github_emoji = "\U0001F680"
    github_link = f"[Github Profile {github_emoji}](https://github.com/BHEESETTIANAND)"
    st.markdown(github_link, unsafe_allow_html=True)
    st.write("To see my work, please visit the link to my portfolio below.")
    portfolio_link = "https://anandbheesetti.wixsite.com/portfolio"
    st.markdown(portfolio_link, unsafe_allow_html=True)
    gmail_emoji = "\U0001F4E7"
    st.markdown(f"email me at {gmail_emoji}")
    st.write("anandbheesetti@gmail.com")

if selected == "home":
    st.title(" Diamond Price Predictor")
    st.write("With the help of this project Predict the Price of your Diamond")
    st.image("th.jpg")
    

if selected == "Diamond Price Predictor":
    f1 = st.number_input("**Enter the carat value of diamond**")
    f2 = st.number_input(f"**Enter the Depth value**")
    f3 = st.number_input(f"**Enter the table value**")
    f4 = st.number_input(f"**Enter the X value**")
    f5 = st.number_input(f"**Enter the  Y value**")
    f6 = st.number_input(f"**Enter the Z  value**")
    f7 = st.selectbox("select the cut type of your diamond", ("Fair", "Good", "Very Good", "Premium", "Ideal"))
    f8 = st.selectbox("select the color type of your diamond", ("D", 'E', 'F', 'G', 'H', 'I', 'J'))
    f9 = st.selectbox("select the Clarity type of your diamond", ("I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"))

    features_df = pd.DataFrame({
        'carat': [f1],
        'depth': [f2],
        'table': [f3],
        'x': [f4],
        'y': [f5],
        'z': [f6],
        'cut': [f7],
        'color': [f8],
        'clarity': [f9]
    })

    pre_pro_fea = pre_model.transform(features_df)
    pre = model.predict(pre_pro_fea)
    if st.button("Predict"):
        st.write(pre)
        
if selected == "Info":
    st.image("four-cs-of-diamonds-grahams.jpg")


