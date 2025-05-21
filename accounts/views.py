from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()



def home_view(request):
    return render(request, 'accounts/home.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('login')  # We'll make login soon
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_exists = User.objects.filter(username=username).exists()

        if not user_exists:
            messages.error(request, "Invalid username.")
        elif not form.is_valid():
            messages.error(request, "Invalid password.")
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.user_type == 'patient':
                    return redirect('patient_dashboard')
                elif user.user_type == 'doctor':
                    return redirect('doctor_dashboard')
            else:
                messages.error(request, "Invalid username or password.")

    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login') 


@login_required
def patient_dashboard(request):
    return render(request, 'accounts/patient_dashboard.html', {'user': request.user})

@login_required
def doctor_dashboard(request):
    return render(request, 'accounts/doctor_dashboard.html', {'user': request.user})
