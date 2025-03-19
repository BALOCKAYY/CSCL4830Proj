from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import Todo

class TodoForm(forms.ModelForm):
    due = forms.DateField(
        input_formats=['%m/%d/%Y'],  # Expects input in MM/DD/YYYY format
        widget=forms.DateInput(format='%m/%d/%Y', attrs={'placeholder': 'MM/DD/YYYY'}),
        error_messages={'invalid': 'Please enter the date in MM/DD/YYYY format.'}
    )

    class Meta:
        model = Todo
        fields = ['todo', 'due']

    def clean_due(self):
        due_date = self.cleaned_data['due']
        today = date.today()

        # Ensure the year is 2025 or later
        if due_date.year < 2025:
            raise ValidationError("Year must be 2025 or later.")

        # If the due date is in the current year, check that it is not in the past
        if due_date.year == today.year:
            # Compare (month, day) tuples to determine if the due date has already passed
            if (due_date.month, due_date.day) < (today.month, today.day):
                raise ValidationError("The month and day cannot be a date that has already passed this year.")
                
        return due_date

