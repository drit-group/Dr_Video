from .views import wellcome
from django.urls import path
name = "account"
urlpatterns = [
    path('wellcome/', wellcome,name="wellcome"),
]