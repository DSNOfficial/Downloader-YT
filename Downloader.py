import pytube

link = "https://www.youtube.com/watch?v=29-fw1FPx7E&list=RDaALAnlrz2A8&index=28"
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download()
