import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

pipe = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-sentiment-latest")
tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment-latest")
model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment-latest")

st.markdown("""
    <div style='text-align: center; padding: 5px; border: 2px solid #1E90FF; border-radius: 10px; background-color: #f0f8ff; width:50%; margin:0 0 0 25%;'>
        <h1 style='color: #1E90FF;'>Bioinformatics Project</h1>
    </div>
""", unsafe_allow_html=True)
st.title('Sentimentus')
st.write('Sentiment Analysis with Hugging Face and Streamlit')

with st.form(key='sentiment_form'):
    user_text = st.text_area("Write your text here:")
    submit_button = st.form_submit_button(label='Analyze Sentiment')

def get_color(score):
    if score > 0.75:
        return '#4CAF50'  # Green
    elif score > 0.5:
        return '#FFC107'  # Yellow
    elif score > 0.25:
        return '#FF5722'  # Orange
    else:
        return '#F44336'  # Red

if submit_button and user_text:
    result = pipe(user_text)
    st.write("## Sentiment Analysis Results:")
    for sentiment in result:
        label = sentiment['label']
        score = sentiment['score']
        if label == "positive":  # Verifique o nome correto do rótulo para POSITIVE
            emoji = "😄"
            sentiment_text = "Positive"
            st.balloons()
        elif label == "negative":  # Verifique o nome correto do rótulo para NEGATIVE
            emoji = "😡"
            sentiment_text = "Negative"
        elif label == "neutral":  # Verifique o nome correto do rótulo para NEUTRAL
            emoji = "😐"
            sentiment_text = "Neutral"
        
        color = get_color(score)
        st.markdown(f"<div style='padding: 10px; border-radius: 5px; background-color: #1C1C1C;'>"
                    f"<h4 style='color: #f0f2f6;'>Sentiment: {sentiment_text} {emoji}</h4>"
                    f"<div style='background-color: #ddd; border-radius: 5px;'>"
                    f"<div style='width: {score*100}%; background-color: {color}; height: 20px; border-radius: 5px;'></div>"
                    f"</div>"
                    f"<p style='color: #f0f2f6;'><strong>There is {score*100:.2f}% that this phrase is {label}.</strong></p>"
                    f"</div>", unsafe_allow_html=True)

# Referências
st.markdown("""
#### References:
- [TimeLMs paper](https://arxiv.org/abs/2202.03829)
- [TimeLMs official repository](https://github.com/cardiffnlp/timelms)
""")

# Estilização adicional
st.markdown(
    """
    <style>
    .stButton button {
        background: #4CAF50;
        color: white;
    }
    .stButton button:hover {
        background: #388E3C;
        color: white;
        border-color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)
