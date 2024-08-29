from django.shortcuts import render,redirect
from django.contrib import messages
from office.models import *
# Create your views here.
def sunil_home(request):
    if request.session.has_key('sunil_mobile'):
        context={}
        if 'add_employee'in request.POST:
            name=request.POST.get('name')
            mobile=request.POST.get('mobile')
            pin=request.POST.get('pin')
            if Office_employee.objects.filter(mobile=mobile).exists():
                messages.success(request,"Employee Allready Exits")
            else:
                Office_employee(
                    name=name,
                    mobile=mobile,
                    pin=pin,
                    ).save()
                messages.success(request,"Employee Add Succesfully") 
                return redirect('sunil_home')
        context={
            'e':Office_employee.objects.all()
        }
        return render(request, 'sunil/sunil_home.html', context)
    else:
        return redirect('sunil_login')