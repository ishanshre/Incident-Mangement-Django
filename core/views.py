from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from django.views.generic import ListView

from django.contrib.messages.views import SuccessMessageMixin

from core.models import Incident, Team
from core.forms import AddIncidentForm
# Create your views here.
def index(request):
    incidents = Incident.objects.all()
    context = {
        "incidents":incidents,
    }
    return render(request, "index.html", context)


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


class TeamsListView(ListView):
    model = Team
    template_name = "manage/teams/team_list.html"
    context_object_name = 'teams'