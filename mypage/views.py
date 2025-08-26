from django.shortcuts import render

def home(request):
    return render(request, 'homepage.html', {'current_page': 'home'})

def about(request):
    return render(request, 'about.html', {'current_page': 'about'})

def services(request):
    return render(request, 'services.html', {'current_page': 'services'})