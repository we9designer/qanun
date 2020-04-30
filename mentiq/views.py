from django.shortcuts import render, get_object_or_404

from .models import Mentiq
from .forms import MentiqForm

from taggit.models import Tag
from django.template.defaultfilters import slugify


def home_view_mentiq(request):
    mentiqs = Mentiq.objects.all()
    common_tags = Mentiq.tags.most_common()[:4]
    form = MentiqForm(request.POST)
    if form.is_valid():
        mentiq = form.save(commit=False)
        mentiq.slug = slugify(mentiq.title)
        mentiq.save()
        form.save_m2m()
    context = {
        'mentiqs':mentiqs,
        'common_tags':common_tags,
        'form':form,
    }
    return render(request, 'home-mentiq.html', context)

def upload_view_mentiq(request):
    mentiqs = Mentiq.objects.all()
    common_tags = Mentiq.tags.most_common()[:4]
    form = MentiqForm(request.POST)
    if form.is_valid():
        newmentiq = form.save(commit=False)
        newmentiq.slug = slugify(newmentiq.title)
        newmentiq.save()
        form.save_m2m()
    context = {
        'mentiqs':mentiqs,
        'common_tags':common_tags,
        'form':form,
    }
    return render(request, 'upload-mentiq.html', context)

def detail_view_mentiq(request, slug):
    mentiq = get_object_or_404(Mentiq, slug=slug)
    context = {
        'mentiq':mentiq,
    }
    return render(request, 'detail-mentiq.html', context)

def tagged_mentiq(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = Mentiq.tags.most_common()[:4]
    mentiqs = Mentiq.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'common_tags':common_tags,
        'mentiqs':mentiqs,
    }
    return render(request, 'home-mentiq.html', context)