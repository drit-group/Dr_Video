<<<<<<< HEAD
from .views import DashBoard ,addArticle
=======
from .views import DashBoard,addArticle,editArticle
>>>>>>> 24175081143c5fa32d25d2666f8f9eabcd4cee1c
from django.urls import path
app_name = "account"
urlpatterns = [
    path('', DashBoard.as_view(),name="dashboard"),
<<<<<<< HEAD
    path('create/',addArticle.as_view(),name="addArticle")
=======
    path('create', addArticle.as_view(),name="addArticle"),
    path("edit/<int:pk>", editArticle.as_view(), name="editArticle"),
>>>>>>> 24175081143c5fa32d25d2666f8f9eabcd4cee1c
]