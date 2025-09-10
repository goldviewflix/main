from django.urls import path
from . import views

urlpatterns = [
    path('', views.kyc_submission, name='kyc_submission'),
]
