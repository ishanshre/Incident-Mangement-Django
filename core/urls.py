from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('manage/incident/add', views.AddIncidentView.as_view(), name="addIncident"),
]