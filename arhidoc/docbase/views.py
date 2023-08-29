import os
from django.http import HttpResponse, Http404
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator

from .models import Doc, Category
from .forms import DocumentForm


def index(request):
    documents = Doc.objects.order_by("-pub_create")
    paginator = Paginator(documents, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "docbase/list.html", {"page_obj": page_obj})

def category(request):
    category = Category.objects.all()
    return render(request, "docbase/category.html", {"page_obj": category})

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

