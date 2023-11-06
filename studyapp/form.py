from django import forms
from .models import Assignment


class AssignmentForm(forms.ModelForm):
    dueDate = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    class Meta:
        model = Assignment
        fields = ['title', 'course', 'description', 'dueDate']


class DocForm(forms.Form):
    doc_file = forms.FileField(
        label='Select a file',
        help_text='max 2 GB'
    )
