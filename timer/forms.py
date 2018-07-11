from django import forms

from .models import Activity

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['activity_title', 'activity_time']
