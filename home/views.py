from django.shortcuts import render,HttpResponse
from home.models import Home
# Create your views here.
def home(request):
    return render (request, 'index.html')

def blog(request):
    blogs = Home.objects.all()
    context={'blogs':blogs}
    return render(request,'blog.html',context)

def search(request):
     return render(request,'search.html')

def blogpost(request,slug):
    blog=Home.objects.filter(slug=slug).first()
    context={'blog':blog}
    return render(request,'blogpost.html',context)

def contact(request):
    return render(request,'contact.html')

