from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate
from .models import PreRegisteredStudent


class PreRegistrationFrom(ModelForm):
    class Meta:
        model = PreRegisteredStudent
        fields = '__all__'
        labels = {
            "student_first_name": "نام",
            "student_last_name": "نام خانوادگی",
        }
        # required = '__all__'


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(max_length=50, required=True)
    subject = forms.CharField(max_length=50, required=False)
    body = forms.CharField(widget=forms.Textarea, required=True)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.', label=u'نام')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.', label=u'نام خانوادگی')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',
                             label=u'پست الکترونیکی')
    phone = forms.CharField(max_length=30, required=False, label=u'شماره موبایل', widget=forms.TextInput(
        attrs={'class': 'form-control', 'autocomplete': 'off', 'pattern': '[0-9]+', 'title': 'Enter numbers Only '}))
    password1 = forms.CharField(label=_(u"رمز عبور"),
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label=_(u"تایید رمز عبور"),
                                widget=forms.PasswordInput,
                                help_text=_("Enter the same password as above, for verification."))
    birth_date = forms.DateField(required=False, help_text="Enter your birth date.", label=u'تاریخ تولد')
    img = forms.ImageField(required=False)

    class Meta:
        User._meta.get_field('email')._unique = True
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'phone', 'email', 'password1', 'password2', 'birth_date', 'img',)
        labels = {
            'username': _(u'نام کاربری'),
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("login error")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
