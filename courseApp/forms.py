from django import forms
from courseApp.models import Reports, StudentReports


class reportForm(forms.Form):
    report_title = forms.ChoiceField(required=False, label='کارنامه', choices=[])
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        reports = [(s.title, s.title) for s in
                   Reports.objects.all()]
        self.fields['report_title'] = forms.ChoiceField(required=False, label='کارنامه', choices=reports)


    class Meta:
        # model = StudentReports
        fields = ('report_title', 'files')
