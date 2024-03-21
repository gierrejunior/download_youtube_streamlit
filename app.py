# app.py

import os
import glob
from youtube_downloader import YouTubeDownloader
import streamlit as st

# Apagar todos os arquivos nas pastas 'mp3/' e 'mp4/'
files = glob.glob('mp3/*')
for f in files:
    os.remove(f)
files = glob.glob('mp4/*')
for f in files:
    os.remove(f)

st.title('YouTube Video Downloader')

url = st.text_input('Digite a URL do vídeo do YouTube que você deseja baixar:')
qualidade = st.selectbox('Selecione a qualidade do vídeo:', [
                         'highest', 'lowest', 'medium'])
tipo = st.selectbox(
    'Selecione o tipo de arquivo para baixar:', ['Vídeo', 'Áudio'])

if st.button('Gerar Download'):
    with st.spinner('Gerando download...'):
        downloader = YouTubeDownloader(url, qualidade)
        downloader.baixar_video()
        if tipo == 'Áudio':
            caminho_audio = downloader.converter_video_para_mp3()
            downloader.excluir_video()
            st.download_button(
                label="Download",
                data=open(caminho_audio, 'rb'),
                file_name=f'{downloader.youtube.title}.mp3',
                mime='audio/mpeg'
            )
        else:
            st.download_button(
                label="Download",
                data=open(downloader.caminho_video, 'rb'),
                file_name=f'{downloader.youtube.title}.mp4',
                mime='video/mp4'
            )
    st.success('Download gerado!')
