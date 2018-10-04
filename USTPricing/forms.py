from django.forms import ModelForm
from USTPricing.models import USTContract, USTResult

class ContractForm(ModelForm):
    class Meta:
        model = USTContract
        fields = ['evepraisalURL', 'rush', 'altloc']
