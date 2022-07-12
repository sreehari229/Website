from email.policy import default
from django.db import models


class Education(models.Model):
    course = models.CharField(max_length=200)
    institution_name = models.CharField(max_length=200)
    year_start = models.IntegerField()
    year_end = models.IntegerField()
    score = models.CharField(max_length=200)
    display = models.BooleanField(default=True)

    def __str__(self):
        return self.course

class Projects(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    is_source_code = models.BooleanField(default=True)
    link = models.TextField(default=' - ')
    display = models.BooleanField()
    image = models.CharField(max_length=200,default='default.jpg')
    is_website = models.BooleanField(default=False)
    website_link = models.TextField(default=' ')
    tech_used = models.TextField(default=' ')

    def __str__(self):
        return self.name
