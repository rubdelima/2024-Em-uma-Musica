import streamlit as st

from app.text import (
    introduction_text,
    music_generation_p1, music_generation_p1_items,
    music_generation_p2, music_generation_p2_items,
    music_generation_p3, music_generation_p3_items, music_generation_p4
)

st.set_page_config(page_title="Relatório", page_icon="📊")

def display_audio_items(items):
    items_cols = st.columns(len(items))
    for col, item in zip(items_cols, items):
        with col:
            st.markdown(f"**{item['title']}**")
            st.badge(item['tag'], color="primary")
            st.audio(item['audio'])

st.title("Relatório de Grupo 11 - 2024 em Uma Música")
# Ponham aqui a Introdução

# 2 Geração/Alteração de Voz
st.title("2 Geração de Músicas")

# 2.1 Geração/Alteração de Voz
st.markdown(music_generation_p1)
p1_cols = st.columns(len(music_generation_p1_items))
display_audio_items(music_generation_p1_items)
st.markdown(music_generation_p2)
display_audio_items(music_generation_p2_items)

# 2.2 Geração de Melodia
st.markdown(music_generation_p3)
display_audio_items(music_generation_p3_items)
st.markdown(music_generation_p4)

# Ponham aqui a parte de geração de vídeos
    
