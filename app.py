import streamlit as st
import pandas as pd

# Pengaturan halaman
st.set_page_config(
    page_title="British Vocab Builder",
    page_icon="🇬🇧",
    layout="centered"
)

# Judul Aplikasi
st.title("-------")
st.write("-------")
st.markdown("---")

# Membaca data dari Excel
try:
    # Membaca file excel bernama 'daftar_vocab.xlsx'
    df = pd.read_excel("daftar_vocab.xlsx")
    
    # Mengubah data dari Excel menjadi format list agar bisa looping seperti kemarin
    vocab_data = df.to_dict(orient="records")
    
    # Menampilkan Vocab dalam bentuk Expander (Square Dropdown)
    for item in vocab_data:
        # Menampilkan nama vocab dan POS (Part of Speech)
        with st.expander(f"{item['Vocab']} ({item['Pos']})"):
            st.markdown(f"**Arti:**")
            st.write(item['Arti'])
            
            st.markdown(f"**Contoh Kalimat:**")
            st.info(f"\"{item['Contoh']}\"")

except FileNotFoundError:
    st.error("Aduh! File 'daftar_vocab.xlsx' tidak ditemukan di folder projek. Pastikan file Excel sudah ditaruh di folder yang sama dengan app.py ya!")
except Exception as e:
    st.error(f"Terjadi kesalahan saat membaca file Excel: {e}")