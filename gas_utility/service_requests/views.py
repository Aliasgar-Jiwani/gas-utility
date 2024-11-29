from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('request_tracking')
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/submit_request.html', {'form': form})

@login_required
def request_tracking(request):
    requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'service_requests/request_tracking.html', {'requests': requests})
