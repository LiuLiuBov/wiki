from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("wiki/<str:title>", views.getentry, name="getentry"),
    path("create/", views.create, name="create"),
    path("edit/<str:title>", views.edit, name="edit")
]
