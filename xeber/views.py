from django.shortcuts import render, get_object_or_404

from .models import Xeber
from .forms import XeberForm

from taggit.models import Tag
from django.template.defaultfilters import slugify


def home_view_xeber(request):
    xebers = Xeber.objects.all()
    common_tags = Xeber.tags.most_common()[:4]
    form = XeberForm(request.POST)
    if form.is_valid():
        xeber = form.save(commit=False)
        xeber.slug = slugify(xeber.title)
        xeber.save()
        form.save_m2m()
    context = {
        'xebers':xebers,
        'common_tags':common_tags,
        'form':form,
    }
    return render(request, 'xeberler.html', context)

def upload_view_xeber(request):
    xebers = Xeber.objects.all()
    common_tags = Xeber.tags.most_common()[:4]
    form = XeberForm(request.POST)
    if form.is_valid():
        newaxeber = form.save(commit=False)
        newaxeber.slug = slugify(newxeber.title)
        newaxeber.save()
        form.save_m2m()
    context = {
        'xebers':xebers,
        'common_tags':common_tags,
        'form':form,
    }
    return render(request, 'xeberler.html', context)

def detail_view_xeber(request, slug):
    xeber = get_object_or_404(Xeber, slug=slug)
    context = {
        'xeber':xeber,
    }
    return render(request, 'xeber.html', context)

def tagged_xeber(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = Xeber.tags.most_common()[:4]
    xeber = Xeber.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'common_tags':common_tags,
        'xebers':xeber,
    }
    return render(request, 'xeberler.html', context)