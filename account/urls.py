from .views import DashBoard,addArticle
from django.urls import path
name = "account"
urlpatterns = [
    path('', DashBoard.as_view(),name="dashboard"),
    path('create', addArticle.as_view(),name="addArticle"),
]