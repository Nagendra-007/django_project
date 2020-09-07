from django.db import models

class Member(models.Model):
    Name = models.CharField(max_length=25)
    Username = models.CharField(max_length=25)
    Password1 = models.CharField(max_length=25)
    Password2 = models.CharField(max_length=25)
    DOB = models.CharField(max_length=25)


    def __str__(self):
        return self.Name