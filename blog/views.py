from django.http import HttpResponse
from django.shortcuts import render
from matplotlib.style import context

data = {
    "blogs": [
        {
            "id": 1,
            "title": "komple web geliştirme",
            "image": "1.jpg",
            "is_active": True,
            "is_home": False,
            "description": "Çok iyi kurs"
        },
        {
            "id": 2,
            "title": "Python kursu",
            "image": "2.jpg",
            "is_active": True,
            "is_home": True,
            "description": "Çok iyi kurs"
        },
        {
            "id": 3,
            "title": "Django Kursu",
            "image": "3.jpg",
            "is_active": False,
            "is_home": True,
            "description": "Çok iyi kurs"
        }
    ]
}

def index(request):
    context = {
        "blogs": data["blogs"]
    }
    return render(request,"blog/index.html", context)

def blogs(request):
    context = {
        "blogs": data["blogs"]
    }
    return render(request,"blog/blogs.html", context)

def blogDetails(request, id):
    return render(request,"blog/blogDetails.html",{
        "id":id
    })