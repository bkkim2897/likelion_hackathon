from django.shortcuts import render, redirect
from .models import Blog
from django.utils import timezone



# Create your views here.
def mypage(request):
    blogs = Blog.objects.order_by('-pub_date')
    return render(request, 'mypage.html', {'blogs': blogs})

def guide_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    return render(request, 'guide_detail.html', {'blog' : blog})

def guide_new(request) :
    return render(request, 'guide_new.html')

def create(request):
    blog =Blog()
    blog.title = request.POST['title']
    blog.tag = request.POST['tag']
    blog.place = request.POST['place']
    blog.content = request.POST['content']
    blog.photo = request.FILES['photo']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    blogs=Blog.objects.all()
    return render(request, 'mypage.html', {'blogs':blogs})

def guide_edit(request, pk):
    blog=get_object.objects.get(pk=pk)
    return render(request, 'guide_edit.html', {'blog':blog})

def guide_update(request, pk):
    blog=Blog.objects.get(pk=pk)
    blog.title = request.POST['title']
    blog.tag = request.POST['tag']
    blog.place = request.POST['place']
    blog.content = request.POST['content']
    blog.pub_date = timezone.datetime.now()

    blog.save()
    return redirect('mypage')

def guide_delete(request, pk):
    blog=Blog.objects.get(pk=pk)
    blog.delete()
    return redirect('mypage')

def result(request):
    query = request.GET['query']
    if query:
        blog = Blog.objects.filter(title__contains=query)
    return render(request, 'result.html',{'blog': blog})
def search(request):
    return render(request, 'search.html')

    
    