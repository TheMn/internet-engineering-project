from django import forms
from froala_editor.widgets import FroalaEditor
from .models import PostStuff


class PageForm(forms.ModelForm):
    content = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = PostStuff
        fields = ('title', 'text')