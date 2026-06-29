from django.shortcuts import render, get_object_or_404
from .models import Anime

def home(request):
    animes = Anime.objects.all()

    q = request.GET.get("q")

    if q:
        animes = animes.filter(name__icontains=q)

    return render(request,"home.html",{
        "animes":animes,
        "count":animes.count(),
        "query":q,
    })


def anime_detail(request,id):
    anime = get_object_or_404(Anime,id=id)
    return render(request,"detail.html",{
        "anime":anime
    })
