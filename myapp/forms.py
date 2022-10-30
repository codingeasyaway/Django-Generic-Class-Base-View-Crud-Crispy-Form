from django import forms
from .models import Candidate
class candidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = "__all__"
        labels = {'careen': 'career'}