from django.http import HttpResponseRedirect
from django.shortcuts import render

from home.forms import RegistrationForm
from .models import CompanyHomePageDisplay
# Create your views here.
def index(request):
   return render(request,'pages/home.html')
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})