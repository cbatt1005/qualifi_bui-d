from dataclasses import fields
from django import forms
from django.forms import ModelChoiceField, ModelForm
from .models import QualifiBrand, QualifiCampaign
from django.forms.widgets import NumberInput


# create campaign form

class CampaignForm(ModelForm):
    class Meta:
        model = QualifiCampaign
        fields = ('brand','campaign','start_date','end_date','impression_goal')
        labels = {
            'brand': '',
            'campaign':'',
            'start_date': '',
            'end_date': '',
            'impression_goal': '',
        }
        widgets = {
            'brand': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Brand'}),
            'campaign': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Campaign'}),
            'start_date': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Start Date'}),
            'end_date': forms.DateInput(attrs={'class':'form-control', 'placeholder':'End Date'}),
            'impression_goal': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Impressions Goal'}),
        }

class CampaignUpdateForm(ModelForm):
    class Meta:
        model = QualifiCampaign
        fields = ('agency','platform','channel','advertiser_name','market','csm','sales','brand','campaign','start_date','end_date','impression_goal')
        brand = forms.ModelChoiceField(queryset=QualifiBrand.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
        start_date = forms.DateField()
        end_date = forms.DateField()
        labels = {
            'agency': '',
            'platform':'',
            'channel': '',
            'advertiser_name': '',
            'market': '',
            'csm': '',
            'sales': '',
            'brand': '',
            'campaign': '',
            'start_date': '',
            'end_date': '',
            'impression_goal': '',
        
        }
        widgets = {
            'agency': forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
            'platform': forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
            'channel': forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
            'advertiser_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Advertiser Name'}),
            'market': forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
            'csm': forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
            'sales': forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
            'brand': forms.Select(attrs={'class':'form-control', 'placeholder':'Enter Brand'}),
            'campaign': forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
            'start_date': forms.NumberInput(attrs={'type': 'date', 'class':'form-control'}),
            'end_date': forms.NumberInput(attrs={'type': 'date', 'class':'form-control'}),
            'impression_goal': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Enter Impression Goal'}),
        }
