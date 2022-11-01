from django.shortcuts import render
from .models import Company
# Create your views here.

def list(request):
    Data = {'Companies': Company.objects.all()}
    return render(request, 'company/company.html', Data)
def detail(request, id):
    detail = Company.objects.get(id=id)
    return render(request, 'company/companyDetail.html', {'detail': detail})
