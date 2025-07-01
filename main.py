import streamlit as st

from app.utils import (
    load_data, music_containter, download_model,
    filter_and_sort_musics
)

from app.text import main_text

st.set_page_config(page_title="2024 em Uma Música", page_icon=":musical_note:", layout="wide")

def main():
    musics = load_data()
    
    img_col, info_col = st.columns(2)
    
    with info_col:
        st.title("2024 em Uma Música")
        st.markdown(main_text)
        download_model()
    
    musics = filter_and_sort_musics(musics)
    
    for music in musics:
        music_containter(music)

if __name__ == "__main__":
    main()