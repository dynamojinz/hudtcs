from django import forms

class FollowForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea(attrs={'cols':130, 'rows':15}))
    attachment = forms.FileField(required=False)


class TopicForm(forms.Form):
    title = forms.CharField(required=True)
    body = forms.CharField(widget=forms.Textarea(attrs={'cols':130, 'rows':15}))

