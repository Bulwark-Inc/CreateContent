from django.shortcuts import render

def home(request):
    return render(request, 'website/home.html')

def chat(request):
    return render(request, 'website/chat.html')

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')
