import streamlit as str

# Pengaturan halaman
st.set_page_config(
    page_title="British Vocab Builder",
    page_icon="🇬🇧",
    layout="centered"
)

# Judul Aplikasi
st.title("🇬🇧 British Vocabulary Builder")
st.write("Klik pada kotak kosakata untuk melihat arti dan cara penggunaannya.")
st.markdown("---")

# Data Kosakata (Bisa Kamu tambah sendiri ke depannya)
vocab_data = [
    {
        "vocab": "Keen",
        "pos": "adjective",
        "arti": "Sangat tertarik, bersemangat, atau tajam secara intelektual.",
        "contoh": "He's very keen on learning classical piano."
    },
    {
        "vocab": "Daft",
        "pos": "adjective",
        "arti": "Silly; agak konyol atau bodoh tapi dalam konteks yang jenaka/ringan.",
        "contoh": "Don't be daft, of course you can pass the exam!"
    },
    {
        "vocab": "A bit of alright",
        "pos": "idiom",
        "arti": "Ungkapan kolokial untuk sesuatu atau seseorang yang sangat menarik atau memuaskan.",
        "contoh": "That new suit you wore to the presentation is a bit of alright!"
    }
]

# Menampilkan Vocab dalam bentuk Expander (Square Dropdown)
for item in vocab_data:
    # st.expander akan membuat kotak yang bisa diklik
    with st.expander(f"✨ {item['vocab']} ({item['pos']})"):
        st.markdown(f"**Arti:**")
        st.write(item['arti'])
        
        st.markdown(f"**Contoh Kalimat:**")
        st.info(f"\"{item['contoh']}\"")