from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "index.html", {"users": users})


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
