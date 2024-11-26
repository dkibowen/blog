from django.shortcuts import render
from blogs.models import Category,Blog
from about.models import About


def home(request):    
    featured_posts = Blog.objects.filter(is_featured=True,status="Published").order_by("-created_at")
    posts = Blog.objects.filter(is_featured=False,status="Published")
    about = About.objects.get()
    context = {        
        "featured_posts":featured_posts,
        "posts":posts,
        "about":about,
    }
    return render(request,'home.html',context)