from .views import home
from django.urls import path
name = "landing"
urlpatterns = [
    path('', home,name="home"),
    path("page/<int:page>", home, name="home"),
]