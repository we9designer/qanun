from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Material(models.Model):
    # user = models.ForeignKey(User, verbose_name='User', related_name='users', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250)
    description = RichTextField('Description', null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=250)
    tags = TaggableManager()
    created_at = models.DateTimeField('Created on', auto_now_add=True)
    update_at = models.DateTimeField('Updated', auto_now_add=True)
    file = models.FileField('Archive', upload_to='file/materials', null=True, blank=True)
    cover = models.ImageField('Cover', upload_to='cover/materials', null=True, blank=True)
    icon = models.ImageField('Icon', upload_to='icon/materials', null=True, blank=True)

    def __str__(self):
        return self.title
