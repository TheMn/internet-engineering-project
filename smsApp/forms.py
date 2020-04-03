from django import forms
from loginApp.models import User, Profile


class smsForm(forms.ModelForm):
    choice_10 = [(s.profile.parent_phone, s.first_name + ' ' + s.last_name) for s in
                 User.objects.filter(profile__grade=10).all()]
    choice_11 = [(s.profile.parent_phone, s.first_name + ' ' + s.last_name) for s in User.objects.filter(profile__grade=11).all()]
    field_10 = forms.MultipleChoiceField(required=False, label='پایه ی دهم', choices=choice_10)
    field_11 = forms.MultipleChoiceField(required=False, label='پایه ی یازدهم', choices=choice_11)
    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': '4'
    }), label='متن پیام')

    class Meta:
        model = Profile
        fields = ('field_10', 'field_11', 'text')
