from django.urls import path
from DL2_app1 import views

urlpatterns = [
    path("", views.users, name="users"),
]