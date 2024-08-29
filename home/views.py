from django.shortcuts import render,redirect
from office.models import *
from django.contrib import messages
# Create your views here.
def index(request):
    #o = Office_employee.objects.get(name='keshaw talekar')
    #o.name = 'Keshav Talekar'
    #o.save()
    return render(request, 'home/index.html')


def login(request):
    if request.session.has_key('office_mobile'):
        return redirect('office_dashboard')
    else:
        if request.method == "POST":
            number=request.POST ['number']
            pin=request.POST ['pin']
            e= Office_employee.objects.filter(mobile=number,pin=pin,status=1)
            if e:
                request.session['office_mobile'] = request.POST["number"]
                return redirect('office_dashboard')
            else:
                messages.success(request,"please insert correct information or call more suport 9730991252")            
                return redirect('login')
    return render(request, 'home/login.html')


def sunil_login(request):
    if request.method == 'POST':
        a =int(request.POST["number"])
        b =int(request.POST["pin"])
        s = a+b
        if s == 10000 :
            request.session['sunil_mobile'] = s
            return redirect('sunil_home')
        else:
            return redirect('sunil_login')
    return render(request, 'home/sunil_login.html')



def office_logout(request):
    if request.session.has_key('office_mobile'):
        del request.session['office_mobile']
    return redirect('login')
























































































































































































































































































































