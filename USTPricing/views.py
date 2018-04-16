from django.shortcuts import render
from django.http import HttpResponse

from .models import USTContract

def index(request):
    latest_contract_list = USTContract.objects.order_by('-pub_date')[:5]
    context = {'latest_contract_list': latest_contract_list}
    return render(request, 'USTPricing/index.html', context)

def results(request, evepraisalID):
    contract = USTContract.objects.get(evepraisalID=evepraisalID)
    context = {'contract': contract}
    return render(request, 'USTPricing/results.html', context)
