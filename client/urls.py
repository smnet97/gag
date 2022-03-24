from django.urls import path
from .views import ClientRegistration, ClientLogin, client_logout

app_name = 'client'

urlpatterns = [
    path('logout/', client_logout, name='logout'),
    path('login/', ClientLogin.as_view(), name='login'),
    path('registration/', ClientRegistration.as_view(), name='registration')
]
