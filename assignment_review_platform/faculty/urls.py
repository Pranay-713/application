from django.urls import path
from . import views

app_name = 'faculty'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('review/<int:submission_id>/', views.review_submission, name='review_submission'),
]