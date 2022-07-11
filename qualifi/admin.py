from email.headerregistry import Group
from django.apps import apps
from django.contrib import admin
from .models import *
from django.apps import apps
# Register your models here.
@admin.register(QualifiCampaign)
class CampaignAdmin(admin.ModelAdmin):
    ordering = ('campaign',)
#admin.site.register(QualifiCampaign)
#admin.site.register(QualifiBrand)
@admin.register(QualifiBrand)
class CampaignAdmin(admin.ModelAdmin):
    ordering = ('brand',)
#admin.site.register(QualifiAgency)
@admin.register(QualifiAgency)
class CampaignAdmin(admin.ModelAdmin):
    ordering = ('agency',)

#admin.site.unregister(Group)

# x = apps.get_models()
# for model in x:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#             pass
