from django import forms
from .models import Comment
class GuestForm(forms.Form):
    writer = forms.CharField(max_length=10)
    content = forms.CharField(max_length=100)

    def save(self, *args,**kwargs):
        super(CreatePostForm, self).save(*args, **kwargs)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
