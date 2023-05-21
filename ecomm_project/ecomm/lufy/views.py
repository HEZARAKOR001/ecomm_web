from django.shortcuts import render
import os
from wantedposter.wantedposter import WantedPoster
from PIL import Image
# Create your views here.
def home(request):
    return render(request,"home.html")


def generate_poster(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        bounty_amount = request.POST.get('bounty_amount')

        path = WantedPoster(first_name, last_name, bounty_amount)

        return render(request, 'poster.html', {'poster_path': path})

    return render(request, 'generate_poster.html')
    