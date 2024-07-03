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
from fiboapp.models import FiboModel

def index(request):
    return HttpResponse("Hello, Welcome to III ECE Fibo website")

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_post(request):
    l = []
    s = ''
    if request.method == 'POST':
        try:
            fn = int(request.POST.get('n'))
            if fn <0:
                s = "Negative value entered... Enter a positive integer"
                return render(request,'fibo - Copy.html', {'posts': [s]},)
            else:
                for i in range(0,fn):
                    #l.append(fib(i))
                    s = s +' '+str(fib(i))
                FiboModel(numstr=fn,terms =s,).save()          
                return render(request,'fibo - Copy.html', {'posts': [s]},)
                #return HttpResponseRedirect('/fiboapp/fibarchive')    
        except ValueError:
            s = "Text entered... Enter a positive integer"
            return render(request,'fibo - Copy.html', {'posts': [s]},)
            #return HttpResponseRedirect('/fiboapp/fibarchive')    
           
def fib_archive(request):
    posts = FiboModel.objects.all()
    return render(request,'fibo - Copy.html', {'posts': posts})

