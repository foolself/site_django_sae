#-*- coding=utf-8 -*-
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
               url(r'^comment/post/$',comment_post,name='comment_post'),
               url(r'^category/$', category, name='category'),
               url(r'^archive/$', archive, name='archive'),
               url(r'^tag/$', tag, name='tag'),
               url(r'^search/$',search,name='search'),

                #url(r'^login/$', login, name='login'),                           # 登陆
                url(r'^login/weibo/$', weiboLogin, name='weiboLogin'),            # 登陆
                #url(r'^logout/$', 'logout', name='logout'),                        # 登出
                url(r'^login/weibo_check/$', weibo_check, name='weibo_check'),     # 微博回调地址
                #url(r'^register/$', 'register', name='register'),
               #url(r'^codetheme/get_user_info/$', 'get_user_info', name='get_user_info'),
                #url(r'^user_info/$',user_info,name='user_info')
               ]