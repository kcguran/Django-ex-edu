from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"blog/index.html")

def blogs(request):
    return render(request,"blog/blogs.html")

def blogDetails(request, id):
    return render(request,"blog/blogDetails.html",{
        "id":id
    })