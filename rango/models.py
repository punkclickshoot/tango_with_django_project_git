from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

    def __str__(self):      #For Python 2, use __str__ on Python 3
        return self.title

