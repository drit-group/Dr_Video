from .views import DashBoard,addArticle,editArticle
from django.urls import path
app_name = "account"
urlpatterns = [
    path('', DashBoard.as_view(),name="dashboard"),
    path('create', addArticle.as_view(),name="addArticle"),
    path("edit/<int:pk>", editArticle.as_view(), name="editArticle"),
]