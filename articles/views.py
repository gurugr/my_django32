from tkinter.messagebox import NO
from django.shortcuts import render
from .models import Article
from.forms import ArticleForm
# Create your views here.
def article_detail_view(request,id=None):
    obj = None
    if obj == None and id is not None:
        obj = Article.objects.get(id=id)

    context = {"article":obj}
    return render(request,"articles/detail.html",context=context)


def article_search_view(request):
    query_dict = request.GET
    query = query_dict.get("q")
    article_obj = Article.objects.get(id = query)
    context = {"obj":article_obj}
    return render(request,"articles/search.html",context=context)

def article_clreate_view(request):
    form = ArticleForm(request.POST or None)
    context = {"form":form}
    

    if form.is_valid():
        form.save()
        context["form"] = ArticleForm()
        # title = form.cleaned_data.get("title")
        # content = form.cleaned_data.get("content")
        # print(title,content)
        # obj = Article.objects.create(title=title,content=content)
        # context["object"] = obj
        # context["created"] = True


    
    return render(request,"articles/create.html",context=context)
