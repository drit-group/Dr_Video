from django.db import models

# Create your models here.
class Vidoes(models.Model):
    title = models.CharField("عنوان ویدیو",max_length=200)
    # source = models.FileField("videos/")
    source = models.FileField(upload_to="videos/", max_length=100)
    url = models.CharField(max_length=250,null=True)
    description = models.TextField()
    def get_image(self):
        return "/media/"+str(self.source)