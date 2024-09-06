from django.shortcuts import render
from office.models import *
from django.template.loader import render_to_string
from django.http import JsonResponse
import requests

# Create your views here.
def search_lucky_day(request):
    if request.method == 'GET':
        year = request.GET['year']
        month = request.GET['month']
        day = Lucky_day.objects.values().filter(status=1,year=year,month=month)
        lucky_day = list(day)
        #print(lucky_day)
    return JsonResponse({'lucky_day':lucky_day})

def search_event_day(request):
    if request.method == 'GET':
        year = request.GET['year']
        month = request.GET['month']
        day = Event.objects.values().filter(status=1,year=year,month=month)
        event_day = list(day)
    return JsonResponse({'event_day':event_day})

def event_detail(request):
    if request.method == 'GET':
        day = request.GET['day']
        month = request.GET['month']
        year = request.GET['year']
        date = f"{year}-{month}-{day}"
        event = Event.objects.filter(status=1,event_day=date)
        context={
            'event':event,
            'event_count':event.count(),
            'date':f"{day}-{month}-{year}"
        }
        t = render_to_string('ajax/office/event_detail.html', context)
    return JsonResponse({'t':t})




def indraprastha_booking(request):
    if request.method == 'GET':
        k_id = 5
        y = request.GET['y']
        m = request.GET['m']
        #print(f'{k_id}')
        URL = "https://bookkaryalay.com/api/indraprastha/"
        chk=f"{k_id}/{m}/{y}"
        ur=URL+chk
        r = requests.get(url=ur)
        book = r.json()
    return JsonResponse(book)

























