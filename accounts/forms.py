from django import forms
from location_field.forms.plain import PlainLocationField
from django.contrib.auth import get_user_model
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from .models import Teacher
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



class TeacherForm(forms.ModelForm):
    bio = forms.CharField(label='Bio', widget=forms.Textarea(attrs={'rows': 5, 'placeholder':  'Bio '}))
    education_centre = forms.CharField(label = 'Education centre', max_length=50, required=True)
    avatar = forms.ImageField(label='Image',required=False, error_messages = {'invalid':"Image files only"}, widget=forms.FileInput)
    birth_date = forms.DateField(label='Birth date', required=False)
    phone = forms.DateField(label='Phone number', required=False)

    class Meta:
        model = Teacher
        fields = (
                'bio',
                'phone',
                'birth_date',
                'education_centre',
                'location', 
                'avatar' , 
                )
        widgets = {
        'birth_date': DatePickerInput(),
        }



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

class ProfileForm(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'autofocus': True }))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'autofocus': True}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'autofocus': True}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={}))
    password1 = forms.CharField(label='Pasword', widget=forms.PasswordInput(attrs={'placeholder':''}))
    password2 = forms.CharField(label='Confirm Pasword', widget=forms.PasswordInput(attrs={'placeholder':''}))

    class Meta:
        model = User
        fields = ('username',
                'email',
                'first_name',
                'last_name', 
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

class TeacherChangeForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = '__all__'
