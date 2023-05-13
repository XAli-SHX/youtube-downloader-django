from django.shortcuts import render, redirect
import pytube
from django.utils import timezone


def download(request):
    if request.method == 'POST':
        link = request.POST['link']
        video = pytube.YouTube(link)
        stream = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        filename = video.title + timezone.now().timestamp() + '.mp4'
        stream.download()
        # stream.download('./media/', filename=filename)
        return render(request, 'index.html')
    return render(request, 'index.html')
