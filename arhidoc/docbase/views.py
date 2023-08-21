from django.shortcuts import render

from .models import Doc


def index(request):
    template = "docbase/index.html"
    title = "Документы"
    docs = Doc.objects.order_by("-pub_create")
    context = {"title": title, "text": docs}
    return render(request, template, context)
