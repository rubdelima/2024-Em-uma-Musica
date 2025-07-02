import streamlit as st

from app.utils import (
    load_data, music_containter, download_model,
    filter_and_sort_musics, load_custom_font
)

from app.text import main_text

ONLY_MUSIC = True

st.set_page_config(page_title="2024 em Uma Música", page_icon=":musical_note:", layout="centered")
load_custom_font()

def main():
    musics = load_data()

    st.title("2024 em Uma Música")
    
    _1, col, _2 = st.columns([1, 3, 1])
    col.image("./assets/images/cover.png", use_container_width=True)
    
    st.markdown(main_text, unsafe_allow_html=True)
    
    download_model()
    
    musics = filter_and_sort_musics(musics)
    
    for music in musics:
        music_containter(music, ONLY_MUSIC)

if __name__ == "__main__":
    main()