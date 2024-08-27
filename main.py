import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import json
import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Configuração da página principal
st.set_page_config(page_title="Sentiment Analysis", page_icon="🧠")

st.markdown(
    f"""
    <style>
    {open("static/styles.css").read()}
    </style>
    """,
    unsafe_allow_html=True
)

# Carregar animações
with open("animaçoes/animationproduct.json") as source:
    animacao_1 = json.load(source)

# Menu de navegação
with st.sidebar:
    # Exibir animação
    st_lottie(animacao_1, height=200, width=270)

    selected = option_menu("Menu", ["Home", "Previsão NLP", "Sobre"], 
                           icons=['house', 'pencil', 'info-circle'], 
                           menu_icon="cast", default_index=0)

    # Badges
    st.markdown(
        """
    <div style="display: flex; justify-content: space-between;">
        <div>
            <a href="https://github.com/thaleson" target="_blank">
                <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" width="100" />
            </a>
        </div>
        <div>
            <a href="https://www.linkedin.com/in/thaleson-silva-9298a0296/" target="_blank">
                <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" width="100" />
            </a>
        </div>
        <div>
            <a href="mailto:thaleson177@gmail.com" target="_blank">
                <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" width="80" />
            </a>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

# Navegação para as páginas
if selected == "Home":
    from pages.nav import home
    home.show()
elif selected == "Previsão NLP":
    from pages.nav import predict
    predict.show()
elif selected == "Sobre":
    from pages.nav import about
    about.show()
