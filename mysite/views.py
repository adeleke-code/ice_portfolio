from django.shortcuts import render
from django.http.response  import HttpResponse


def home(request):
    data = {
        "page": "home"
    }
    return render(request, "home.html", data)

def about(request):
    data = {
        "page": "about"
    }
    return render(request, "about.html", data)


def services(request):
    context = {
        "page": "services"
    }
    return render(request, "services.html", context)


def acheivements(request):
    context = {
        "page": "acheivements"
    }
    return render(request, "acheivements.html", context)


def skills(request):
    context = {
        "page": "skills"
    }
    return render(request, "skills.html", context)