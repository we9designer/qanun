from django.shortcuts import render, get_object_or_404

from .models import Azdili
from .forms import AzdiliForm

from taggit.models import Tag
from django.template.defaultfilters import slugify


def home_view_azdili(request):
    azdilis = Azdili.objects.all()
    common_tags = Azdili.tags.most_common()[:4]
    form = AzdiliForm(request.POST)
    if form.is_valid():
        azdili = form.save(commit=False)
        azdili.slug = slugify(azdili.title)
        azdili.save()
        form.save_m2m()
    context = {
        'azdilis':azdilis,
        'common_tags':common_tags,
        'form':form,
    }
    return render(request, 'home-azdili.html', context)

def upload_view_azdili(request):
    azdilis = Azdili.objects.all()
    common_tags = Azdili.tags.most_common()[:4]
    form = AzdiliForm(request.POST)
    if form.is_valid():
        newazdili = form.save(commit=False)
        newazdili.slug = slugify(newazdili.title)
        newazdili.save()
        form.save_m2m()
    context = {
        'azdilis':azdilis,
        'common_tags':common_tags,
        'form':form,
    }
    return render(request, 'upload-azdili.html', context)

def detail_view_azdili(request, slug):
    azdili = get_object_or_404(Azdili, slug=slug)
    context = {
        'azdili':azdili,
    }
    return render(request, 'detail-azdili.html', context)

def tagged_azdili(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = Azdili.tags.most_common()[:4]
    azdilis = Azdili.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'common_tags':common_tags,
        'azdilis':azdilis,
    }
    return render(request, 'home-azdili.html', context)