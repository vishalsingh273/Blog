from django.db import models

# Create your models here.
class Home(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content=models.TextField()
    time=models.DateTimeField(auto_now_add=True)

