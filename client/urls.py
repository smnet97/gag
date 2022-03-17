from django.urls import path
from .views import ClientRegistration

app_name = 'client'

urlpatterns = [
    path('registration/', ClientRegistration.as_view(), name='registration')
]
