# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .speak import speak

def index(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            speak(text)
            return JsonResponse({'status': 'success'})
    return render(request, 'index.html')
