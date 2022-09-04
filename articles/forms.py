
from re import S
from django import forms
from.models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","content"]


    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        content = data.get("content")
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error("title",f"{title} is taken")
        qs = Article.objects.filter(content__icontains=title)
        if qs.exists():
            self.add_error("content",f"{content} is taken")
        return data

class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    print("Hellow chan")

    def clean_title(self):
        print("Hello world")
        print(self.cleaned_data)
        cleaned_data = self.cleaned_data
        title = cleaned_data.get("title")
        obj = Article.objects
        if title.lower().strip() == "chan":
            raise forms.ValidationError(f"{title} is taken")
        print(title)
        return title

