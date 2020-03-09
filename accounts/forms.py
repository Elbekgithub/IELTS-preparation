from django import forms
from location_field.forms.plain import PlainLocationField
from django.contrib.auth import get_user_model
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)

from bootstrap_datepicker_plus import DatePickerInput

User = get_user_model()

class UserLoginFom(forms.Form):
    username = forms.CharField(label=False, widget=forms.TextInput(attrs={'autofocus': True, 'placeholder':'Username or Email'}))
    password = forms.CharField(label=False,widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username = username, password = password)
        if not user:
            raise forms.ValidationError("Bu foydalanuvchi nomi yoki parol noto'g'ri kiritildi")



class TeacherCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    
    location = PlainLocationField(based_fields=['education_centre'],
                                  initial='-22.2876834,-49.1607606')
    bio = forms.CharField(label='Bio', widget=forms.Textarea(attrs={'rows': 5, 'placeholder':  'Bio '}))
    education_centre = forms.CharField(label = 'Education centre', max_length=50, required=True)
    avatar = forms.ImageField(label='Image',required=False, error_messages = {'invalid':"Image files only"}, widget=forms.FileInput)
    birth_date = forms.DateField(label='Birth date', required=False)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',
                'email',
                'bio',
                'birth_date',
                'avatar' , 
                'password1', 
                'password2',
                'education_centre',
                'location', 
                )
        widgets = {
        'birth_date': DatePickerInput(),
        }

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2



class StudentCreationForm(forms.ModelForm):
    username = forms.CharField(label=False, widget=forms.TextInput(attrs={'autofocus': True, 'placeholder':'Username'}))
    email = forms.CharField(label=False, widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    password1 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder':'Password confirmation'}))

    class Meta:
        model = User
        fields = ('username',
                'email', 
                'password1', 
                'password2',
                )

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2