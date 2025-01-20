from django.urls import path

from cart import views

urlpatterns = [
    path("", views.index),
    path("add/<str:id>", views.add),
    path("clear/", views.clear),
]
