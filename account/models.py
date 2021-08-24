from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200,verbose_name="عنوان مقاله")
    slug = models.CharField(max_length=100,verbose_name="ادرس مقاله")
    # source = models.FileField("videos/")
    thumbnail = models.ImageField(upload_to="images/",verbose_name="تصویر بند انگشتی")
    description = models.TextField()
    def __str__(self):
        return self.title
    def get_image(self):
        return "/media/"+str(self.thumbnail)
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"