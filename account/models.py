from django.db import models
# from django.contrib.auth.models import User
# AtractUser uses for customizing user model
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class User(AbstractUser):
    class Meta:
        verbose_name= "کاربر"
        verbose_name_plural= "کاربران"
    is_writer = models.BooleanField(verbose_name="وضعیت نویسندگی",default=False)

    
    


class Article(models.Model):
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
    title = models.CharField(max_length=200,verbose_name="عنوان مقاله")
    slug = models.CharField(max_length=100,verbose_name="ادرس مقاله")
    # source = models.FileField("videos/")
    thumbnail = models.ImageField(upload_to="images/",verbose_name="تصویر بند انگشتی")
    description = models.TextField()
    STATUSE_CASES=(
        ("d" , "‍‍‍‍بیش نویس"),
        ("p" , "منتشر" )
    )
    status=models.CharField( max_length=1,choices=STATUSE_CASES,verbose_name="وضعیت مقاله",default="d")
    puished=models.DateField(default=timezone.now,verbose_name="زمان انتشار مقاله")
    description = models.TextField()    

    writer = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,verbose_name="نویسنده :")
    
    published = models.DateField(default=timezone.now,verbose_name="تاریخ انتشار")
    def __str__(self):
        return self.title
    def get_image(self):
        return "/media/"+str(self.thumbnail)
    