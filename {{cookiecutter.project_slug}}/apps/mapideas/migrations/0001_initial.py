# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-04 13:56
from __future__ import unicode_literals

import adhocracy4.categories.fields
import adhocracy4.images.fields
import adhocracy4.maps.fields
import autoslug.fields
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('a4categories', '0002_category_icon'),
        ('a4modules', '0004_description_maxlength_512'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapIdea',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='a4modules.Item')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('name', models.CharField(max_length=120)),
                ('description', ckeditor.fields.RichTextField()),
                ('image', adhocracy4.images.fields.ConfiguredImageField('idea_image', blank=True, upload_to='ideas/images')),
                ('point', adhocracy4.maps.fields.PointField(help_text='Click inside the marked area or type in an address to set the marker. A set marker can be dragged when pressed.', verbose_name='Where can your idea be located on a map?')),
                ('point_label', models.CharField(blank=True, default='', help_text='This could be an address or the name of a landmark.', max_length=255, verbose_name='Label of the ideas location')),
                ('category', adhocracy4.categories.fields.CategoryField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='a4categories.Category', verbose_name='Category')),
            ],
            options={
                'abstract': False,
            },
            bases=('a4modules.item',),
        ),
    ]
