from django.http import Http404
from django.shortcuts import render
from .models import Hostels, Owner


def index(request):
    all_hostels = Hostels.objects.all()
    return render(request, 'hostels/index.html',{'all_hostels':all_hostels})


def detail(request, hostels_id):
    try:
        hostels =Hostels.object.get(pk=hostels_id)
    except Hostels.DoesNotExist:
        raise Http404("Hostel Does no exist")
    return render(request, 'hostels/detail.html', {'hostels':hostels})



