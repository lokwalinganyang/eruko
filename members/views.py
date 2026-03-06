from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import SaccoForm
from .forms import MemberRegistrationForm  # Ensure this matches your forms.py

def register(request):
    if request.method == 'POST':
        form = MemberRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')
    else:
        form = MemberRegistrationForm()
    return render(request, 'members/register.html', {'form': form})

@login_required
def dashboard(request):
    # This is the function that was missing!
    forms = SaccoForm.objects.all().order_by('-uploaded_at')
    return render(request, 'members/dashboard.html', {'forms': forms})