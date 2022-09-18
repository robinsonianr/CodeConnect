from django.shortcuts import render
from django.core.serializers import serialize
from django.http import JsonResponse
from .models import Car

# Create your views here.

def getCars(request):
    cars = Car.objects.all()
    response_object = {"data": serialize("json", cars)}
    return JsonResponse(response_object)



def home(request):
    return render(request, "Home.html")