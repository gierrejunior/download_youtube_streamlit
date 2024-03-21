# youtube_downloader.py

import os
from pytube import YouTube
from moviepy.editor import *

class YouTubeDownloader:
    def __init__(self, url, qualidade='highest'):
        self.url = url
        self.qualidade = qualidade
        self.youtube = YouTube(url)
        self.video = None
        self.caminho_video = None

    def baixar_video(self):
        if not os.path.exists('mp4/'):
            os.makedirs('mp4/')
        if self.qualidade == 'highest':
            self.video = self.youtube.streams.get_highest_resolution()
        elif self.qualidade == 'lowest':
            self.video = self.youtube.streams.get_lowest_resolution()
        elif self.qualidade == 'medium':
            streams = self.youtube.streams.filter(
                progressive=True, file_extension='mp4')
            streams = sorted(streams, key=lambda s: s.resolution)
            mid_index = len(streams) // 2
            self.video = streams[mid_index]
        else:
            self.video = self.youtube.streams.get_highest_resolution()
        self.caminho_video = f'mp4/{self.youtube.title}.mp4'
        self.video.download(filename=self.caminho_video)

    def converter_video_para_mp3(self):
        if not os.path.exists('mp3/'):
            os.makedirs('mp3/')
        clip = VideoFileClip(self.caminho_video)
        caminho_audio = f'mp3/{self.youtube.title}.mp3'
        clip.audio.write_audiofile(caminho_audio)
        return caminho_audio

    def excluir_video(self):
        os.remove(self.caminho_video)
