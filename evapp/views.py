from django.shortcuts import render, redirect
from .forms import SignupForm  # Assuming you have created a SignupForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password # type: ignore

def ev_page(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Create new user object
            user = User(username=username, email=email)
            user.set_password(password)  # Set hashed password
            user.save()  # Save user to database

            # Redirect to success URL (adjust 'success_url' as per your URL config)
            return redirect('success_url')
    else:
        # If not a POST request, render blank form
        form = SignupForm()

    # Render the form with context containing the form object
    return render(request, 'ev_page.html', {'form': form})

