# Generated by Django 3.2 on 2022-11-28 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('content_image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('content_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_alt_text', models.CharField(blank=True, default='aden wellness theme image', max_length=200)),
                ('header', models.CharField(blank=True, max_length=200)),
                ('text_background', models.IntegerField(choices=[(1, 'No background'), (2, 'Put background')], default=1)),
                ('excerpt', models.TextField(blank=True)),
                ('carousel_block', models.IntegerField(choices=[(1, 'First block'), (2, 'Second block'), (3, 'Third block')], default=1)),
                ('image_place', models.IntegerField(choices=[(1, 'Image-as-background'), (2, 'Image-on-side')], default=1)),
                ('image_order', models.IntegerField(default=1)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
            ],
            options={
                'ordering': ['image_order'],
            },
        ),
        migrations.CreateModel(
            name='HomeMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_name', models.CharField(max_length=200, unique=True)),
                ('media_id', models.IntegerField(choices=[(0, 'Not used'), (1, 'First image'), (2, 'Second image'), (3, 'Third image')], default=0)),
                ('media_image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('media_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('media_image_alt_text', models.CharField(blank=True, default='aden image', max_length=200)),
                ('media_text', models.TextField(blank=True)),
            ],
        ),
    ]
