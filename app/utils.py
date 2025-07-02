import streamlit as st
import json
from models.music import Music
import markdown

SHORT_SPOTIFY_BADGE = '''
<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/{track_id}?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
'''

LARGE_SPOTIFY_BADGE = """
<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/{track_id}?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
"""
@st.cache_data
def load_data():
    with open('musics.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return [Music(music_id=music_id, **music_data) for music_id, music_data in data.items()]

def audio_container(music: Music, only_music: bool = False):
    with st.container():
        st.markdown(f"### **{music.title}**")
        st.markdown(', '.join(music.artists))
        st.feedback(options="stars", key=f"feedback-{music.music_id}")
        geners_colums = st.columns(len(music.genres))
        for genre, col in zip(music.genres, geners_colums):
            with col:
                st.badge(genre, color="primary")
        
        st.markdown(
            (LARGE_SPOTIFY_BADGE if only_music else SHORT_SPOTIFY_BADGE).format(track_id=music.spotify), 
            unsafe_allow_html=True
        )
        st.audio(music.audio, autoplay=False)

def music_containter(music: Music, only_music: bool = False):
    with st.container():
        st.divider()
        if only_music:
            audio_container(music, only_music)
        else:
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
                audio_container(music, only_music)
            
    
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

def filter_and_sort_musics(musics: list[Music]):
    with st.sidebar:
        all_genres = set()
        for music in musics:
            all_genres.update(music.genres)

        all_artists = set()
        for music in musics:
            all_artists.update(music.artists)

        # Filtro por texto
        search_text = st.text_input("Buscar por título ou artista", placeholder="Digite para buscar...")

        # Filtros por gênero e artista
        selected_genres = st.multiselect("Filtrar por Gêneros", options=list(all_genres), default=list(all_genres))
        selected_artists = st.multiselect("Filtrar por Artistas", options=list(all_artists), default=list(all_artists))

        # Opções de ordenamento
        sort_options = {
            "Artista e Título": ("artists", "title"),
            "Título": ("title",),
            "Artista": ("artists",)
        }
        selected_sort = st.selectbox("Ordenar por", options=list(sort_options.keys()), index=0)

        # Aplicar filtros
        filtered_musics = []
        for music in musics:
            # Filtro por gênero e artista
            if not (set(music.genres).intersection(selected_genres) and 
                    set(music.artists).intersection(selected_artists)):
                continue
            
            # Filtro por texto (case insensitive)
            if search_text:
                search_lower = search_text.lower()
                title_match = search_lower in music.title.lower()
                artist_match = any(search_lower in artist.lower() for artist in music.artists)

                if not (title_match or artist_match):
                    continue
                
            filtered_musics.append(music)

        # Aplicar ordenamento
        sort_keys = sort_options[selected_sort]

        def sort_key(music):
            result = []
            for key in sort_keys:
                if key == "artists":
                    # Ordena pelo primeiro artista (case insensitive)
                    result.append(music.artists[0].lower() if music.artists else "")
                elif key == "title":
                    result.append(music.title.lower())
            return tuple(result)

        filtered_musics.sort(key=sort_key)

        return filtered_musics
    
import streamlit as st

# Função para carregar e injetar o CSS com a fonte do Google Fonts
def load_custom_font():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');
            
            /* Aplica a fonte a todos os elementos de texto do Streamlit */
            html, body, [class*="st-"], .stHeading, .stTitle, .stMarkdown, .stButton>button {
                font-family: 'Bebas Neue', sans-serif;
            }

            /* Você pode também criar classes específicas para títulos */
            .custom-title {
                font-family: 'Bebas Neue', sans-serif;
                font-size: 60px; /* Ajuste o tamanho como desejar */
                font-weight: bold;
                color: #FFFFFF; /* Cor do texto */
                text-shadow: 2px 2px 4px #000000; /* Sombra para dar profundidade */
            }
        </style>
    """, unsafe_allow_html=True)