from django.shortcuts import render, redirect
import pytube
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from logger.models import Logger


@csrf_exempt
def download(request):
    if request.method == 'POST':
        link = request.POST['link']
        video = pytube.YouTube(link)
        stream = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        filename = video.title + str(timezone.now().timestamp()) + '.mp4'
        path = '../media/' + filename
        # stream.download()
        logger = Logger.objects.create(
            name=filename,
            path=path,
            link=link,
            status=Logger.Status.ERROR,
        )
        stream.download('../media/', filename=filename)
        logger.status = Logger.Status.SUCCESS
        logger.save()
        return render(request, 'index.html')
    return render(request, 'index.html')
