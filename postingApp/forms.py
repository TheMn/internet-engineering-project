from django import forms
from djrichtextfield.models import RichTextField
from .models import PostStuff, Comment


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    text = RichTextField(field_settings='advanced')
    description = forms.CharField(max_length=160)
    # img = forms.ImageField()
    # categories
    featured = forms.BooleanField()

    class Meta:
        model = PostStuff
        fields = (
            'title',
            'text',
            'description',
            # 'img',
            'featured',
        )


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'پیام',
        'id': 'message',
        'rows': '4'
    }))

    class Meta:
        model = Comment
        fields = ('text',)
