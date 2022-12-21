from django.shortcuts import render


def index(request):
    data = {"title": "Voices of Hope"}
    return render(request, "pages/main.html", context=data)


def links(request):
    data = {"title": "Links of Hope"}
    return render(request, "pages/links.html", context=data)


def help_us(request):
    data = {"title": "Help Us"}
    return render(request, "pages/help-us.html", context=data)
