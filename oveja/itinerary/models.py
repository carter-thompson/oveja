from django.db import models
from django.conf import settings

# Create your models here.
class Itinerary(models.Model):
    """
    Itinerary Model
    """
    title = models.CharField(max_length=255, null=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    isPublished = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.owner)