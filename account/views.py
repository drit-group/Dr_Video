from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Article
# Create your views here.

class DashBoard(ListView):
    model = Article
    template_name = "profile/main.html"