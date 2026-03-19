from django.urls import path
from . import views

urlpatterns = [
    # Agrega tus URLs aqu
    path('', views.index, name='luis-index'),
]
