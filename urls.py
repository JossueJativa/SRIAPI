from django.urls import path
from . import views

app_name = "RUC"

urlpatterns = [
    path('', views.intro, name='intro'),
]