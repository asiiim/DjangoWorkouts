from django.contrib import admin

# Register your models here.
from .models import User, Lead, Agent

# This updates to view the list of model in the admin view interface
admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Agent)