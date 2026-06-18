import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Vocab",
    page_icon="🇬🇧",
    layout="centered"
)

# Perbaikan pada '1 px' menjadi '1px'
st.markdown("""
    <style>
    .main-title {
        font-family: 'Inter', sans-serif;
        text-align: center;
        letter-spacing: 1px;
        margin-bottom: 20px;
    }
    
    .sub-title {
        text-align: center; 
        color: #94A3B8; 
        font-size: 15px;
        margin-bottom: 40px;
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

# Judul Utama
st.markdown("<h1 class='main-title'>🇬🇧 Vocab & Sentences</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Andreyson</p>", unsafe_allow_html=True)

tab_word, tab_sentence = st.tabs(["Words & Vocab", "Sentences & Idioms"])

# ================= TAB WORDS =================
with tab_word:
    st.write("") # Pengganti <br> yang lebih clean di Streamlit
    
    try:
        df_word = pd.read_excel("daftar_vocab.xlsx")
        vocab_data = df_word.to_dict(orient="records")
        
        for item in vocab_data:
            # Menggunakan method .get() untuk menghindari KeyError jika kolom tidak pas
            vocab_name = item.get('Vocab', 'N/A')
            vocab_pos = item.get('Pos', 'N/A')
            judul_expander = f"{vocab_name}  |  {vocab_pos}"
            
            with st.expander(judul_expander, expanded=False):
                st.markdown("<p class='content-label'>Arti:</p>", unsafe_allow_html=True)
                st.markdown(f"<p class='content-text'>{item.get('Arti', '-')}</p>", unsafe_allow_html=True)
                
                st.markdown("<p class='content-label'>Contoh Kalimat:</p>", unsafe_allow_html=True)
                st.info(f"\"{item.get('Contoh', '-')}\"")
                
    except FileNotFoundError:
        st.error("File 'daftar_vocab.xlsx' tidak ditemukan. Pastikan file berada di folder yang sama dengan skrip ini.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")

# ================= TAB SENTENCES =================
with tab_sentence:
    st.write("")
    
    try:
        df_sentence = pd.read_excel("daftar_sentence.xlsx")
        sentence_data = df_sentence.to_dict(orient="records")
        
        for item in sentence_data:
            judul_sentence = f"{item.get('Sentence', 'N/A')}"
            
            with st.expander(judul_sentence, expanded=False):
                st.markdown("<p class='content-label'>Arti / Terjemahan:</p>", unsafe_allow_html=True)
                st.success(f"\"{item.get('Arti', '-')}\"")
                
                st.markdown("<p class='content-label'>Penjelasan Konteks:</p>", unsafe_allow_html=True)
                st.markdown(f"<p class='content-text'>{item.get('Penjelasan', '-')}</p>", unsafe_allow_html=True)
                
    except FileNotFoundError:
        st.error("File 'daftar_sentence.xlsx' tidak ditemukan. Pastikan file berada di folder yang sama dengan skrip ini.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")