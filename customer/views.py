from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from .models import ServiceRequest
from django.contrib.auth.decorators import login_required

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('track_request')
    else:
        form = ServiceRequestForm()
    return render(request, 'customer/submit_request.html', {'form': form})

@login_required
def track_request(request):
    requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'customer/track_request.html', {'requests': requests})
