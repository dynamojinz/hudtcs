# Create your views here.
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from tcs.teams.models import UserOfTeam

@login_required
def list(request):
    user_of_teams = UserOfTeam.objects.filter(user=request.user)
    return render_to_response('teams/list.html', locals())
