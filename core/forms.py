from django import forms

from core.models import Incident, Team, TeamMember

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
    assign_incident = forms.BooleanField(widget=forms.HiddenInput)
    class Meta:
        model = Incident
        fields = ["assigned_to",]


class IncidentStatusUpdateForm(forms.ModelForm):
    status_update = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Incident
        fields = ['acknowledged','resolved']

class UpdateTeamDetail(forms.ModelForm):
    update_detail = forms.BooleanField(widget=forms.HiddenInput, initial=True)
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



class AddNewTeamMember(forms.ModelForm):
    add_member = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = TeamMember
        fields = [
            'profile'
        ]
        labels = {
            'profile':'Member'
        }