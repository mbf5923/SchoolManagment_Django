from django.db import models

# Create your models here.
from User.models import CustomUser


class Lessons(models.Model):
    title = models.CharField(max_length=255, null=False)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='teacherid')
    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='managerid')


class Students(models.Model):
    name = models.CharField(max_length=255, null=False)
    family = models.CharField(max_length=255, null=False)
    lesson = models.ManyToManyField(Lessons)
