# 📊 Análise de Sentimentos de Textos e Tweets

Bem-vindo ao projeto de **Análise de Sentimentos**! 🎉 Este projeto utiliza aprendizado de máquina para prever o sentimento de textos e tweets. Ele é construído usando Python e uma aplicação web interativa com Streamlit.

## 🚀 Funcionalidades

- **Previsão de Sentimentos**: Analisa o texto fornecido para determinar se o sentimento é positivo ou negativo.
- **Interface Intuitiva**: Use uma interface web simples e amigável criada com Streamlit.
- **Feedback Imediato**: Veja o resultado da análise de sentimentos com uma barra de progresso enquanto o texto está sendo analisado.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Streamlit**: Framework para criar a interface web.
- **Scikit-learn**: Biblioteca para aprendizado de máquina.
- **Joblib**: Para carregar o modelo treinado e o vetorizer.

## 📦 Instalação

1. **Clone o Repositório**:

   ```bash
   git clone https://github.com/thaleson/sentimentsanalysis.git
   cd sentimentsanalysis
   ```

2. **Crie um Ambiente Virtual** (recomendado):

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Para Windows: .venv\Scripts\activate
   ```

3. **Instale as Dependências**:

   ```bash
   pip install -r requirements.txt
   ```

## 🖥️ Uso

1. **Inicie a Aplicação Streamlit**:

   ```bash
   streamlit run app.py
   ```

2. **Acesse a Aplicação**: Abra seu navegador e vá para [http://localhost:8501](http://localhost:8501).

## 🔍 Como Funciona

1. **Digite um Texto**: Insira o texto ou tweet que você deseja analisar.
2. **Clique em "Prever"**: A aplicação processará o texto e exibirá o sentimento previsto.
3. **Veja o Resultado**: Receba o feedback com uma barra de progresso e veja o sentimento identificado.

## 📈 Exemplo de Resultados

- **Texto**: "Eu adoro este produto, é incrível!"  
  **Sentimento**: Positivo 😊

- **Texto**: "Péssimo serviço, não volto mais."  
  **Sentimento**: Negativo 😡

## ⚠️ Aviso

Este modelo de previsão de sentimentos é baseado em aprendizado de máquina e pode não ser 100% preciso. A precisão pode variar e o modelo pode cometer erros. Use as previsões como uma referência adicional.

## 📝 Contribuições

Contribuições são sempre bem-vindas! Se você tiver sugestões ou melhorias, fique à vontade para abrir uma issue ou enviar um pull request.

