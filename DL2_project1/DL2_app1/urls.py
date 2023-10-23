from django.urls import path, include
from DL2_app1 import views

urlpatterns = [
    path("", views.users, name="users"),
]