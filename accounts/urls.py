from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.CustomRegistrationView.as_view(), name='register-user')
]
