from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='tag_name')

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='category_name')
    index = models.IntegerField(default=999,verbose_name='category_index')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __unicode__(self):
        return self.name

class Article(models.Model):
    author=models.ForeignKey(User)
    title=models.CharField(max_length=200)
    imageURL = models.CharField(max_length=200,blank=True)
    text=models.TextField()
    created_date=models.DateField(default=timezone.now)
    published_date=models.DateField(blank=True,null=True)
    like_count = models.IntegerField(blank=True,null=True)
    view_count = models.IntegerField(blank=True,null=True)
    comment_count = models.IntegerField(blank=True,null=True)
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name='Category')
    tag = models.ManyToManyField(Tag, verbose_name='Tag')

    def publish(self):
        self.published_date=timezone.now()
        self.save()
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = verbose_name

class Comment(models.Model):
    content = models.TextField(verbose_name='Content')
    username = models.CharField(max_length=30, blank=True, null=True, verbose_name='Name')
    email = models.EmailField(max_length=50, blank=True, null=True, verbose_name='Email')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='PublishTime')
    user = models.ForeignKey(User, blank=True, null=True, verbose_name='User')
    article = models.ForeignKey(Article, blank=True, null=False, verbose_name='Article')
    pid = models.ForeignKey('self', blank=True, null=True, verbose_name='PComment')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.article.title + "--" + self.username

class Message(models.Model):
    content = models.TextField(verbose_name='content')
    name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Name')
    date = models.DateField(default=timezone.now)


class ad(models.Model):
    pass

