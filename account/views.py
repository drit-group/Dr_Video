from django.db import models
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView,CreateView,UpdateView
from .models import Article
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import formMixin , Status_access
from django.urls import reverse_lazy
# Create your views here.

class DashBoard(LoginRequiredMixin,ListView):
    # model=Article
    login_url = '/admin/login/'
    template_name = "profile/main.html"
    def get_queryset(self):
        if self.request.GET.get('action') == "publish":
            art = get_object_or_404(Article,pk=self.request.GET.get('pk'))
            setattr(art,'status','p')
            art.save()
        return Article.objects.filter(writer=self.request.user)

class addArticle(Status_access,formMixin,LoginRequiredMixin,CreateView):
    model = Article
    template_name = "profile/addArticle.html"
    # fields = ['title','slug','thumbnail','description','status']
    success_url = reverse_lazy("account:dashboard")


class editArticle(Status_access,LoginRequiredMixin,UpdateView):
    model = Article
    template_name = "profile/addArticle.html"
    fields = ['title','slug','thumbnail','description','status']
    success_url = reverse_lazy("account:dashboard")