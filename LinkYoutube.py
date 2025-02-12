from yt_dlp import YoutubeDL

video_url = input("Digite o link do vídeo do YouTube: ")
ydl_opts = {}
with YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])