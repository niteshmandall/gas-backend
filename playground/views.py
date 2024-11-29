from django.shortcuts import render
from django.http import HttpResponse

from customer.views import track_request


# Create your views here.


def say_hello(request):
    return render(request, 'customer/track_request.html')
