from django.shortcuts import render
from .models import Slider

def slider_view(request):
    sliders = Slider.objects.all()
    return render(request, 'index.html', {'slides': sliders})
