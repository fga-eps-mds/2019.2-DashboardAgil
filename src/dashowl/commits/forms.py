from django import forms

from .models import Commit

class FormularioCommits(forms.ModelForm):
    class Meta:
        model = Commit
        fields = [
            'shaCommit', 
            'totalCommits',
            'author'
        ]