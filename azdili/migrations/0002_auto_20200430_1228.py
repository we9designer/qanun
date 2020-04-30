# Generated by Django 3.0.5 on 2020-04-30 12:28

import ckeditor.fields
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('azdili', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Azdili',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Description')),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('update_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated')),
                ('file', models.FileField(blank=True, null=True, upload_to='upload/file/azdili', verbose_name='Archive')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='upload/cover/azdili', verbose_name='Cover')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.DeleteModel(
            name='Informatika',
        ),
    ]
