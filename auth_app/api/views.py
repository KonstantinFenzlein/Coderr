from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .serializers import LoginSerializer, RegistrationSerializer
from .utils import build_token_response


class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):                                                    # Registriert einen neuen Benutzer. Es validiert die Eingabedaten mithilfe des RegistrationSerializers, erstellt einen neuen Benutzer und ein zugehöriges Profil und gibt eine Antwort mit einem Authentifizierungstoken zurück.
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return build_token_response(user, status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):                                                    # Meldet einen Benutzer an. Es validiert die Eingabedaten mithilfe des LoginSerializers, authentifiziert den Benutzer und gibt eine Antwort mit einem Authentifizierungstoken zurück.
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        return build_token_response(user, status.HTTP_200_OK)
