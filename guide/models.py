from django.db import models

class Guide(models.Model):
    name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    experience_years = models.IntegerField()

    def __str__(self):
        return self.name