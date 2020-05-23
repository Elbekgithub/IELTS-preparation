from django import forms
from .models import AnswerWritingStudent, AnswerSpeakingStudent
class MockRegisterForm(forms.Form):
    pass

class AnswerWritingForm(forms.ModelForm):
    class Meta:
        model = AnswerWritingStudent
        fields = ('task1', 'task2', 'pdf', )