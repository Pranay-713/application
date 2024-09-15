from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('submit/<int:assignment_id>/', views.submit_assignment, name='submit_assignment'),
]