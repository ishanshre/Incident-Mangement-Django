"""
    Creating Models for Incident Management System
"""
from django.db import models

from django.urls import reverse


from accounts.models import Profile

# Create your models here.

class Team(models.Model):
    """Model for team """
    team_name = models.CharField(max_length=255)
    team_description = models.TextField(blank=True, null=True)
    on_call = models.BooleanField(default=False)
    shift_date = models.DateTimeField(null=True, blank=True)
    shift_end_date = models.DateTimeField(null=True, blank=True)
    leader = models.ForeignKey(Profile, on_delete=models.SET_NULL, related_name="team_leader", null=True)
    def __str__(self):
        return f"{self.team_name} lead by {self.leader.user.username.title()}"
    
    def get_absolute_url(self):
        return reverse("core:teamDetail", args=[self.id])

class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="members")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="member_of")

    def __str__(self):
        return f"Member of team : {self.team.team_name}"

class Incident(models.Model):
    """Model for incidents happed"""
    class URGENCY_LEVEL(models.IntegerChoices):
        LOW = 0, 'Low'
        MEDIUM = 1, 'Medium'
        HIGH = 2, 'High'
        

    urgency  = models.IntegerField(choices=URGENCY_LEVEL.choices, default=URGENCY_LEVEL.LOW)
    triggered = models.BooleanField(default=False)
    acknowledged = models.BooleanField(default=False)
    resolved = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    reported_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="incidents", null=True, blank=True)
    assigned_to = models.ForeignKey(Team, on_delete=models.SET_NULL, related_name="incidents", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse("core:detailIncident", args=[self.id])