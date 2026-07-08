from rest_framework import status                                                # HTTP Status-Codes (z.B. 201, 200)
from rest_framework.permissions import AllowAny                                  # Erlaubt jedem Zugriff (auch ohne Authentifizierung) = AllowAny
from rest_framework.views import APIView                                         # Basis-Klasse für API-Endpoints

from .serializers import LoginSerializer, RegistrationSerializer                 # Serializer für Validierung und Datenumwandlung
from .utils import build_token_response                                          # Hilfsfunktion zum Erstellen der Token-Response


class RegistrationView(APIView):                                                 # View für Benutzer-Registrierung
    permission_classes = [AllowAny]                                              # Jeder darf registrieren (ohne Login erforderlich)

    def post(self, request):                                                     # POST-Endpoint für neue Benutzer
        serializer = RegistrationSerializer(data=request.data)                   # Validiere die Eingabedaten (username, email, password)
        serializer.is_valid(raise_exception=True)                                # Prüfe die Daten, wirf Fehler aus wenn ungültig
        user = serializer.save()                                                 # Speichere den neuen Benutzer und Profil in der Datenbank
        return build_token_response(user, status.HTTP_201_CREATED)               # Gib Token zurück mit Status 201 (Created)


class LoginView(APIView):                                                        # View für Benutzer-Anmeldung
    permission_classes = [AllowAny]                                              # Jeder darf sich anmelden (ohne vorherigen Login)

    def post(self, request):                                                     # POST-Endpoint für Anmeldung
        serializer = LoginSerializer(data=request.data)                          # Validiere die Anmeldedaten (username, password)
        serializer.is_valid(raise_exception=True)                                # Prüfe die Daten, wirf Fehler wenn ungültig
        user = serializer.validated_data["user"]                                 # Hole den authentifizierten Benutzer
        return build_token_response(user, status.HTTP_200_OK)                    # Gib Token zurück mit Status 200 (OK)
