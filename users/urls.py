from django.urls import path

from users import views

urlpatterns = [
    path("home/", views.home),
    path("details/<int:id>", views.details),
    path("delete/<int:id>", views.delete),
]
