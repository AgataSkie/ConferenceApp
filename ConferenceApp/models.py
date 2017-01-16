from django.db import models
from django.urls import reverse
# from


# Create your models here.
class Speaker(models.Model):
    name = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    bio = models.TextField(max_length=500)
    twitter = models.CharField(max_length=60, blank=True, null=True)
    fb = models.CharField(max_length=60, blank=True, null=True)


    def __str__(self):
        return self.name


class Track(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title


SESSION_STATUS = (
    ('a', 'Approved'),
    ('p', 'pending'),
    ('r', 'rejected'),
)


class Session(models.Model):
    title = models.CharField(max_length=80)
    abstract = models.TextField(max_length=500)
    track = models.ForeignKey(Track)
    speaker = models.ForeignKey(Speaker)
    status = models.CharField(max_length=1, choices=SESSION_STATUS, default='p')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('conference:session_detail', kwargs={'pk': self.pk})
