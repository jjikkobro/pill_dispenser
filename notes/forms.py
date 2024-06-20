from django import forms
from .models import Note, REPEAT_CHOICES, CONTAINER_CHOICES


class NoteModelForm(forms.ModelForm):
    dosing_time = forms.TimeField(widget=forms.TimeInput(attrs={"class":'timepicker', "placeholder":"HH:MM"}))
    repetition = forms.MultipleChoiceField(choices=REPEAT_CHOICES, widget=forms.CheckboxSelectMultiple(attrs={'class': 'repeat-checkbox'}))
    container = forms.ChoiceField(choices=CONTAINER_CHOICES)
    
    class Meta:
        model = Note
        fields = ['medicine', 'dosing_time', 'repetition', 'container']
