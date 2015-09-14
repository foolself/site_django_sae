from django.conf.urls import url
from blog import views

urlpatterns = [url(r'^$', views.home),
               url(r'^article/(?P<pk>[0-9]+)/edit/$',views.article_edit,name='article_edit'),
               ]