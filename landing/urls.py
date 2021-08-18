from .views import home,detail,multi
from django.urls import path
name = "landing"
urlpatterns = [
    path('', home,name="home"),
    path("page/<int:page>", home, name="home"),
    path('video/<int:pk_id>', detail ,name="single"),
    path("multi/<int:num>", multi, name="m"),

]