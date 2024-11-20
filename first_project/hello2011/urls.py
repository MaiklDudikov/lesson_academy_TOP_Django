from django.urls import path
from . import views

urlpatterns = [
    path('', views.index2, name='index2'),
    path("create/", views.create, name='create'),
    path("edit/<int:id>/", views.edit, name='edit'),
    path("delete/<int:id>/", views.delete, name='delete'),
]
