import pytube


def download(request):
    link = request
    video = pytube.YouTube(link)
    stream = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    stream.download()


link = input('link')
download(link)
print('done')
