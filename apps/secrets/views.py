from django.shortcuts import render, redirect, reverse
from django.db.models import Count
from .models import Secret
from ..login.models import User


# Create your views here.
def index(request):
    current_user = User.objects.currentUser(request)
    secrets = Secret.objects.annotate(num_likes=Count('liked_by'))


    context = {
        'user': current_user,
        'secrets' : secrets
    }

    return render(request, 'secrets/index.html', context)

def popular(request):
    current_user = User.objects.currentUser(request)
    secrets = Secret.objects.annotate(num_likes=Count('liked_by')).order_by('-num_likes')

    context = {
        'user': current_user,
        'secrets': secrets
    }

    return render(request, 'secrets/popular.html', context)

def add(request):
    print "Inside the method"
    if request.method == "POST":

        if len(request.POST['content']) != 0:

            current_user = User.objects.currentUser(request)
            secret = Secret.objects.AddSecret(request.POST, current_user)

    return redirect(reverse('success'))

def like(request, id):
    current_user = User.objects.currentUser(request)
    secret = Secret.objects.get(id=id)

    current_user.likes.add(secret)

    return redirect(reverse('success'))

def unlike(request, id):
    current_user = User.objects.currentUser(request)
    secret = Secret.objects.get(id=id)

    current_user.likes.remove(secret)

    return redirect(reverse('success'))

def delete(request, id):
    if request.method == "POST":
        secret = Secret.objects.get(id=id)
        current_user =  User.objects.currentUser(request)

        if current_user.id == secret.user.id:
            secret.delete()

        return redirect(reverse('success'))
