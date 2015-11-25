# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Article, Comment, Message, Category, Tag

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_date', 'published_date', )
    class Media:
        js = (
            '/static/js/tinymce/tinymce.min.js',
            '/static/js/tinymce/config.js',
        )
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Message)
admin.site.register(Category)
admin.site.register(Tag)