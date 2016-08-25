# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.mail import send_mail
from django import forms

#notify = False

class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to = 'blog/static/fotos', default = 'blog/static/fotos/index.png')
    imagen = models.ImageField(upload_to = 'blog/static/fotos', default = 'blog/static/fotos/cambio.jpeg')
    nombre_imagen = models.CharField(max_length=80, default= 'juan.png')
    url_post=models.CharField(max_length=60, null=True,blank=True)
    
    def __str__(self):
        return self.title




### Admin

class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    display_fields = ["title", "created","categorias","nombre_imagen","imagen",]
    
#NO IMPLEMENTADO    
class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.body[:60]))
