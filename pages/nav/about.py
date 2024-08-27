import streamlit as st

def show():
    st.header("Sobre o Projeto")
    st.write(
        """
        Bem-vindo ao nosso projeto de **Análise de Sentimentos em Tweets**! 🧠

        Este projeto é uma aplicação avançada que utiliza técnicas de processamento de linguagem natural e aprendizado de máquina para analisar o sentimento expresso em tweets. Através de modelos de aprendizado de máquina, nossa aplicação classifica os sentimentos dos tweets como positivos, negativos ou neutros com base no texto fornecido.

        ### Como Funciona
        1. **Entrada do Usuário**: Você insere um tweet ou um texto para análise.
        2. **Processamento**: Nosso sistema utiliza modelos como **Naive Bayes** e **Random Forest** para analisar o texto e identificar o sentimento.
        3. **Previsão**: A aplicação retorna a classificação do sentimento do texto inserido.

        ### Tecnologias Utilizadas
        - **Python**: Linguagem de programação principal para desenvolvimento e manipulação de dados.
        - **Streamlit**: Framework para criação de aplicações web interativas e fáceis de usar.
        - **Scikit-learn**: Biblioteca para implementação de modelos de aprendizado de máquina e processamento de texto.
        - **NLTK**: Biblioteca para processamento de linguagem natural e análise de texto.
        - **Pandas**: Biblioteca essencial para manipulação e análise de dados.
        - **Joblib**: Utilizado para armazenar e carregar modelos treinados de forma eficiente.

        ### Funcionalidades
        - **Análise de Sentimentos**: Classifique o sentimento de tweets e outros textos.
        - **Interface Intuitiva**: Navegue facilmente através de uma interface simples e amigável.
        - **Modelos Avançados**: Utilize modelos de aprendizado de máquina para obter previsões precisas.

        ### Objetivo
        O objetivo principal deste projeto é fornecer uma ferramenta útil para a análise de sentimentos, ajudando a compreender as opiniões expressas em tweets e outros textos de forma rápida e eficiente.

        **Agradecemos por utilizar nossa aplicação e esperamos que ela ajude a explorar e entender melhor os sentimentos expressos nas redes sociais!** 😊
        """
    )
