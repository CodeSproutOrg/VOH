from django.shortcuts import render


def index(request):
    data = {"title": "Voices of Hope"}
    return render(request, "base.html", context=data)
