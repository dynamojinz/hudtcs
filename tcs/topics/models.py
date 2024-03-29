from django.db import models
from django.contrib.auth.models import User
from tcs.teams.models import Team

# Create your models here.
class UploadFile(models.Model):
    filename = models.CharField(max_length=100)
    storedpath = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.filename

class Topic(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    team = models.ForeignKey('teams.Team')
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class Follow(models.Model):
    body = models.TextField()
    topic = models.ForeignKey('Topic')
    user = models.ForeignKey(User)
    attachment = models.FileField(upload_to='uploadfiles')  # id of UploadFile
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.body[:200]



