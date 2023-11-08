from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100);
    last_name = models.CharField(max_length=155);
    mark_score = models.IntegerField()
    url = models.URLField(verbose_name='Url')

    def __str__(self):
        return self.name