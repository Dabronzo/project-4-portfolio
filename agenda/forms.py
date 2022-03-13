from django import forms
from .models import Gig
from django.forms import ModelForm


class DateInput(forms.DateInput):
    """Class to overwrite the DateTimeInput of Django"""
    input_type = 'date'



class GigCreateForm(ModelForm):
    """Class form for create Gigs"""

    event_date = forms.DateField(widget=DateInput(attrs={'class': 'form-control', 'placeholder': ''}))
    is_payed = forms.BooleanField(required=False)

    class Meta:
        """Meta class"""

        model = Gig
        fields = ('event_name', 'event_date', 'start_time', 'play_time', 'dj', 'status', 'venue', 'fees', 'info_notes', 'is_payed')

        widgets = {
            'event_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
            'start_time': forms.TextInput(attrs={'class': 'form-control'}),
            'play_time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Set play time: E.g. 2hours'}),
            'dj': forms.Select(attrs={'class': 'form-select form-control', 'placeholder': 'DJ'}),
            'status': forms.Select(attrs={'class': 'form-select form-control', 'placeholder': 'Select the status of the gig'}),
            'venue': forms.Select(attrs={'class': 'form-select form-control','placeholder': 'Select a venue'}),
            'fees': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'info_notes': forms.Textarea(attrs={'class': 'form-control'}),
        }
