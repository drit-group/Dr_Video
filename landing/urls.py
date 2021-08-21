from .views import DetailVideo,multi,ListVideo
from django.urls import path
name = "landing"
urlpatterns = [
    path('', ListVideo.as_view(),name="home"),
    path("page/<int:page>", ListVideo.as_view(), name="home"),
    path('video/<int:pk>', DetailVideo.as_view() ,name="single"),
    path("multi/<int:num>", multi, name="m"),

]