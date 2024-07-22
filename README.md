# Sentiment Analysis App

## Descrição

Este projeto é uma aplicação de análise de sentimentos construída com [Streamlit](https://streamlit.io/) e [Transformers](https://huggingface.co/transformers). A aplicação utiliza um modelo de linguagem treinado para classificar o sentimento de frases inseridas pelo usuário, oferecendo uma visualização clara dos resultados.

## Funcionalidades

- **Análise de Sentimentos**: Classifica o sentimento das frases fornecidas pelo usuário em categorias como positivo, negativo ou neutro.
- **Interface Intuitiva**: Interface de usuário amigável e interativa construída com Streamlit.
- **Visualização de Resultados**: Exibe o resultado da análise de sentimentos de forma visual e intuitiva.

## Tecnologias Utilizadas

- **Streamlit**: Framework para criar aplicações web interativas em Python.
- **Transformers**: Biblioteca para modelos de linguagem baseados em transformers.
- **Torch**: Biblioteca para computação numérica e aprendizado profundo.

---

## Instalação

Siga estes passos para instalar e executar a aplicação localmente:

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/seu_usuario/sentimentus_ml.git

## Passos para Rodar o Projeto

### Navegue até o Diretório do Projeto

```bash
cd sentimentus_ml
```

### Crie e Ative um Ambiente Virtual

Para **Linux/macOS**:

1. Crie o ambiente virtual:
    ```bash
    python -m venv venv
    ```

2. Ative o ambiente virtual:
    ```bash
    source venv/bin/activate
    ```

Para **Windows**:

1. Crie o ambiente virtual:
    ```bash
    python -m venv venv
    ```

2. Ative o ambiente virtual:
    ```bash
    venv\Scripts\activate
    ```

### Instale as Dependências

```bash
pip install -r requirements.txt
```

### Execute a Aplicação

```bash
streamlit run sentimentus.py
```

## Versão Online na Nuvem
O projeto também pode ser acessado diretamente na nuvem. Foi montada uma imagem Docker, e em seguida feito um deploy no Google Cloud, Acesse Via link : https://sentimentus-app-bkm6lf7kiq-rj.a.run.app
