from django.shortcuts import render
from MyApp.models import MyAppBlogPost,MyAppBlogPostForm
from datetime import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.template import RequestContext
from django import forms
def home(request):
     return HttpResponse("Hello, Welcome to My Blog website")

"""
def archive(request):
    post = MyAppBlogPost(title='Mocktitle', body='mockbody',timestamp=datetime.now())
    return render(request,'archive.html', {'posts': [post]})

def archive(request):
    posts = MyAppBlogPost.objects.all()
    #posts = MyAppBlogPost.objects.all().order_by('-timestamp')[:2]
    t = get_template("archive - Copy.html")
    c = {'posts': posts}
    return HttpResponse(t.render(c,request))

def create_blogpost(request):
    if request.method == 'POST':
         MyAppBlogPost(title=request.POST.get('title'),body=request.POST.get('body'),
                 timestamp=datetime.now(),).save()
    return HttpResponseRedirect('/MyApp/')
"""
def archive(request):
    posts = MyAppBlogPost.objects.all().order_by('-timestamp')
    return render(request,'archive_form.html',{'posts': posts,'form': MyAppBlogPostForm()})

def create_blogpost(request):
    if request.method == 'POST':
        form = MyAppBlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.timestamp=datetime.now()
            post.save()
    return HttpResponseRedirect('/MyApp/')

