import streamlit as st
import joblib
import time  # Importado para simular um atraso no exemplo

# Função para carregar o modelo e o vectorizer, otimizado com cache
@st.cache_resource
def load_resources():
    model = joblib.load('models/best_model.pkl')
    vectorizer = joblib.load('models/vectorizer.pkl')
    return model, vectorizer

def show():
    st.title("Previsão de Sentimentos de Textos ou Tweets")

    # Carregar o modelo e o vectorizer
    model, vectorizer = load_resources()

    # Aviso sobre acurácia do modelo com destaque
    st.warning(
        """
        **Aviso:** Este modelo de previsão de sentimentos é baseado em aprendizado de máquina e pode não ser 100% preciso. A precisão pode variar e o modelo pode cometer erros. Use as previsões como uma referência adicional.
        """,
        icon="⚠️"
    )

    st.write("Digite um texto ou tweet abaixo para analisar o sentimento:")

    # Entrada do usuário
    user_input = st.text_area("Texto para análise:")

    if st.button("Prever"):
        if user_input.strip():
            # Mostrar a barra de progresso
            progress_bar = st.progress(0)
            status_text = st.empty()
            status_text.text("Analisando o texto...")

            try:
                # Simular um atraso para a barra de progresso (pode ser removido em produção)
                for i in range(100):
                    time.sleep(0.01)  # Ajuste o tempo conforme necessário
                    progress_bar.progress(i + 1)

                # Transformar o texto de entrada
                X_input = vectorizer.transform([user_input])

                # Fazer a previsão
                prediction = model.predict(X_input)[0]

                # Exibir o resultado
                sentiment = "Positivo" if prediction == 1 else "Negativo"
                if sentiment == "Positivo":
                    st.success(f"O sentimento do texto é: **{sentiment}**")
                else:
                    st.error(f"O sentimento do texto é: **{sentiment}**")

            except Exception as e:
                st.error(f"Ocorreu um erro durante a previsão: {str(e)}")

            # Remover a barra de progresso e o texto de status
            progress_bar.empty()
            status_text.empty()

        else:
            st.warning("Por favor, digite um texto não vazio.")
