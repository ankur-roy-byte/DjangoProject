from django.db import models

# Create your models here.

class Event(models.Model):
    EVENT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)
    totalPerson = models.IntegerField()
    release_date = models.DateField()
    event_size = models.CharField(max_length=1, choices=EVENT_SIZES)
