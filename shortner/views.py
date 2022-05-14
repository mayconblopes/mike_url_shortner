from django.http import HttpResponse
from django.shortcuts import render, redirect
import uuid
from .models import Url

def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        # return render(request, 'index.html', {'new_url': f'https://secret-ocean-97039.herokuapp.com/{new_url.uuid}'})
        return render(request, 'index.html', {'new_url': new_url.uuid})


def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)
