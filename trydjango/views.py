
from contextlib import redirect_stderr
from django.http import HttpResponse
from articles.models import Article
from django.shortcuts import render

def home(request,id=None):
    all = Article.objects.all()
 
    # return HttpResponse("<h2>{id}, {title}</h2>".format(**context))
    return render(request,"home.html",{"context":all} )


