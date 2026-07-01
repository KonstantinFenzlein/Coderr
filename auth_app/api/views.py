from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegistrationSerializer


class RegistrationView(APIView):                                                                # API-View für die Registrierung von Benutzern. Es verarbeitet POST-Anfragen, validiert die Eingabedaten mithilfe des RegistrationSerializers und erstellt einen neuen Benutzer sowie ein zugehöriges Profil. Anschließend wird ein Authentifizierungstoken generiert und zurückgegeben.
    permission_classes = [AllowAny]                                                             # Erlaubt allen Benutzern, auf diese View zuzugreifen, unabhängig davon, ob sie authentifiziert sind oder nicht.

    def post(self, request):                                                                    # Verarbeitet POST-Anfragen zur Benutzerregistrierung. Es validiert die Eingabedaten, erstellt einen neuen Benutzer und ein zugehöriges Profil, generiert ein Authentifizierungstoken und gibt die relevanten Informationen in der Antwort zurück.
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response(                                                                        # Gibt eine erfolgreiche Antwort mit dem Authentifizierungstoken, dem Benutzernamen, der E-Mail-Adresse und der Benutzer-ID zurück, wenn die Registrierung erfolgreich war.
            {
                "token": token.key,
                "username": user.username,
                "email": user.email,
                "user_id": user.id,
            },
            status=status.HTTP_201_CREATED,
        )
