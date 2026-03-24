from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='accounts:login_form')
def home_page(request):
    return render(request, 'base.html')