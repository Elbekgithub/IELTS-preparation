from django.contrib import admin

from .models import AnswerReadingStudent, AnswerWritingStudent, AnswerListeningStudent, AnswerSpeakingStudent

admin.site.register(AnswerReadingStudent)
admin.site.register(AnswerSpeakingStudent)
admin.site.register(AnswerListeningStudent)
admin.site.register(AnswerWritingStudent)