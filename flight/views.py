from django import forms
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from flight.forms import FlightForm
from flight.models import Flight
from service.models import Service


def flight(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    flights = Flight.objects.filter(
        Q(flightNo__icontains=q) |
        Q(origin__locationName__icontains=q)
    )

    flight_count = flights.count()

    context = {'flights': flights,
               'flight_count': flight_count, }
    return render(request, "flight/flight.html", context)


def flightShow(request, pk):
    flight = Flight.objects.get(id=pk)

    context = {'flight': flight, }
    return render(request, "flight/flightCRUD.html", context)


def createFlight(request):
    form = FlightForm(request.POST or None)
    messages=[]
    if request.method == 'POST':
        if form.is_valid():
            edt = form.cleaned_data.get('edt')
            estimatedDuration = form.cleaned_data.get('estimatedDuration')
            originId = form.cleaned_data.get('origin').id
            origin = Service.objects.get(id=originId)
            destinationId = form.cleaned_data.get('destination').id
            destination = Service.objects.get(id=destinationId)

            Flight.objects.create(
                flightNo=request.POST.get('flightNo'),
                edt=edt,estimatedDuration=estimatedDuration,origin=origin,destination=destination,
            )
            return redirect('flight')
        else:
            messages.append(form.errors)

    services=Service.objects.all()
    context = {'form': form, 'services': services, 'messages': messages}
    return render(request, 'flight/flight_form.html', context)



def updateFlight(request, pk):
    flight = get_object_or_404(Flight, id=pk)
    form = FlightForm(request.POST or None, instance=flight)
    messages=[]
#    if request.user != room.host:
#        return HttpResponse('Your are not allowed here!!')

    if request.method == 'POST':
        # form1=form.full_clean()
        if form.is_valid():
            flight.flightNo = form.cleaned_data.get('flightNo')
            flight.origin = Service.objects.get(id=request.POST.get('origin'))
            flight.destination = Service.objects.get(id=request.POST.get('destination'))
            flight.edt = request.POST.get('edt')
            flight.estimatedDuration = request.POST.get('estimatedDuration')

            flight.save()
            return redirect('flight')
        else:
            messages.append(form.errors)
            #'Origin and Destination cannot be equal!!')

    services=Service.objects.all()
    context = {'form': form, 'flight': flight, 'services': services, 'messages':messages}
    return render(request, 'flight/flight_form.html', context)

def deleteFlight(request, pk):
    flight = Flight.objects.get(id=pk)
#    if request.user != room.host:
#        return HttpResponse('Your are not allowed here!!')
    if request.method == 'POST':
        flight.delete()
        return redirect('flight')
    return render(request, 'flight/delete.html', {'obj': flight})

