# Generated by Django 3.2.9 on 2021-12-07 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dancer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag_set',
            field=models.ManyToManyField(blank=True, to='dancer.Tag'),
        ),
    ]
