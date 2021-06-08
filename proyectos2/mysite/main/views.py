from django.shortcuts import render
from django.http import HttpResponse
from main.models import Curso

# Create your views here.

def homepage(request):

    return render(request, "main/inicio.html", {"Curso":Curso.objects.all})
