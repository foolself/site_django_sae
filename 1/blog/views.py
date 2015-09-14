from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from .models import Article, Comment, Message, Category, Tag
from .forms import ArticleForm, CommentForm, MessageForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def global_setting(request):
	title = "foolself blog"
	category_list = Category.objects.all()[:6]
	tag_list = Tag.objects.all()
	tag_format_ = ["btn btn-danger","btn btn-success","btn btn-default","btn btn-info","btn btn-warning","btn btn-primary",]
	tag_dict = {}
	for i in range(len(tag_list)):
		tag_dict[tag_list[i]]=tag_format_[i % len(tag_format_)]
	return locals()

def home(request):
	article_list=Article.objects.filter(published_date__isnull=False).order_by('-pk')#'-published_date')

	return render(request,'index.html',{'article_list':article_list})
	#return render(request,'test.html')

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
	return render(request,'article_detail.html',locals())

def comment_post(request):
	comment_form = CommentForm(request.POST)
	if comment_form.is_valid():
		comment = Comment.objects.create(username=comment_form.cleaned_data["username"],
                                             email=comment_form.cleaned_data["email"],
                                             content=comment_form.cleaned_data["content"],
                                             article=comment_form.cleaned_data["article"],
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
	return redirect('blog.views.home')
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

def about(request):
	return render(request,'about.html')