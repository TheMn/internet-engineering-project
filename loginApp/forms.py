from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.', label=u'نام')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.', label=u'نام خانوادگی')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',
                             label=u'پست الکترونیکی')
    phoneNumber = forms.CharField(max_length=30, required=False, label=u'شماره موبایل', widget=forms.TextInput(
        attrs={'class': 'form-control', 'autocomplete': 'off', 'pattern': '[0-9]+', 'title': 'Enter numbers Only '}))
    password1 = forms.CharField(label=_(u"رمز عبور"),
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label=_(u"تایید رمز عبور"),
                                widget=forms.PasswordInput,
                                help_text=_("Enter the same password as above, for verification."))
    birth_date = forms.DateField(required=False, help_text="Enter your birth date.", label=u'تاریخ تولد')
    prof_pic = forms.ImageField(required=False)

    class Meta:
        User._meta.get_field('email')._unique = True
        model = User
        fields = ('username', 'first_name', 'phoneNumber', 'last_name', 'email', 'password1', 'password2', 'birth_date', 'prof_pic', )
        labels = {
            'username': _(u'نام کاربری'),
        }