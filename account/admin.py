from django.contrib import admin
from .models import Film,User,Category
# Register your models here.
admin.site.register(User)
admin.site.register(Film)
admin.site.register(Category)