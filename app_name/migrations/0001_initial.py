# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 20:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(blank=True, default=0, null=True)),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('comment', models.CharField(blank=True, max_length=300, null=True)),
                ('price', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(blank=True, default=0, null=True)),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_name.FoodCategory'),
        ),
        migrations.AddField(
            model_name='food',
            name='ingredients',
            field=models.ManyToManyField(blank=True, null=True, to='app_name.Ingredient'),
        ),
    ]
