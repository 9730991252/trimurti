from django.shortcuts import render, redirect
from office.models import *
#from store.models import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta , date
from django.core.paginator import Paginator
# Create your views here.
def office_dashboard(request):
    if request.session.has_key('office_mobile'):
        office_mobile = request.session['office_mobile']
        context={}
        e=Office_employee.objects.filter(mobile=office_mobile).first()
        if e:
            status_event_lucky_day()
        context={
            'e':e,
        }
        return render(request, 'office/office_dashboard.html', context)
    else:
        return redirect('login')
    


def status_event_lucky_day():
    d = date.today() - timedelta(days=1)
    event = Event.objects.filter(status=1,event_day__lte=d)
    if event:
        for e in event:
            e.status = 0
            e.save()
    lucky_day = Lucky_day.objects.filter(status=1,lucky_day__lte=d)
    if lucky_day:
        for l in lucky_day:
            l.status = 0
            l.save()

def lucky_day(request):
    if request.session.has_key('office_mobile'):
        office_mobile = request.session['office_mobile']
        context={}
        e=Office_employee.objects.filter(mobile=office_mobile).first()
        if e:
            if 'Add_lucky_day'in request.POST:
                form_date = request.POST.get('date')
                today_date = date.today()
                if form_date >= str(today_date) :
                    dt = datetime.strptime(form_date, '%Y-%m-%d').date()
                    if Lucky_day.objects.filter(lucky_day=form_date).exists():
                        messages.warning(request,"Lucky Day Already Exists ") 
                    else:
                        Lucky_day(
                            office_employee_id = e.id,
                            lucky_day = form_date,
                            month = dt.month,
                            year = dt.year,
                            status = 1,
                        ).save()
                        return redirect('/office/lucky_day/')
                else:
                    messages.warning(request,"please Select Future Lucky Day")            
        context={
            'e':e,
            'lucky_day':Lucky_day.objects.filter(status=1).order_by('lucky_day')
        }
        return render(request, 'office/lucky_day.html', context)
    else:
        return redirect('login')
    

def event(request):
    if request.session.has_key('office_mobile'):
        office_mobile = request.session['office_mobile']
        context={}
        e=Office_employee.objects.filter(mobile=office_mobile).first()
        if e:
            if 'Add_Event'in request.POST:
                party_name = request.POST.get('party_name')
                persons = request.POST.get('persons')
                location = request.POST.get('location')
                event_day = request.POST.get('date')
                today_date = date.today()
                if event_day >= str(today_date) :
                    dt = datetime.strptime(event_day, '%Y-%m-%d').date()
                    Event(
                        office_employee_id = e.id,
                        party_name=party_name,
                        persons=persons,
                        location=location,
                        event_day = event_day,
                        month = dt.month,
                        year = dt.year,
                        status = 1,
                    ).save()
                    return redirect('/office/event/')
                else:
                    messages.warning(request,"please Select Future Event Day") 
            if 'Edit_Event'in request.POST:           
                id = request.POST.get('id')
                e_id = request.POST.get('e_id')
                party_name = request.POST.get('party_name')
                persons = request.POST.get('persons')
                location = request.POST.get('location')
                event_day = request.POST.get('date')
                if event_day == '':
                    e = Event.objects.get(id=id)
                    event_day = e.event_day
                    event_day = str(event_day)
                today_date = date.today()
                if event_day >= str(today_date) :
                    dt = datetime.strptime(event_day, '%Y-%m-%d').date()
                    Event(
                        id=id,
                        office_employee_id = e_id,
                        party_name=party_name,
                        persons=persons,
                        location=location,
                        event_day = event_day,
                        month = dt.month,
                        year = dt.year,
                        status = 1,
                    ).save()
                    return redirect('/office/event/')
                else:
                    messages.warning(request,"please Select Future Event Day") 
        context={
            'e':e,
            'event':Event.objects.filter(status=1).order_by('event_day')
        }
        return render(request, 'office/event.html', context)
    else:
        return redirect('login')


def office_profile(request):
    if request.session.has_key('office_mobile'):
        office_mobile = request.session['office_mobile']
        context={}
        e=Office_employee.objects.filter(mobile=office_mobile).first()
        if e:
            if 'edit_profile'in request.POST:
                name = request.POST.get('name')
                mobile = request.POST.get('mobile')
                pin = request.POST.get('pin')
                Office_employee(
                    id=e.id,
                    name = name,
                    mobile = mobile,
                    pin = pin
                ).save()
                del request.session['office_mobile']
        context={
            'e':e,
        }
        return render(request, 'office/office_profile.html', context)
    else:
        return redirect('login')
















