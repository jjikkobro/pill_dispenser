from django import forms
from .models import Note, REPEAT_CHOICES, CONTAINER_CHOICES


class NoteModelForm(forms.ModelForm):
    dosing_time = forms.TimeField(widget=forms.TimeInput(attrs={"class":'timepicker'}))
    repetition = forms.MultipleChoiceField(choices=REPEAT_CHOICES, widget=forms.CheckboxSelectMultiple)
    container = forms.ChoiceField(choices=CONTAINER_CHOICES)
    
    class Meta:
        model = Note
        fields = ['medicine', 'dosing_time', 'repetition', 'container']
