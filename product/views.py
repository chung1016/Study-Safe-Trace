from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.
from django.views.generic import TemplateView
from urllib.request import urlopen
import json

context = {}

class basePage(TemplateView):
    template_name = "base.html"
    def get_context_data(self, **kwargs):
        context = {
            "subject": self.request.GET.get('HKU_id'),
            "date": f"{self.request.GET.get('date')}T12:00:00Z/"
        }        
        return context

class listVenues(TemplateView):
    template_name = "venues.html"
    def get_context_data(self, **kwargs):
        return self.getVenuesListFromAPI(self.request.GET.get('HKU_id'), self.request.GET.get('date'))

    def getVenuesListFromAPI(self, HKU_id, date):
        print(f"HKU_id: {HKU_id}, date:{date}")
        url = f"https://pure-lowlands-21595.herokuapp.com/venues/{HKU_id}/{date}T12:00:00Z/"
        response = urlopen(url)
        data_json = json.loads(response.read())
        print(data_json)
        context = {
            "subject": self.request.GET.get('HKU_id'),
            "date": datetime.strptime(f"{self.request.GET.get('date')}T12:00:00Z", "%Y-%m-%dT%H:%M:%SZ"),
            "venues": data_json['venues']
        }        
        print(context)
        return context

class listContacts(TemplateView):
    template_name = "contacts.html"
    def get_context_data(self, **kwargs):
        return self.getContactsListFromAPI(self.request.GET.get('HKU_id'), self.request.GET.get('date'))

    def getContactsListFromAPI(self, HKU_id, date):
        url = f"https://pure-lowlands-21595.herokuapp.com/contacts/{HKU_id}/{date}T12:00:00Z/"
        response = urlopen(url)
        data_json = json.loads(response.read())
        print(data_json)
        context = {
            "subject": self.request.GET.get('HKU_id'),
            "date": datetime.strptime(f"{self.request.GET.get('date')}T12:00:00Z", "%Y-%m-%dT%H:%M:%SZ"),
            "contacts": data_json['contacts']
        }     
        return context