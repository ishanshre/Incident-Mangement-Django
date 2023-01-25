from django.contrib import admin

# Register your models here.
from core.models import (
    Incident,
    Team,
    TeamMember,
)

admin.site.register(Incident)
admin.site.register(Team)
admin.site.register(TeamMember)