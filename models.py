from django.db import models

# Create your models here.
class BlackBelt (models.Model):
    prefix          = models.CharField(max_length = 10)
    first_name      = models.CharField(max_length = 20)
    last_name       = models.CharField(max_length = 20)
    rank            = models.CharField(max_length = 20)
    instructor_bio  = models.TextField(blank = True)

    def __str__(self):
        return self.prefix + " " + self.first_name + " " + self.last_name