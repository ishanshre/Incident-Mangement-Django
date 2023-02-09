from django import forms

from core.models import Incident, Team

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


class UpdateTeamDetail(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            'team_name',
            'team_description',
            'on_call',
            'shift_date',
            'shift_end_date',
            'leader',
        ]