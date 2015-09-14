from django.conf.urls import url, include
from blog.views import*

urlpatterns = [url(r'^$', home,name = 'home'),
               url(r'^about/$',about,name = 'about'),
               url(r'^message/$',message,name = 'message'),
               url(r'^message/post/$',message_post,name = 'message_post'),
               url(r'^message/(?P<pk>[0-9]+)/delete/$', message_delete, name='message_delete'),
               url(r'^accounts/login/$', 'django.contrib.auth.views.login',name = 'login'),
               url(r'^accounts/logout/$','django.contrib.auth.views.logout',{'next_page':'/'},name = 'logout'),
               url(r'^article/(?P<pk>[0-9]+)/edit/$',article_edit,name = 'article_edit'),
               url(r'^article/(?P<pk>[0-9]+)/$',article_detail,name = 'article_detail'),
               url(r'^article/(?P<pk>[0-9]+)/remove/$',article_remove,name='article_remove'),
               url(r'^article/new/$',article_new,name='article_new'),
               url(r'^article/(?P<pk>[0-9]+)/publish/$',article_publish,name='article_publish'),
               url(r'^drafts/$',article_draft_list,name='article_draft_list'),
               url(r'^comment/post/$',comment_post,name='comment_post')


               ]