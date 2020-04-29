from django.shortcuts import render, get_object_or_404

from .models import Material
from .forms import MaterialForm

from taggit.models import Tag
from django.template.defaultfilters import slugify


def home_view_material(request):
    materials = Material.objects.all()
    common_tags = Material.tags.most_common()[:4]
    form = MaterialForm(request.POST)
    if form.is_valid():
        newmaterial = form.save(commit=False)
        newmaterial.slug = slugify(newmaterial.title)
        newmaterial.save()
        form.save_m2m()
    context = {
        'materials':materials,
        'common_tags':common_tags,
        'form':form,
    }
    return render(request, 'home.html', context)

def upload_view_material(request):
    materials = Material.objects.all()
    common_tags = Material.tags.most_common()[:4]
    form = MaterialForm(request.POST)
    if form.is_valid():
        newmaterial = form.save(commit=False)
        newmaterial.slug = slugify(newmaterial.title)
        newmaterial.save()
        form.save_m2m()
    context = {
        'materials':materials,
        'common_tags':common_tags,
        'form':form,
    }
    return render(request, 'upload.html', context)

def detail_view_material(request, slug):
    material = get_object_or_404(Material, slug=slug)
    context = {
        'material':material,
    }
    return render(request, 'detail.html', context)

def tagged_material(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = Material.tags.most_common()[:4]
    materials = Material.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'common_tags':common_tags,
        'materials':materials,
    }
    return render(request, 'home.html', context)

def landing(request):
    context = {
    }
    return render(request, 'landing.html', context)    