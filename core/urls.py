from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('manage/incident/add', views.AddIncidentView.as_view(), name="addIncident"),
    path('manage/teams/all', views.TeamsListView.as_view(), name="teamsList"),
    path('manage/teams/<int:pk>/detail', views.TeamDetailView.as_view(), name="teamDetail"),
]