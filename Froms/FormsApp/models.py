from django.db import models


# Create your models here.

class profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    proPic = models.ImageField(upload_to='static/img', null=True)

    def __str__(self):
        return str(self.name)