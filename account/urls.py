from .views import DashBoard,addFilm,editFilm
from django.urls import path
app_name = "account"
urlpatterns = [
    path('', DashBoard.as_view(),name="dashboard"),
    path('create', addFilm.as_view(),name="addArticle"),
    path("edit/<int:pk>", editFilm.as_view(), name="editArticle"),
]