from django.urls import path
from . import views


urlpatterns = [
    path('', views.training_program, name='training_program'),
    path('program/<int:id>/', views.training_program_details, name='training_program_details'),
]