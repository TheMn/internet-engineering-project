from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import PostStuff


class PageForm(forms.ModelForm):
    content = forms.CharField(widget= RichTextWidget)

    class Meta:
        model = PostStuff
        fields = ('content', )