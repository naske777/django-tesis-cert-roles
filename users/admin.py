from django import forms
from django.contrib import admin
from .models import UserProfile
from students.models import Students

class UserProfileAdminForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tutor_students'].queryset = Students.objects.all()
        self.fields['tutor_students'].label_from_instance = lambda obj: f"{obj.name}"

class UserProfileAdmin(admin.ModelAdmin):
    form = UserProfileAdminForm

admin.site.register(UserProfile, UserProfileAdmin)