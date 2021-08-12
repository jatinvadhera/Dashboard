from django.shortcuts import render


# Create your views here.


def index(request):
    ustop5 = [{'Ohio':25000}, {'California':40000}, {'Texas':15000}, {'Florida':45000},{'New Jersey':13000}]
    context = {'ustop5':ustop5}
    return render(request, 'index.html', context)
