from django.shortcuts import render, get_object_or_404

from .models import Informatika
from .forms import InformatikaForm

from taggit.models import Tag
from django.template.defaultfilters import slugify


def home_view_informatika(request):
    informatikas = Informatika.objects.all()
    common_tags = Informatika.tags.most_common()[:4]
    form = InformatikaForm(request.POST)
    if form.is_valid():
        newinformatika = form.save(commit=False)
        newinformatika.slug = slugify(newinformatika.title)
        newinformatika.save()
        form.save_m2m()
    context = {
        'informatikas':informatikas,
        'common_tags':common_tags,
        'form':form,
    }
    return render(request, 'home-informatika.html', context)

def upload_view_informatika(request):
    informatikas = Informatika.objects.all()
    common_tags = Informatika.tags.most_common()[:4]
    form = InformatikaForm(request.POST)
    if form.is_valid():
        newinformatika = form.save(commit=False)
        newinformatika.slug = slugify(newinformatika.title)
        newinformatika.save()
        form.save_m2m()
    context = {
        'informatikas':informatikas,
        'common_tags':common_tags,
        'form':form,
    }
    return render(request, 'upload-informatika.html', context)

def detail_view_informatika(request, slug):
    informatika = get_object_or_404(Informatika, slug=slug)
    context = {
        'informatika':informatika,
    }
    return render(request, 'detail-informatika.html', context)

def tagged_informatika(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = Informatika.tags.most_common()[:4]
    informatikas = Informatika.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'common_tags':common_tags,
        'informatikas':informatikas,
    }
    return render(request, 'home-informatika.html', context)