from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def MasterErrors(request, errors):
    for error in errors:
        messages.error(request, error)

def index(request):
    return render(request, 'login/index.html')

def success(request):
    if 'user_id' in request.session:

        return render(request, 'login/success.html')

    return redirect(reverse('landing'))

def register(request):
    if request.method == 'POST':
        errors = User.objects.validateRegistration(request.POST)

        if not errors:
            user = User.objects.createUser(request.POST)

            request.session['user_id'] = user.id

            return redirect(reverse('success'))

        MasterErrors(request, errors)

    return redirect(reverse('landing'))

def login(request):
    if request.method == "POST":

        errors = User.objects.validateLogin(request.POST)

        if not errors:
            user = User.objects.filter(email = request.POST['email']).first()

            if user:
                password = str(request.POST['password'])
                user_password = str(user.password)

                hashed_pw = bcrypt.hashpw(password, user_password)

                if hashed_pw == user.password:
                    request.session['user_id'] = user.id

                    return redirect(reverse('success'))

            errors.append("Invalid account information.")

        MasterErrors(request, errors)

    return redirect(reverse('landing'))

def logout(request):
    if 'user_id' in request.session:
        request.session.pop('user_id')

    return redirect(reverse('landing'))
