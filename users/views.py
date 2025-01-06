from django.http import HttpResponse
from django.shortcuts import redirect, render

from users.forms import CreateUser, EditUser
from users.models import User


# Create your views here.
def home(request):
    users = User.objects.all()
    return render(request, "index.html", {"users": users})


def catalog(request):
    users = User.objects.all()
    return render(request, "catalog.html", {"users": users})


def create(request):
    form = CreateUser()

    # Check if the request method is POST (create new user)
    if request.method == "POST":
        form = CreateUser(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("/users/home")

    return render(request, "create.html", {"form": form, "return_url": "/users/home"})


def edit(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return redirect("/users/home")

    form = EditUser(instance=user)

    if request.method == "POST":
        form = EditUser(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect("/users/home")

    return render(request, "edit.html", {"form": form, "return_url": "/users/home"})


def details(request, id):
    user = User.objects.get(id=id)

    print(user.avatar)
    print(user.avatar.url)

    return render(request, "details.html", {"user": user, "return_url": "/users/home"})


def delete(request, id):
    user = User.objects.get(id=id)

    if user is not None:
        user.delete()

    return redirect("/users/home")


def about(request):
    return HttpResponse("<h1>About Page!</h1>")
