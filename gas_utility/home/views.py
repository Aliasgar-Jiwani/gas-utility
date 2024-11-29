from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from service_requests.models import ServiceRequest

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return dashboard(request)
    return render(request, 'home/home.html')

@login_required
def dashboard(request):
    service_requests = ServiceRequest.objects.filter(customer=request.user).order_by('-submission_date')[:5]
    context = {
        'service_requests': service_requests,
    }
    return render(request, 'home/dashboard.html', context)
