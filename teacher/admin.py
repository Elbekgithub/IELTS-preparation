from django.contrib import admin


from .models import (MockTest, Listening, Reading, Writing, Speaking, AnswerListening, AnswerReading,)
# Register your models here.

admin.site.register(MockTest)
admin.site.register(Listening)
admin.site.register(Reading)
admin.site.register(Writing)
admin.site.register(Speaking)
admin.site.register(AnswerReading)
admin.site.register(AnswerListening)