from django.urls import include, path

from users import views

urlpatterns = [
    path("", views.catalog),
    path("home/", views.home),
    path("create/", views.create),
    path("edit/<int:id>", views.edit),
    path("details/<int:id>", views.details),
    path("delete/<int:id>", views.delete),
]
