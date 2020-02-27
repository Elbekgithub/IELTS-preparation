from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()

from .models import Teacher, Student



class TeacherInline(admin.StackedInline):
    model = Teacher
    can_delete = False
    verbose_name_plural = 'teacher'

class UserAdmin(BaseUserAdmin):
    inlines = (TeacherInline,)
    list_display = ('email', 'username', 'is_teacher', 'is_student')
    list_filter = ('is_teacher', 'is_student')
    fieldsets = (
        ('Required Fields', {'fields': ('email',)}),
        ('Personal info', {'fields': ('username','first_name', 'last_name',)}),
        ('Permissions', {'fields': ( 'is_student', 'is_teacher')}),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.register(Student)

# Register your models here.
