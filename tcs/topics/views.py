# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from tcs.teams.models import Team
from tcs.topics.models import Topic, Follow, UploadFile
from tcs.topics.forms import *
from django.core.files.base import ContentFile
import os


@login_required
def list(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    return render_to_response('topics/list.html', locals())

@login_required
def mytopics(request):
    own_topics = request.user.topic_set.all()
    follow_topics = set([f.topic for f in request.user.follow_set.all()])
    return render_to_response('topics/mytopic_list.html', locals())


@login_required
def show(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    user_role = {}
    follows = {}
    for ut in topic.team.userofteam_set.all():
        user_role[ut.user] = ut.role
        follows[ut.role] = []
    for follow in topic.follow_set.all():
        role = user_role[follow.user]
        follows[role].append(follow)
    return render_to_response('topics/show.html', { 'topic':topic, 'follows':follows } )

@login_required
def follow(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    if request.method == 'POST':
        form = FollowForm(request.POST, request.FILES)
        if form.is_valid():
            follow = Follow(topic=topic, user=request.user, body=form.cleaned_data['body'])
            follow.save()
            if 'attachment' in request.FILES:
                file_content = ContentFile(request.FILES['attachment'].read())
                follow.attachment.save(request.FILES['attachment'].name, file_content)
            return redirect('/topics/%d/show' % (topic.id,))
        else:
            return render_to_response('topics/follow_form.html', {'topic':topic, 'form':form})
    else:
        form = FollowForm()
        return render_to_response('topics/follow_form.html', {'topic':topic, 'form':form})

@login_required
def new(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = Topic(
                    team = team,
                    user=request.user,
                    title = form.cleaned_data['title'],
                    body = form.cleaned_data['body'])
            topic.save()
            return redirect('/teams/%d/topics/list' % (team.id,))
    else:
        form = TopicForm()
        return render_to_response('topics/topic_form.html', {'team':team, 'form':form})

@login_required
def handle_uploaded_file(request, filedata):
    upfile = UploadFile(filename=filedata.name, user=request.user)
    upfile.save()
    upfile.storedpath = "upfile_%d_%d" % (request.user.id, upfile.id)
    upfile.save()
    destfile = open(os.path.join(os.path.dirname(__file__), '../uploadfiles', upfile.storedpath), 'wb+')
    for chunk in filedata.chunks():
        destfile.write(chunk)
    destfile.close()
    return upfile



