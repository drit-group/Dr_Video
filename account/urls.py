from .views import DashBoard
from django.urls import path
name = "account"
urlpatterns = [
    path('', DashBoard.as_view(),name="dashboard"),
]