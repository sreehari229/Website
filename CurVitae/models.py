from django.db import models


class Education(models.Model):
    course = models.CharField(max_length=200)
    institution_name = models.CharField(max_length=200)
    year_start = models.IntegerField()
    year_end = models.IntegerField()
    score = models.CharField(max_length=200)

    def __str__(self):
        return self.course
