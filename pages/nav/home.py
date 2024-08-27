import json
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottie_animation(file_path):
    """Carregar a animação Lottie a partir do arquivo JSON"""
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error(f"Arquivo não encontrado: {file_path}")
        return None
    except json.JSONDecodeError:
        st.error(f"Erro ao decodificar o arquivo JSON: {file_path}")
        return None

def show():
    # Configurar o título da página
    st.title("Bem-vindo ao Analisador de Sentimentos! 🧠")

    # Adicionar subtítulo
    st.subheader("Descubra os sentimentos por trás dos tweets! 👋")

    # Carregar animações
    animation_1 = load_lottie_animation("animaçoes/animation3.json")  # Animação principal
    animation_2 = load_lottie_animation("animaçoes/animationproduct.json")  # Outra animação opcional

    if animation_1 and animation_2:
        # Configurar layout em colunas
        col1, col2 = st.columns(2)

        # Conteúdo da coluna 1
        with col1:
            st_lottie(animation_1, height=350, width=350, key="animation1")
            st.markdown(
                """
                <div style='margin-top: 10px;'>
                    <h5 style='text-align: justify;'>Este aplicativo permite que você insira tweets e receba uma análise do sentimento por trás deles. Utilizamos técnicas avançadas de processamento de linguagem natural para identificar se o sentimento é positivo ou negativo.</h5>
                </div>
                """,
                unsafe_allow_html=True
            )

        # Conteúdo da coluna 2
        with col2:
            st.markdown(
                """
                <div style='margin-top: 10px;'>
                    <h5 style='text-align: justify;'>Explore a funcionalidade de previsão de sentimentos para obter uma visão mais profunda sobre as opiniões expressas em tweets. Navegue pelas outras seções para saber mais sobre o projeto e as tecnologias utilizadas.</h5>
                </div>
                """,
                unsafe_allow_html=True
            )
            st_lottie(animation_2, height=350, width=350, key="animation2")

        # Adicionar um aviso
        st.markdown(
            """
            <div style='background-color: #d4edda; padding: 15px; border-radius: 8px;'>
                <h4 style='color: #155724;'>Aviso:</h4>
                <p style='color: #155724;'>Este projeto é uma demonstração da análise de sentimentos e pode não refletir a precisão total dos modelos de Machine Learning. Utilize as previsões como uma referência adicional.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("Não foi possível carregar as animações.")

if __name__ == "__main__":
    show()
