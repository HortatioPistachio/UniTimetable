from django import forms
from .models import timetable, iCal_calendar

class postForm(forms.ModelForm):
    
    class Meta:
        model = timetable
        fields = ('email', 'raw_data', 'cal_type')


class iCalForm(forms.ModelForm):
    class Meta:
        model = iCal_calendar
        fields = ('cal',)
        