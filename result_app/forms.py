from django import forms
from .models import Student, Marks

class StudForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('studname','studroll','coursename','branchname','sem','mobile','adhar','gen','add','city','state','country','dob','father','mother','religion','category','reg','year','session')

class MarkForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['roll','subcode','marks','sheet']
