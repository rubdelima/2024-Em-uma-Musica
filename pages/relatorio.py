import streamlit as st
import dotenv

RAW_GITHUB_URL = dotenv.get_key(".env", "RAW_GITHUB_URL")
ONLINE_MODE = dotenv.get_key(".env", "ONLINE_MODE") == "True"

from app.text import (
    introduction_text,
    music_generation_p1, music_generation_p1_items,
    music_generation_p2, music_generation_p2_items,
    music_generation_p3, music_generation_p3_items, music_generation_p4
)

from app.video_text import (
    main_text,
    first_approach,
    second_approach,
    third_approach,
    generated_videos,
    tries_text,
    generated_tries,
)

st.set_page_config(page_title="Relatório", page_icon="📊")

def display_audio_items(items, max_items_columns=None):
    if max_items_columns:
        items_chunks = [items[i:i + max_items_columns] for i in range(0, len(items), max_items_columns)]
    else:
        items_chunks = [items]

    for items in items_chunks:
        items_cols = st.columns(len(items))
        for col, item in zip(items_cols, items):
            with col:
                st.markdown(f"**{item['title']}**")
                st.badge(item['tag'], color="primary")
                st.audio(item['audio']if not ONLINE_MODE
                         else f"{RAW_GITHUB_URL}/audios/{item['audio'].split('/')[-1].replace(' ', '%20')}",
                         autoplay=False)

def display_video_items(items):
    for video in items:
        st.markdown(f"### {video['title']}")
        st.caption(video["tag"])
        st.video(video["video"] if not ONLINE_MODE
                  else f"{RAW_GITHUB_URL}/videos/{video['video'].split('/')[-1].replace(' ', '%20')}",
                  loop=False)
        st.divider()


st.title("Relatório do Grupo 11 - 2024 em Uma Música")

# 1 Intro
st.markdown(introduction_text)

# 2 Geração/Alteração de Voz
st.title("2 Geração de Músicas")

# 2.1 Geração/Alteração de Voz
st.markdown(music_generation_p1)
p1_cols = st.columns(len(music_generation_p1_items))
display_audio_items(music_generation_p1_items, max_items_columns=2)
st.markdown(music_generation_p2)
display_audio_items(music_generation_p2_items, max_items_columns=2)

# 2.2 Geração de Melodia
st.markdown(music_generation_p3)
display_audio_items(music_generation_p3_items)
st.markdown(music_generation_p4)

# 3 Geração de vídeos a partir das músicas geradas
st.title("3 Geração de Vídeos")
st.markdown(main_text)
st.markdown(first_approach)
st.markdown(second_approach)
st.markdown(third_approach)

display_video_items(generated_videos)

st.markdown(tries_text)
st.divider()

display_video_items(generated_tries)