import pytube as py


def download(url: str):
    yt = py.YouTube('https://www.youtube.com/watch?v=5uV4IMkokGk')
    print(yt.streams.filter(mime_type= 'audio/webm', abr= '160kbps'))
    stream = yt.streams.get_by_itag('251')
    stream.download(filename= 'audio.webm', timeout= None)