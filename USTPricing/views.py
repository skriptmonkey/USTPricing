from django.shortcuts import render
from django.http import HttpResponse

from .models import USTContract

def index(request):
    return render(request, 'USTPricing/index.html')

def results(request):
    if USTContract.objects.filter(evepraisalURL=request.POST['evepraisalURL']).exists():
        c = USTContract.objects.get(evepraisalURL=request.POST['evepraisalURL'])
        contract = c
    else:
        c = USTContract(evepraisalURL=request.POST['evepraisalURL'])
        c.getData()
        c.save()
        contract = USTContract.objects.get(evepraisalID=c.evepraisalID)

    context = {'contract': contract}
    return render(request, 'USTPricing/results.html', context)
