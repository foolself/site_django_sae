from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Article(models.Model):
	author=models.ForeignKey(User)
	title=models.CharField(max_length=200)
	text=models.TextField()
	created_date=models.DateTimeField(default=timezone.now)
	published_date=models.DateTimeField(blank=True,null=True)
	def publish(self):
		self.published_date=timezone.now()
		self.save()
	class Meta:
		verbose_name = 'Article'
		verbose_name_plural = verbose_name

class ad(models.Model):
    pass

