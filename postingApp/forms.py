from django import forms
from djrichtextfield.models import RichTextField
from .models import PostStuff


class PageForm(forms.ModelForm):
    text = RichTextField(field_settings='advanced')

    class Meta:
        model = PostStuff
        fields = ('text',)
