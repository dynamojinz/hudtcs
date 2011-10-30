from django.contrib import admin
from tcs.teams.models import Team, Role, UserOfTeam

admin.site.register(Team)
admin.site.register(Role)
admin.site.register(UserOfTeam)
