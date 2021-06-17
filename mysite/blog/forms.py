from django import forms
from .models import timetable

class postForm(forms.ModelForm):
    
    class Meta:
        model = timetable
        fields = ('email', 'raw_data',)
        