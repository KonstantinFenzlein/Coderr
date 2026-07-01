from django.urls import path

from .views import RegistrationView

urlpatterns = [                                                                 # Definiert die URL-Muster für die Authentifizierungs-API. Es enthält eine Route für die Benutzerregistrierung, die auf die RegistrationView verweist.
    path("registration/", RegistrationView.as_view()),
]
