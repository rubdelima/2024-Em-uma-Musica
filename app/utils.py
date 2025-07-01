import streamlit as st
import json
from models.music import Music

@st.cache_data
def load_data():
    with open('musics.json', 'r') as file:
        data = json.load(file)
    return [Music(music_id=music_id, **music_data) for music_id, music_data in data.items()]

def music_containter(music: Music):
    with st.container():
        st.divider()
        
        music_colums = st.columns(2)
        
        with music_colums[0]:
            image_tab, video_tab = st.tabs(["Capa", "Video"])
            with image_tab:
                if music.image:
                    st.image(music.image, use_container_width=True)
                else:
                    st.warning("Imagem não disponível")
            with video_tab:
                if music.video:
                    st.video(music.video, loop=True)
                else:
                    st.warning("Vídeo não disponível")

        with music_colums[1]:
            st.markdown(f"### **{music.title}**")
            st.markdown(', '.join(music.artists))
            st.feedback(options="stars", key=f"feedback-{music.music_id}")
            geners_colums = st.columns(len(music.genres))
            for genre, col in zip(music.genres, geners_colums):
                with col:
                    st.badge(genre, color="primary")
            
            st.markdown(f'''
                    <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/{music.spotify}?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
                    ''', unsafe_allow_html=True)
            
            st.audio(music.audio, autoplay=False)
    
def download_model():
    st.subheader("Utilize o modelo de voz!")
    col_down1, col_down2 = st.columns(2)
    with col_down1:
        st.download_button(
            label="Baixar Modelo de Voz",
            data=open("assets/models/model.pth", "rb").read(),
            file_name="model.pth",
        )
    with col_down2:
        st.download_button(
            label="Baixar Modelo de Voz (Indices)",
            data=open("assets/models/index.index", "rb").read(),
            file_name="model.index",
        )

def filter_and_sort_musics(musics : list[Music]):
    all_genres = set()
    for music in musics:
        all_genres.update(music.genres)
    
    all_artists = set()
    for music in musics:
        all_artists.update(music.artists)
    
    selected_genres = st.multiselect("Filtrar por Gêneros", options=list(all_genres), default=list(all_genres))
    selected_artists = st.multiselect("Filtrar por Artistas", options=list(all_artists), default=list(all_artists))

    filtered_musics = [
        music for music in musics
        if set(music.genres).intersection(selected_genres) and set(music.artists).intersection(selected_artists)
    ]

    return filtered_musics