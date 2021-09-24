from django.shortcuts import redirect, render

def home(request):
    return render(request, 'web/home.html', locals())