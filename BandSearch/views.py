from django.shortcuts import render


# Create your views here.


def band_search(request):
    return render(request, 'base.html')