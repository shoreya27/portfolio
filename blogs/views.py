from django.shortcuts import render,get_object_or_404
from .models import Blog

# Create your views here.
def blogs(request):
    blog=Blog.objects
    return render(request,'blogs.html',{'blog':blog})

def blogdetails(request,blogid):
    blog=get_object_or_404(Blog,pk=blogid)
    return render(request,'blogdetails.html',{'blogs':blog})
