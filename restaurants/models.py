from django.db import models


# Create your models here.
class Restaurants(models.Model):
    name = models.CharField(max_length=10)
    location = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'restaurants'

    def __str__(self):
        return self.name


