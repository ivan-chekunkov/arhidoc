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
    count = documents.count()
    paginator = Paginator(documents, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "docbase/list.html", {"page_obj": page_obj, "count": count})


def all_category(request):
    category = Category.objects.all()
    return render(request, "docbase/category.html", {"page_obj": category})


def docs_category(request, pk):
    documents = Doc.objects.filter(category=pk).order_by('-pub_create')
    count = documents.count()
    paginator = Paginator(documents, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "docbase/list.html", {"page_obj": page_obj, "count": count})


def create_docs(request, pk):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('docbase:main')
    else:
        form = DocumentForm()
        counter = Category.objects.filter(id=pk).first().counter
        name = Category.objects.filter(id=pk).first().name
        number = '{}-{}'.format(name, counter)
    return render(request, 'core/model_form_upload.html', {
        'form': form, 'number': number
    })


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
