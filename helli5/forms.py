from django import forms


class BunchAddForm(forms.Form):
    model_type = forms.ChoiceField(required=False, label='کارنامه', choices=[])
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': False}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choice = [
            ('user', 'کاربر'),
        ]
        self.fields['model_type'] = forms.ChoiceField(required=False, label='کارنامه', choices=choice)

    class Meta:
        fields = ('model_type', 'file')
