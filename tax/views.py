from django.shortcuts import render
from django.http import HttpResponse

variable = 0.15
def index (request):
    return render(request, 'tax/index.html')

def taxn (request , num):
    try:
        int(num)
        num= num + num*variable
    except ValueError:
        print('please enter number')
    return HttpResponse(f"the number is {num}")

def taxrate (request ):
    r = variable * 100
    return render(request, 'tax/taxrate.html', {'variable': r})
   
   