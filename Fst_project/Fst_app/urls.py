from django.urls import path
from Fst_app import views

urlpatterns = [
    path("", views.index, name="index")
]

