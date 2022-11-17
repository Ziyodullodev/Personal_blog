from django.shortcuts import render
from .models import Books, Blog
# Create your views here.


def home(req):
    blogs = Blog.objects.all()
    return render(req, 'index.html',context={'blogs':blogs})

def books(req):
    books = Books.objects.all()
    return render(req, 'books.html', context={'books':books})

def contact(req):
    return render(req, 'contact.html')

def about(req):
    return render(req, 'about.html')

def blogdetail(req, pk):
    blog = Blog.objects.get(id=pk)
    return render(req, 'single.html', context={'blog':blog})