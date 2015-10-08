# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from .models import Article, Comment, Message, Category, Tag
from .forms import ArticleForm, CommentForm, MessageForm
from django.contrib.auth.decorators import login_required
from weibo import APIClient
from django.db.models import Q
import urllib
import urllib2
from django.http import HttpResponse
from django.shortcuts import render_to_response

URL = 'http://foolselfblog.sinaapp.com'
APP_KEY = '3125712034' # app key
APP_SECRET = '75680bf3386cb5482df99fbbad467ea9' # app secret
CALLBACK_URL = 'http://www.foolselfblog.sinaapp.com/' # callback url
CALLBACK_URL = URL+'/login/weibo_check/'
USER_INFO_URL = 'https://api.weibo.com/2/users/show.json'

def my_custom_page_not_found_view(request):
    return render(request,'404.html')

def my_custom_error_view(request):
    return render(request,'500.html')

def global_setting(request):
    title = "foolself blog"
    category_list = Category.objects.all()[:6]
    archive_list = Article.objects.distinct_date()
    popular_article_list=Article.objects.filter(published_date__isnull=False).order_by('-view_count')[:3]
    tag_list = Tag.objects.all()
    #标签云中 设置标签字体的大小
    for tag in tag_list:
        tag.count = len(Article.objects.filter(tag=tag))
        if tag.count>30 :
            tag.count = 50
        else:
            tag.count = 20+tag.count*2
    return locals()

def home(request):
    article_list=Article.objects.filter(published_date__isnull=False).order_by('-pk')#'-published_date')
    return render(request,'index.html',{'article_list':article_list,})


def article_detail(request,pk):
    article=get_object_or_404(Article,pk=pk)
    comment_form = CommentForm({'name': request.user.username,
                                    'email': request.user.email,
                                    'article': article} if request.user.is_authenticated() else{'article': article})
    comments = Comment.objects.filter(article=article).order_by('id')
    comment_list = []
    for comment in comments:
        for item in comment_list:
            if not hasattr(item, 'children_comment'):
                setattr(item, 'children_comment', [])
            if comment.pid == item:
                item.children_comment.append(comment)
                break
        if comment.pid is None:
            comment_list.append(comment)

    article.view_count += 1
    article.comment_count = len(comments)
    article.save()
    return render(request,'article_detail.html',locals())

def comment_post(request):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = Comment.objects.create(username=comment_form.cleaned_data["username"],
                                             email=comment_form.cleaned_data["email"],
                                             content=comment_form.cleaned_data["content"],
                                             article=comment_form.cleaned_data["article"],
                                             pid=comment_form.cleaned_data["pid"],
                                             user=request.user if request.user.is_authenticated() else None)
        comment.save()
    else:
        return render(request, 'failure.html', {'reason': comment_form.errors})
    return redirect(request.META['HTTP_REFERER'])

@login_required
def article_new(request):
    if request.method=='POST':
        form=ArticleForm(request.POST)
        if form.is_valid():
            article=form.save(commit=False)
            article.author=request.user
            article.like_count=0
            article.view_count=0
            article.comment_count=0
            article.save()
            return redirect('blog.views.article_detail',pk=article.pk)
    else:
        form=ArticleForm()
    return render(request,'article_edit.html',{'form':form})

@login_required
def article_edit(request,pk):
    article=get_object_or_404(Article,pk=pk)
    if request.method=='POST':
        form=ArticleForm(request.POST,instance=article)
        if form.is_valid():
            article=form.save(commit=False)
            article.author=request.user
            article.save()
            return redirect('blog.views.article_detail',pk=article.pk)
    else:
        form=ArticleForm(instance=article)
    return render(request,'article_edit.html',{'form':form})

def article_draft_list(request):
    articles=Article.objects.filter(published_date__isnull=True).order_by('-created_date')
    return render(request,'article_draft_list.html',{'articles':articles})

@login_required
def article_publish(request,pk):
    article=get_object_or_404(Article,pk=pk)
    article.publish()
    return redirect('blog.views.article_detail',pk=article.pk)

@login_required
def article_remove(request,pk):
    article=get_object_or_404(Article,pk=pk)
    article.delete()
    return redirect('blog.views.blog')
def article_next(request,pk):
    pk=pk-1
    article=get_object_or_404(Article,pk=pk)
    return render(request,'article_detail.html',{'article':article})

def message(request):
    messages = Message.objects.all().order_by("id")
    message_form = MessageForm()
    return render(request,'message.html',{"messages": messages, "message_form": message_form})

def message_post(request):
    message_form = MessageForm(request.POST)
    if message_form.is_valid():
        message = Message.objects.create(name=message_form.cleaned_data["name"],
                                             content=message_form.cleaned_data["content"],)
        message.save()
    else:
        pass
    return redirect('blog.views.message')

def message_delete(request,pk):
    message=get_object_or_404(Message,pk=pk)
    message.delete()
    return redirect('blog.views.message')

def category(request):
    cid = request.GET.get('cid', None)
    try:
        category = Category.objects.get(pk=cid)
    except Category.DoesNotExist:
        return render(request, 'failure.html', {'reason': 'category not exit'})
    article_list = Article.objects.filter(category=category)
    return render(request, 'category.html', locals())

def tag(request):
    tid = request.GET.get('tid', None)
    try:
        tag = Tag.objects.get(pk=tid)
    except Tag.DoesNotExist:
        return render(request, 'failure.html', {'reason': 'tag not exit'})
    article_list = Article.objects.filter(tag=tag)
    return render(request, 'index.html', locals())

def archive(request):
    year = request.GET.get('y',None)
    month = request.GET.get('m', None)
    article_list = Article.objects.filter(published_date__icontains=year+'-'+month+'-')
    return render(request, 'archive.html',{'article_list': article_list,'year':year,'month':month})

def about(request):
    return render(request,'about.html')

def weiboLogin(request):

    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    url = client.get_authorize_url()
    return HttpResponseRedirect(url)

def weibo_check(request):
    global client
    code = request.GET.get('code', None)
    now = datetime.datetime.now()
    if code:
        client = APIClient(app_key=APP_KEY, app_secret=APP_SERCET, redirect_uri=CALLBACK_URL)
        r = client.request_access_token(code)
        access_token = r.access_token   # 返回的token，类似abc123xyz456
        expires_in = r.expires_in       # token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4
        uid = r.uid
        # 在此可保存access token
        client.set_access_token(access_token, expires_in)
        request.session['access_token'] = access_token
        request.session['expires_in'] = expires_in
        request.session['uid'] = uid
        return HttpResponseRedirect('/')
    return HttpResponse('/404/')

def search(request):
    query = request.GET.get('q','')
    if query:
        qset = (
            Q(title__icontains = query) |
            Q(text__icontains = query)
        )
        result = Article.objects.filter(qset).distinct()
    else:
        result = []
    return  render(request,'search.html',{'query':query,'result':result})
'''
def user_info(request):
    if request.session['uid']:
        data = {'access_token': request.session['access_token'], 'uid': request.session['uid']}
        params = urllib.urlencode(data)
        values = urllib2.Request(USER_INFO_URL+'?%s' %params)
        response = urllib2.urlopen(values)
        return HttpResponse(request.session['uid'])
    else :
        return HttpResponse("no user login")
'''