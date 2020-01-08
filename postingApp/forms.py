from django import forms
from djrichtextfield.models import RichTextField
from .models import PostStuff, Comment


class PageForm(forms.ModelForm):
    text = RichTextField(field_settings='advanced')

    class Meta:
        model = PostStuff
        fields = ('text',)


# class CommentForm(forms.ModelForm):
#     content = forms.Textarea(attrs={
#         'class': 'form-control'
#     })
#
#     class Meta:
#         model = Comment
#         fields = ('content',)
