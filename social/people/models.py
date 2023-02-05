from django.db import models

class People(models.Model):
    name = models.TextField(max_length=255)
    surname = models.TextField(max_length=255)
    login = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_online = models.BooleanField(default=True)

    def __str__(self):
        return self.name
