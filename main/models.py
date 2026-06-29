from django.db import models

class Anime(models.Model):
    name = models.CharField(max_length=245)
    izoh = models.CharField(max_length=245)
    janr = models.CharField(max_length=245)
    yili = models.DateField()
    rasm = models.ImageField(upload_to="anime")
    def __str__(self):
        return self.name


