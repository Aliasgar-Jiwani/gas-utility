from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class CustomerRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'address', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
            # Create or update customer profile
            profile = user.profile
            profile.phone_number = self.cleaned_data['phone_number']
            profile.address = self.cleaned_data['address']
            profile.save()
            
        return user
