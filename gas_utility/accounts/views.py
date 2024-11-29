from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from .forms import UserUpdateForm, CustomerRegistrationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = form.save(commit=False)
                    user.save()
                    
                    # Update profile
                    profile = user.profile
                    profile.phone_number = form.cleaned_data['phone_number']
                    profile.address = form.cleaned_data['address']
                    profile.save()
                    
                    messages.success(request, 'Registration successful! Please login with your credentials.')
                    return redirect('login')
            except Exception as e:
                messages.error(request, f'An error occurred during registration. Please try again.')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def account_info(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account_info')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'accounts/account_info.html', {'form': form})
