from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import USTContract
from .forms import ContractForm

def index(request):
    if request.method == "POST":
        form = ContractForm(request.POST)
        #print(form)

        if form.is_valid():
            if USTContract.objects.filter(evepraisalURL=request.POST['evepraisalURL']).exists():
                #print("exists")
                d = USTContract.objects.get(evepraisalURL=request.POST['evepraisalURL'])
                return redirect('results', evepraisalID=d.evepraisalID)
            else:
                #print("doesn't exist")
#                form.save()

                c = USTContract(evepraisalURL=form.cleaned_data['evepraisalURL'], rush=form.cleaned_data['rush'], altloc=form.cleaned_data['altloc'])
                c.getData()
                c.save()

            return redirect('results', evepraisalID=c.evepraisalID)
            
    else:
        form = ContractForm()

    return render(request, 'USTPricing/index.html', {'form': form})

def results(request, evepraisalID):
    contract = USTContract.objects.get(evepraisalID=evepraisalID)
    context = {'contract': contract}
    return render(request, 'USTPricing/results.html', context)
