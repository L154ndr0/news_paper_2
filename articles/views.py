from django.shortcuts import render
from django.views.generic import ListView

from .models import Article
# Create your views here idiot.

class ArticleView(ListView):
    model = Article
    template_name = "article_list.html"
