from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse_lazy

from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, DeleteView

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from core.models import Incident, Team
from core.forms import (
    AddIncidentForm,
    AssignIncidentForm, 
    UpdateTeamDetail
)
# Create your views here.
def index(request):
    incidents = Incident.objects.all()
    context = {
        "incidents":incidents,
    }
    return render(request, "index.html", context)


class IncidentDetailView(View):
    template_name = 'manage/incidents/detail_incident.html'
    def get(self,request, *args, **kwargs):
        incident = get_object_or_404(Incident, id=self.kwargs['pk'])
        assign_incident_form = AssignIncidentForm(instance=incident)
        context = {
            'incident':incident,
            'assign_incident_form':assign_incident_form,
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        incident = get_object_or_404(Incident, id=self.kwargs['pk'])
        assign_incident_form = AssignIncidentForm(request.POST, instance=incident)
        if assign_incident_form.is_valid():
            assign_incident_form.save()
            messages.success(request, "Successfull assigned incident to the team")
            return redirect("core:detailIncident", pk=incident.pk)
        context = {
            'incident':incident,
            'assign_incident_form':assign_incident_form,
        }
        return render(request, self.template_name, context)


class AddIncidentView(SuccessMessageMixin,CreateView):
    form_class = AddIncidentForm
    template_name = "manage/incidents/add_incident.html"
    success_message = "Incident Reported"
    success_url = reverse_lazy("core:index")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.reported_by = self.request.user.profile
            form.instance.save()
        return super().form_valid(form)

class IncidentDeleteView(SuccessMessageMixin, DeleteView):
    model = Incident
    template_name = "manage/incidents/delete_incident.html"
    success_url = reverse_lazy("core:index")
    success_message = "Incident Deleted Successfully"


class TeamsListView(ListView):
    model = Team
    template_name = "manage/teams/team_list.html"
    context_object_name = 'teams'


class TeamDetailView(View):
    template_name = "manage/teams/team_detail.html"
    def get(self, request, *args, **kwargs):
        team = get_object_or_404(Team, id=self.kwargs['pk'])
        update_detail = UpdateTeamDetail(instance=team)
        context = {
            'team':team,
            'update_detail':update_detail,
        }
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        team = get_object_or_404(Team, id=self.kwargs['pk'])
        update_detail = UpdateTeamDetail(request.POST, instance=team)
        if update_detail.is_valid():
            update_detail.save()
            messages.success(request, "Team Detail Updated Successfully")
            return redirect('core:teamDetail', pk=team.pk)
        context = {
            'team':team,
            'update_detail':update_detail,
        }
        return render(request, self.template_name, context)