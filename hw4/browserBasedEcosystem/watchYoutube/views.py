from django.shortcuts import render
from django.http import HttpResponse
import application.customExceptions as cExc

# Create your views here.
def syncYoutubePlayerPageLoader(request):
    try:
        if request.method != 'GET':
            raise cExc.HttpMethodIsNotSupported

        return render(request, 'syncYoutubePlayer.html',
                      {"video_id": request.GET.get('v')})
    except cExc.HttpMethodIsNotSupported:
        return HttpResponse(status=405)
