from django import forms
from djrichtextfield.models import RichTextField
from .models import PostStuff, Comment


class PageForm(forms.ModelForm):
    text = RichTextField(field_settings='advanced')

    class Meta:
        model = PostStuff
        fields = ('text',)


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'پیام',
        'id': 'message',
        'rows' : '4'
    }))

    class Meta:
        model = Comment
        fields = ('text',)
