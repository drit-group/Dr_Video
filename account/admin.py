from django.contrib import admin
from .models import Article,User
# Register your models here.
admin.site.register(User)
admin.site.register(Article)