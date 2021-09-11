from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,CreateView
from .models import Article
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class DashBoard(LoginRequiredMixin,ListView):
    # model = Article
    login_url = "/admin/login"
    template_name = "profile/main.html"
    def get_queryset(self):
        return Article.objects.filter(writer=self.request.user)
class addArticle(LoginRequiredMixin,CreateView):
    model = Article
    template_name = "profile/addArticle.html"
    fields = ['title','slug','thumbnail','description','status']