from django.http import HttpResponse
from django.shortcuts import render


users = [
    {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
    },
    {
        "id": 2,
        "name": "Ervin Howell",
        "username": "Antonette",
        "email": "Shanna@melissa.tv",
    },
    {
        "id": 3,
        "name": "Clementine Bauch",
        "username": "Samantha",
        "email": "Nathan@yesenia.net",
    },
]


# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello from Django!</h1>")


def list(request):

    html = "<h1>Users</h1>"
    html += "<ul>"
    for user in users:
        html += f"<li>{user['name']}</li>"
    html += "</ul>"

    return HttpResponse(html)


def details(request, id):
    return HttpResponse(f"User Details: ID - {id}")


def about(request):
    return HttpResponse("<h1>About Page!</h1>")
