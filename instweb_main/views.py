from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main_pg(request):
    return render(request, 'index.html')
