from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app1_hai(request):
    return render(request,'app1_hai.html')

def app_string(request):
    return HttpResponse('app_string')

