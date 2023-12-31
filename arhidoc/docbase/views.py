import os
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.conf import settings

from .models import Doc, Category
from .forms import DocForm, SearcheForm


def index(request):
    documents = Doc.objects.order_by("-date_created")
    count = documents.count()
    paginator = Paginator(documents, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request, "docbase/list.html", {"page_obj": page_obj, "count": count}
    )


def all_category(request):
    category = Category.objects.all()
    return render(request, "docbase/category.html", {"page_obj": category})


def docs_category(request, pk):
    documents = Doc.objects.filter(category=pk).order_by("-date_created")
    count = documents.count()
    paginator = Paginator(documents, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request, "docbase/list.html", {"page_obj": page_obj, "count": count}
    )


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, "rb") as fh:
            response = HttpResponse(
                fh.read(),
                content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )
            response[
                "Content-Disposition"
            ] = "inline; filename=" + os.path.basename(file_path)
            return response
    raise Http404


def searche(request):
    if request.method == "POST":
        form = DocForm(request.POST, request.FILES)
        validate_data = form.data
        name = validate_data["name"].strip()
        number = validate_data["number"].strip().upper()
        data_doc = validate_data["data_doc"].strip()
        page_obj = (
            Doc.objects.filter(data_doc__contains=data_doc)
            .filter(name__contains=name)
            .filter(number__contains=number)
        )
        count = page_obj.count
        return render(
            request,
            "docbase/list.html",
            {"page_obj": page_obj, "count": count},
        )
    else:
        form = SearcheForm()
    return render(request, "core/searche.html", {"form": form})


def create_docs(request, pk):
    error = False
    if request.method == "POST":
        form = DocForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            counter = Category.objects.filter(id=pk).first().counter + 1
            Category.objects.filter(id=pk).update(counter=counter)
            return redirect("docbase:main")
        else:
            error = True
    else:
        counter = Category.objects.filter(id=pk).first().counter
        name = Category.objects.filter(id=pk).first().name
        if counter < 10:
            counter = "0" + str(counter)
        number = "{}-{}".format(counter, name)
        form = DocForm()
        form.fields["number"].initial = number
        form.fields["category"].initial = Category.objects.filter(
            id=pk
        ).first()
    return render(
        request,
        "core/model_form_upload.html",
        {"form": form, "error": error},
    )


def model_form_upload(request):
    if request.method == "POST":
        form = DocForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("docbase:main")
    else:
        form = DocForm()
    return render(request, "core/model_form_upload.html", {"form": form})
