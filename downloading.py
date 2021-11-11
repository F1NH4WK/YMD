import pytube as py
from pytube.cli import on_progress

def download(url: str, name: str):
    yt = py.YouTube(url, on_progress_callback = on_progress)
    stream = yt.streams.get_by_itag('251')
    stream.download(filename= f'{name}.mp3', timeout = None)