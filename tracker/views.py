from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView

from .models import Campaign, Placement


def campaign_list(request):
    campaigns = Campaign.objects.filter(status=1).order_by('end_date')
    return render(request, 'tracker/campaign_list.html', {'campaigns': campaigns})
