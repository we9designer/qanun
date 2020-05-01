# Generated by Django 3.0.5 on 2020-04-30 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informatika', '0002_auto_20200430_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='informatika',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='icon/informatika', verbose_name='Icon'),
        ),
        migrations.AlterField(
            model_name='informatika',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='cover/informatika', verbose_name='Cover'),
        ),
        migrations.AlterField(
            model_name='informatika',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='file/informatika', verbose_name='Archive'),
        ),
    ]
