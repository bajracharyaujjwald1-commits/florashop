from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from .forms import SignUpForm
from .models import Customer

def main_page_view(request):
    return render(request, "customer/main.html")

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Save the new user object
            user = form.save()
            email = form.save()

            # Automatically create the associated Customer profile
            Customer.objects.create(username=user)
            Customer.objects.create(email=email)

            # Log the user in immediately after registering
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect("home")  # Replace 'home' with your landing page URL name
    else:
        form = SignUpForm()

    return render(request, "customer/login2.html", {"form": form})

def login_view(request):
    # If user is already logged in, redirect straight to home
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username_input = request.POST.get("username")
        password_input = request.POST.get("password")
        remember_me = request.POST.get("remember_me")

        user = authenticate(
            request, username=username_input, password=password_input
        )

        if user is not None:
            login(request, user)

            # Keep session active if 'Remember me' was checked
            if not remember_me:
                request.session.set_expiry(0)  # Expires on browser close
            else:
                request.session.set_expiry(1209600)  # 2 weeks

            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "customer/login.html")