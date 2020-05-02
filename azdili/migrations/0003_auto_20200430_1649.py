# Generated by Django 3.0.5 on 2020-04-30 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azdili', '0002_auto_20200430_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='azdili',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='icon/azdili', verbose_name='Icon'),
        ),
        migrations.AlterField(
            model_name='azdili',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='cover/azdili', verbose_name='Cover'),
        ),
        migrations.AlterField(
            model_name='azdili',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='file/azdili', verbose_name='Archive'),
        ),
    ]