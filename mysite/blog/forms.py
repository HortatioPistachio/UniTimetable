from django import forms
from .models import timetable, iCal_calendar

class postForm(forms.ModelForm):
    
    class Meta:
        model = timetable
        fields = ('email', 'raw_data', 'colour','cal_type')


class postFormiCal(forms.ModelForm):
    class Meta:
        model=timetable
        fields = ('raw_data',)


class postFormGoogle(forms.ModelForm):
    class Meta:
        model=timetable
        fields = ('email', 'raw_data', 'colour')
        

class iCalForm(forms.ModelForm):
    class Meta:
        model = iCal_calendar
        fields = ('cal',)
        