from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("about/", views.about),
    path("contact/", views.contact),
    path("details/", views.details),
    path("index/<int:id>", views.index),
    path("access/<int:age>", views.access),
]
