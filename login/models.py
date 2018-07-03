from django.db import models

class user_info(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
