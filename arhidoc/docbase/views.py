import os
from django.http import HttpResponse, Http404
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from .models import Doc
from .forms import DocumentForm


def index(request):
    template = "docbase/index.html"
    title = "Документы"
    docs = Doc.objects.order_by("-pub_create")
    context = {"title": title, "text": docs}
    return render(request, template, context)


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('docbase:main')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })


def download(request, path):
    print(file_path)
    file_path = os.path.join('', path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(
                fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + \
                os.path.basename(file_path)
            return response
    raise Http404
