from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from service.forms import ServiceForm
from service.models import Service


def service(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    services = Service.objects.filter(
        Q(locationCode__icontains=q) |
        Q(locationCode__icontains=q)
    )

    service_count = services.count()

    context = {'services': services,
               'service_count': service_count, }
    return render(request, "service/service.html", context)


def serviceShow(request, pk):
    service = Service.objects.get(id=pk)

    context = {'service': service, }
    return render(request, "service/serviceCRUD.html", context)

@login_required(login_url='login')
def createService(request):
    form = ServiceForm(request.POST or None)
    messages=[];

    if request.method == 'POST':
        #       topic_name = request.POST.get('topic')
        #       topic, created = Topic.objects.get_or_create(name=topic_name)
        if form.is_valid():
            Service.objects.create(
                locationName=request.POST.get('locationName'),
                locationCode=form.cleaned_data.get('locationCode'),
                user=request.user.__str__()
            )
            return redirect('service')
        messages=form.errors
    context = {'form': form,'messages':messages}
    return render(request, 'service/service_form.html', context)

@login_required(login_url='login')
def updateService(request, pk):
    service = get_object_or_404(Service, id=pk)
    form = ServiceForm(request.POST or None, instance=service)
    messages=[]
    if request.method == 'POST':
        if form.is_valid():
            service.locationName = request.POST.get('locationName')
            service.locationCode = form.cleaned_data.get('locationCode')
            service.user = request.user.__str__()
            service.save()
            return redirect('service')
        else:
            messages.append(form.errors)
    context = {'form': form, 'service': service,'messages':messages}
    return render(request, 'service/service_form.html', context)

@login_required(login_url='login')
def deleteService(request, pk):
    service = Service.objects.get(id=pk)
#    if request.user != room.host:
#        return HttpResponse('Your are not allowed here!!')
    if request.method == 'POST':
        service.delete()
        return redirect('service')
    return render(request, 'service/delete.html', {'obj': service})

