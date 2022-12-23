from django.shortcuts import render

from charityfinderapp.charityapp.forms import CharityForm
from charityfinderapp.charityapp.models import Charity


# Create your views here.

def addCharity(request):
    if request.method == "POST":
       from = CharityForm(request.POST)

       if form.is_valid():
          try:
              form.save()

          except:
              pass
       else:
           form = CharityForm()

def getAllData(request):
    charities = Charity.objects.all()

def edit(request,id):
    charity = Charity.object.get(id=id)