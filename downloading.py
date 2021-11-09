import pytube as py

def download(url: str, name: str):
    yt = py.YouTube(url)
    print(yt.streams.filter(mime_type= 'audio/webm', abr= '160kbps'))
    stream = yt.streams.get_by_itag('251')
    stream.download(filename= f'{name}.webm', timeout= None)