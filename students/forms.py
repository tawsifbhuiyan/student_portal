from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student  # Specify the model to which the form is bound
        fields = ['name', 'age', 'address']  # Define the fields to be included in the form
