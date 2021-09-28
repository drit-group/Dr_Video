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
    is_admin = models.BooleanField(verbose_name="وضعیت مدیر",default=False)    
    
class Category(models.Model):
    name = models.CharField("نام دسته بندی", max_length=50)
    status = models.BooleanField("وضعیت تگ")
    slug = models.CharField("اسلاگ تگ", max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "دسته"
        verbose_name_plural = "دسته بندی"

class Film(models.Model):
    class Meta:
        verbose_name = "فیلم"
        verbose_name_plural = "فیلم ها"

    
    title = models.CharField(max_length=200,verbose_name="عنوان فیلم")
    slug = models.CharField(max_length=100,verbose_name="ادرس فیلم")
    source = models.FileField("videos/",null=True)
    iframe_source = models.CharField(max_length=600,null=True)
    thumbnail = models.ImageField(upload_to="images/",verbose_name="تصویر بند انگشتی")
    description = models.TextField()
    STATUSE_CASES=(
        ("d" , "‍‍‍‍بیش نویس"),
        ("p" , "منتشر" ),
        ("d","حذف شده")
    )
    status=models.CharField( max_length=1,choices=STATUSE_CASES,verbose_name="وضعیت فیلم",default="d")
    puished=models.DateField(default=timezone.now,verbose_name="زمان انتشار فیلم")
    description = models.TextField()

    creator = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,verbose_name="منتشر کننده :")
    



    category = models.ManyToManyField(Category,related_name="film",verbose_name="دسته بندی")

    def get_category(self):
        cats = self.category.filter(status=True)
        # result = ""
        # for category in cats:
        #     result += category.name
        return ",".join([category.name for  category in cats]) 
    def __str__(self):
        return self.title
    def get_image(self):
        return "/media/"+str(self.thumbnail)
    def get_video(self):
        return "/media/"+str(self.source)



