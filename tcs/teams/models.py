from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class UserOfTeam(models.Model):
    user = models.ForeignKey(User)
    team = models.ForeignKey(Team)
    role = models.ForeignKey(Role)

    def __unicode__(self):
        return u"%s belongs to %s, role:%s" % (self.user, self.team, self.role)

