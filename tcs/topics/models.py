from django.db import models

# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __unicode__(self):
        return self.title


class Follow(models.Model):
    body = models.TextField()
    topic = models.ForeignKey('Topic')

    def __unicode__(self):
        return self.body[:200]

