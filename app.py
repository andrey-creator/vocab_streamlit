import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="British English Learning Center",
    page_icon="🇬🇧",
    layout="centered"
)

st.markdown("""
    <style>
    .main-title {
        font-family: 'Inter', sans-serif;
        text-align: center;
        letter-spacing: -0.5px;
        margin-bottom: 10px;
    }
    
    div[data-testid="stExpander"] {
        border: 1px solid #475569 !important;
        border-radius: 12px !important;
        margin-bottom: 12px !important;
    }
    
    .content-label {
        font-weight: 700 !important;
        margin-top: 10px;
        margin-bottom: 2px;
    }
    
    .content-text {
        font-size: 16px !important;
        line-height: 1.5;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🇬🇧 ---------</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94A3B8; font-size: 15px;'>Platform ------</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

tab_word, tab_sentence = st.tabs(["📚 Words & Vocab", "🗣️ Sentences & Idioms"])

with tab_word:
    st.markdown("<br>", unsafe_allow_html=True)
    
    try:
        df_word = pd.read_excel("daftar_vocab.xlsx")
        vocab_data = df_word.to_dict(orient="records")
        
        for item in vocab_data:
            judul_expander = f"{item['Vocab']}  |  {item['Pos']}"
            
            with st.expander(judul_expander, expanded=False):
                st.markdown("<p class='content-label'>Arti:</p>", unsafe_allow_html=True)
                st.markdown(f"<p class='content-text'>{item['Arti']}</p>", unsafe_allow_html=True)
                
                st.markdown("<p class='content-label'>Contoh Kalimat:</p>", unsafe_allow_html=True)
                st.info(f"\"{item['Contoh']}\"")
                
    except FileNotFoundError:
        st.error("File 'daftar_vocab.xlsx' tidak ditemukan.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")

with tab_sentence:
    st.markdown("<br>", unsafe_allow_html=True)
    
    try:
        df_sentence = pd.read_excel("daftar_sentence.xlsx")
        sentence_data = df_sentence.to_dict(orient="records")
        
        for item in sentence_data:
            judul_sentence = f"{item['Sentence']}"
            
            with st.expander(judul_sentence, expanded=False):
                st.markdown("<p class='content-label'>Arti / Terjemahan:</p>", unsafe_allow_html=True)
                st.success(f"\"{item['Arti']}\"")
                
                st.markdown("<p class='content-label'>Penjelasan Konteks:</p>", unsafe_allow_html=True)
                st.markdown(f"<p class='content-text'>{item['Penjelasan']}</p>", unsafe_allow_html=True)
                
    except FileNotFoundError:
        st.error("File 'daftar_sentence.xlsx' tidak ditemukan.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")