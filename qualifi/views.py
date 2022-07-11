from dataclasses import fields
from django.shortcuts import redirect, render
from .models import QualifiCampaign
from .forms import CampaignForm, CampaignUpdateForm
from django.http import HttpResponseRedirect
# importing pagination 
from django.core.paginator import Paginator
from django.db.models import Q
#from drf_multiple_model.views import FlatMultipleModelAPIView
# Create your views here.
def delete_campaign(request, campaign_id):
    camp = QualifiCampaign.objects.get(pk=campaign_id)
    camp.delete()
    return redirect('list-campaign')


def update_campaign(request,campaign_id):
    camp = QualifiCampaign.objects.get(pk=campaign_id)
    form = CampaignUpdateForm(request.POST or None, instance=camp)
    if form.is_valid():
        form.save()
        return redirect('missing-campaign')
    context = {'camp':camp, 'form':form}
    return render(request, 'update_campaign.html', context)

def update_missinginfo_camapign(request):
    #camps = QualifiCampaign.objects.all().filter(brand__isnull=True).values() | QualifiCampaign.objects.all().filter(start_date__isnull=True).values() | QualifiCampaign.objects.all().filter(end_date__isnull=True).values() | QualifiCampaign.objects.all().filter(impression_goal__isnull=True).values()
    count = QualifiCampaign.objects.filter(Q(start_date__isnull=True) | Q(end_date__isnull=True) | Q(impression_goal__isnull=True)).count()
    p = Paginator(QualifiCampaign.objects.all().filter(brand__isnull=True).values() | QualifiCampaign.objects.all().filter(start_date__isnull=True).values() | QualifiCampaign.objects.all().filter(end_date__isnull=True).values() | QualifiCampaign.objects.all().filter(impression_goal__isnull=True).values(), 7)
    page = request.GET.get('page')
    campaign_page = p.get_page(page)
    #form = CampaignUpdateForm(request.POST or None, instance=camp)
    # if form.is_valid():
    #     form.save()
    #     return redirect('list-campaign')
    context = { 'count':count, 'campaign_page': campaign_page}
    return render(request,'missing_campaign.html', context)

def home(request):
    posts = QualifiCampaign.objects.all()
    context = {'posts':posts}
    return render(request, 'home.html', context)

def add_campaign(request):
    submitted = False
    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_campaign?submitted=True')

    else:
        form = CampaignForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'view_campaign.html',{'form':form, 'submitted':submitted})

def list_campaign(request):
    campaigns = QualifiCampaign.objects.all().order_by('campaign')
    p = Paginator(QualifiCampaign.objects.all().order_by('campaign'), 7)
    page = request.GET.get('page')
    campaign_page = p.get_page(page)
    context = {'campaigns':campaigns, 'campaign_page':campaign_page}
    return render(request, 'campaigns.html', context)

def show_campaign(request, campaign_id):
    camp = QualifiCampaign.objects.get(pk=campaign_id)
    context = {'camp':camp}
    return render(request, 'show_campaigns.html', context)

def search_camps(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        camps = QualifiCampaign.objects.filter(campaign__contains=searched).order_by('campaign')
        p = Paginator(QualifiCampaign.objects.filter(campaign__contains=searched).order_by('campaign'), 7)
        page = request.GET.get('page')
        campaign_page = p.get_page(page)
        context = {'searched':searched, 'campaign_page':campaign_page}
        return render(request, 'search_camps.html', context)
    else:
         context = {}
         return render(request, 'search_camps.html', context)

