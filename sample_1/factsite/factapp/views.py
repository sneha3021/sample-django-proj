from django.shortcuts import render


#from datetime import datetime
from django.shortcuts import render
#from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from datetime import datetime
from django.template import RequestContext
from django.http import HttpResponseRedirect
from factapp.models import FactModel

def index(request):
    return HttpResponse("Hello, Welcome to III CSE")

def fact(n):
   if n ==0:
       return 1
   elif n == 1:
       return n
   else:
       return n*fact(n-1)
    
def fact_post(request):
    
    if request.method == 'POST':
        try:
            n = int(request.POST.get('n'))
            if n <0:
                f = "Invalid .. Enter a positive integer"
                return render(request,'fact.html', {'posts': [f]},)
                
            else:
                f = fact(n)
                FactModel(numstr=str(n),fact_val=str(f),).save()          
                return render(request,'fact.html', {'posts': [f]},)
                
        except ValueError:
            f = "Text found....Enter a positive integer"
            return render(request,'fact.html', {'posts': [f]},)
            #return HttpResponseRedirect('/factapp/factarchive')    

def fact_archive(request):
    posts = FactModel.objects.all()
    return render(request,'fact.html', {'posts': posts})

