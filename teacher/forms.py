from django import forms 
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *

class NewMockForm(forms.ModelForm):
    name = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'Name'}))
    bio = forms.CharField(label=False, widget=forms.Textarea(attrs={'placeholder':'Description'}), required=False)
    is_free = forms.CharField(label='Is free | if yes, please leave a next input', widget=forms.CheckboxInput())
    fee = forms.DecimalField(label=False, initial= '0.00', required=False)
    time_start = forms.DateField(label=False, widget=forms.DateInput(attrs={'id': 'date-picker-example','class':'form-control datepicker', 'placeholder':'Start date'}))
    speak_date = forms.CharField(label=False, widget=forms.DateInput(attrs={'id': 'date-picker-example','class':'form-control datepicker','placeholder':'Speaking date'}))
    class Meta:
        model = MockTest
        fields = ('name', 'bio', 'is_free', 'fee', 'time_start', 'speak_date',)

class ListeningForm(forms.ModelForm):
    audio = forms.FileField(label='Audio')
    section1 = forms.CharField(label='Section 1', widget=CKEditorUploadingWidget())
    section2 = forms.CharField(label='Section 2', widget=CKEditorUploadingWidget())
    section3 = forms.CharField(label='Section 3', widget=CKEditorUploadingWidget())
    section4 = forms.CharField(label='Section 4', widget=CKEditorUploadingWidget())
    class Meta:
        model = Listening
        fields = ('audio', 'pdf', 'section1','section2','section3','section4', )

class ReadingForm(forms.ModelForm):
    passage1 = forms.CharField(label='Passage 1', widget=CKEditorUploadingWidget())
    passage2 = forms.CharField(label='Passage 2', widget=CKEditorUploadingWidget())
    passage3 = forms.CharField(label='Passage 3', widget=CKEditorUploadingWidget())
    class Meta:
        model = Reading
        fields = ('pdf', 'passage1','passage2','passage3', )

class WritingForm(forms.ModelForm):
    task1 = forms.CharField(label='Task 1', widget=CKEditorUploadingWidget())
    task2 = forms.CharField(label='Task 2', widget=CKEditorUploadingWidget())
    class Meta:
        model = Writing
        fields = ('pdf', 'task1','task2','image', )

class SpeakingForm(forms.ModelForm):
    part1 = forms.CharField(label='Part 1', widget=CKEditorUploadingWidget())
    part2 = forms.CharField(label='Part 2', widget=CKEditorUploadingWidget())
    part3 = forms.CharField(label='Part 3', widget=CKEditorUploadingWidget())
    class Meta:
        model = Speaking
        fields = ('pdf', 'part1','part2','part3', )

class AnswerListeningForm(forms.ModelForm):
    a1 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer1'}))
    a2 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer2'}))
    a3 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer3'}))
    a4 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer4'}))
    a5 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer5'}))
    a6 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer6'}))
    a7 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer7'}))
    a8 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer8'}))
    a9 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer9'}))
    a10 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer10'}))
    a11 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer11'}))
    a12 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer12'}))
    a13 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer13'}))
    a14 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer14'}))
    a15 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer15'}))
    a16 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer16'}))
    a17 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer17'}))
    a18 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer18'}))
    a19 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer19'}))
    a20 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer20'}))
    a21 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer21'}))
    a22 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer22'}))
    a23 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer23'}))
    a24 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer24'}))
    a25 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer25'}))
    a26 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer26'}))
    a27 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer27'}))
    a28 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer28'}))
    a29 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer29'}))
    a30 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer30'}))
    a31 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer31'}))
    a32 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer32'}))
    a33 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer33'}))
    a34 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer34'}))
    a35 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer35'}))
    a36 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer36'}))
    a37 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer37'}))
    a38 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer38'}))
    a39 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer39'}))
    a40 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer40'}))

    class Meta:
        model = AnswerListening
        fields = ('a1','a2','a3','a4','a5','a6',
        'a7','a8','a9','a10','a11','a12','a13','a14','a15',
        'a16','a17','a18','a19','a20','a21','a22','a23','a24',
        'a25','a26','a27','a28','a29','a30','a31','a32','a33',
        'a34','a35','a36','a37','a38','a39','a40',)

class AnswerReadingForm(forms.ModelForm):
    a1 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer1'}))
    a2 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer2'}))
    a3 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer3'}))
    a4 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer4'}))
    a5 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer5'}))
    a6 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer6'}))
    a7 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer7'}))
    a8 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer8'}))
    a9 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer9'}))
    a10 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer10'}))
    a11 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer11'}))
    a12 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer12'}))
    a13 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer13'}))
    a14 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer14'}))
    a15 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer15'}))
    a16 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer16'}))
    a17 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer17'}))
    a18 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer18'}))
    a19 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer19'}))
    a20 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer20'}))
    a21 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer21'}))
    a22 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer22'}))
    a23 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer23'}))
    a24 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer24'}))
    a25 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer25'}))
    a26 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer26'}))
    a27 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer27'}))
    a28 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer28'}))
    a29 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer29'}))
    a30 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer30'}))
    a31 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer31'}))
    a32 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer32'}))
    a33 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer33'}))
    a34 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer34'}))
    a35 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer35'}))
    a36 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer36'}))
    a37 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer37'}))
    a38 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer38'}))
    a39 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer39'}))
    a40 = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'answer40'}))
    class Meta:
        model = AnswerReading
        fields = ('a1','a2','a3','a4','a5','a6',
        'a7','a8','a9','a10','a11','a12','a13','a14','a15',
        'a16','a17','a18','a19','a20','a21','a22','a23','a24',
        'a25','a26','a27','a28','a29','a30','a31','a32','a33',
        'a34','a35','a36','a37','a38','a39','a40',)

class AnswerListeningUpdateForm(forms.ModelForm):
    class Meta:
        model = AnswerListening
        fields = ('a1','a2','a3','a4','a5','a6',
        'a7','a8','a9','a10','a11','a12','a13','a14','a15',
        'a16','a17','a18','a19','a20','a21','a22','a23','a24',
        'a25','a26','a27','a28','a29','a30','a31','a32','a33',
        'a34','a35','a36','a37','a38','a39','a40',)

class AnswerReadingUpdateForm(forms.ModelForm):
    class Meta:
        model = AnswerReading
        fields = ('a1','a2','a3','a4','a5','a6',
        'a7','a8','a9','a10','a11','a12','a13','a14','a15',
        'a16','a17','a18','a19','a20','a21','a22','a23','a24',
        'a25','a26','a27','a28','a29','a30','a31','a32','a33',
        'a34','a35','a36','a37','a38','a39','a40',)

class AnswerWritingCheckForm(forms.ModelForm):

    class Meta:
        model = AnswerWritingChecked
        fields = ('band', 'fedback')

class AnswerSpeakingCheckForm(forms.ModelForm):

    class Meta:
        model = AnswerSpeakingChecked
        fields = ('band', 'fedback')