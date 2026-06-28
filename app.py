import streamlit as st
import pandas as pd
import random

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
st.markdown("<h1 class='main-title'>Vocab & Sentences</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Andreyson</p>", unsafe_allow_html=True)

tab_word, tab_sentence = st.tabs(["Words & Vocab", "Sentences & Idioms"])

# ================= TAB WORDS =================
with tab_word:
    st.write("") # Pengganti <br> yang lebih clean di Streamlit
    
    try:
        df_word = pd.read_excel("daftar_vocab.xlsx")
        
        # --- 1. KONTROL FILTER & SORTING ---
        col1, col2 = st.columns(2)
        
        with col1:
            # Mengambil semua jenis POS unik secara dinamis dari Excel
            list_pos = ["All"] + sorted(df_word['Pos'].dropna().unique().tolist())
            pilihan_pos = st.selectbox("Filter according to POS:", list_pos, key="filter_pos")
            
        with col2:
            pilihan_urut = st.selectbox("Order by:", ["Default", "A-Z", "Random"], key="sort_vocab")
        
        # --- 2. PROSES FILTERING ---
        if pilihan_pos != "All":
            df_proses = df_word[df_word['Pos'] == pilihan_pos].copy()
        else:
            df_proses = df_word.copy()
            
        # --- 3. PROSES SORTING ---
        if pilihan_urut == "A-Z":
            df_proses = df_proses.sort_values(by='Vocab', ascending=True, key=lambda col: col.str.lower())
            
        elif pilihan_urut == "Random":
            # State agar urutan acak tidak berubah-ubah saat expander diklik
            if "vocab_seed" not in st.session_state:
                st.session_state.vocab_seed = 42
                
            df_proses = df_proses.sample(frac=1, random_state=st.session_state.vocab_seed)
            
            # Tombol khusus untuk mengocok ulang urutan kata
            if st.button("Acak Ulang Kata"):
                st.session_state.vocab_seed = random.randint(1, 10000)
                st.rerun()

        # Konversi dataframe hasil filter/sort ke dictionary
        vocab_data = df_proses.to_dict(orient="records")
        
        # --- 4. RENDER EXPANDER ---
        if not vocab_data:
            st.warning("Tidak ada kosakata yang cocok dengan filter POS ini.")
            
        for item in vocab_data:
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
        st.error(f"Terjadi kesalahan pada Tab Vocab: {e}")

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
                
                st.markdown("<p class='content-label'>Contoh Kalimat:</p>", unsafe_allow_html=True)
                st.markdown(f"<p class='content-text'>{item.get('Contoh', '-')}</p>", unsafe_allow_html=True)
                
    except FileNotFoundError:
        st.error("File 'daftar_sentence.xlsx' tidak ditemukan. Pastikan file berada di folder yang sama dengan skrip ini.")
    except Exception as e:
        st.error(f"Terjadi kesalahan pada Tab Sentence: {e}")