# Generated by Django 3.2.9 on 2021-12-10 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
            options={
                'verbose_name': '태그',
                'verbose_name_plural': '태그 목록',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('option', models.TextField()),
                ('cost', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to='car/shop/%Y/%m/%d')),
                ('tag_set', models.ManyToManyField(blank=True, to='car.Tag')),
            ],
            options={
                'verbose_name': '차',
                'verbose_name_plural': '차 모델 목록',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author_name', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.shop')),
            ],
            options={
                'verbose_name': '댓글',
                'verbose_name_plural': '댓글 목록',
            },
        ),
    ]
