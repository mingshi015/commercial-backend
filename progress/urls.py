from django.urls import path
from . import views

urlpatterns = [
    path('me/', views.RetrieveCreateUpdateMe.as_view())
]