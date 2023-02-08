from django import forms

from core.models import Incident

class AddIncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = [
            'title',
            'urgency',
            'triggered',
            'acknowledged',
            'description',
        ]


class AssignIncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ["assigned_to",]
