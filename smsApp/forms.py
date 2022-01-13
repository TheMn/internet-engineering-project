from django import forms
from loginApp.models import User, Profile


class smsForm(forms.ModelForm):
    field_10_student = forms.MultipleChoiceField(required=False, label='دانش آموزان پایه دهم')
    field_10_mom = forms.MultipleChoiceField(required=False, label='مادر دانش آموزان پایه دهم')
    field_10_dad = forms.MultipleChoiceField(required=False, label='پدر دانش آموزان پایه دهم')
    field_11_student = forms.MultipleChoiceField(required=False, label='دانش آموزان پایه یازدهم')
    field_11_mom = forms.MultipleChoiceField(required=False, label='مادر دانش آموزان پایه یاردهم')
    field_11_dad = forms.MultipleChoiceField(required=False, label='پدر دانش آموزان پایه یازدهم')
    teacher = forms.MultipleChoiceField(required=False, label='دبیران')
    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': '4'
    }), label='متن پیام')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choice_10_student = [(s.profile.phone, s.first_name + ' ' + s.last_name) for s in
                             User.objects.filter(username__regex='400d*').all()]
        choice_10_mom = [(s.profile.mom_number, s.first_name + ' ' + s.last_name) for s in
                         User.objects.filter(username__regex='400d*').all()]
        choice_10_dad = [(s.profile.dad_number, s.first_name + ' ' + s.last_name) for s in
                         User.objects.filter(username__regex='400d*').all()]
        choice_11_mom = [(s.profile.mom_number, s.first_name + ' ' + s.last_name) for s in
                         User.objects.filter(username__regex='399d*').all()]
        choice_11_dad = [(s.profile.dad_number, s.first_name + ' ' + s.last_name) for s in
                         User.objects.filter(username__regex='399d*').all()]
        choice_11_student = [(s.profile.phone, s.first_name + ' ' + s.last_name) for s in
                             User.objects.filter(username__regex='399d*').all()]
        choice_teachers = [(s.profile.phone, s.first_name + ' ' + s.last_name) for s in
                           User.objects.filter(groups__name='Teacher').all()]
        self.fields['field_10_student'] = forms.MultipleChoiceField(required=False, choices=choice_10_student,
                                                                    label='دانش آموزان پایه دهم')
        self.fields['field_10_mom'] = forms.MultipleChoiceField(required=False, choices=choice_10_mom,
                                                                label='مادر دانش آموزان پایه دهم')
        self.fields['field_10_dad'] = forms.MultipleChoiceField(required=False, choices=choice_10_dad,
                                                                label='پدر دانش آموزان پایه دهم')
        self.fields['field_11_student'] = forms.MultipleChoiceField(required=False, choices=choice_11_student,
                                                                    label='دانش آموزان پایه یازدهم')
        self.fields['field_11_mom'] = forms.MultipleChoiceField(required=False, choices=choice_11_mom,
                                                                label='مادر دانش آموزان پایه یاردهم')
        self.fields['field_11_dad'] = forms.MultipleChoiceField(required=False, choices=choice_11_dad,
                                                                label='پدر دانش آموزان پایه یازدهم')
        self.fields['teacher'] = forms.MultipleChoiceField(required=False, choices=choice_teachers,
                                                           label='دبیران')

    class Meta:
        model = Profile
        fields = ('field_10_student', 'field_10_mom', 'field_10_dad', 'field_11_student', 'field_11_mom',
                  'field_11_dad', 'teacher', 'text')
