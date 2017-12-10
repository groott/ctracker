from django.contrib import admin

from .models import Client, Campaign, Publisher, Placement

class PlacementInline(admin.TabularInline):
    model = Placement
    extra = 1


class CampaignAdmin(admin.ModelAdmin):
    inlines = [PlacementInline,]

admin.site.register(Client)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Publisher)
admin.site.register(Placement)
