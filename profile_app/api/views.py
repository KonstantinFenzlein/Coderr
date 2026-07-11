from rest_framework.generics import RetrieveUpdateAPIView                      # Importiere allgemeine Ansicht die ABRUFEN und ÄNDERN/AKTUALISIEREN unterstützt
from rest_framework.permissions import IsAuthenticated                          # Importiere Berechtigungs-Klasse die Anmeldung verlangt

from profile_app.models import Profile                                         # Importiere das Profil-Modell aus der Datenbank
from .serializers import ProfileSerializer                                      # Importiere den Serializer für Datenumwandlung
from .permissions import IsOwnProfile                                           # Importiere die eigene Berechtigung um nur eigenes Profil zu bearbeiten


class ProfileDetailView(RetrieveUpdateAPIView):                                # Ansicht für Profil-Abruf und -Bearbeitung. Erbt von RetrieveUpdateAPIView die ABRUFEN und ÄNDERN automatisch umsetzt
    queryset = Profile.objects.all()                                            # Definiere welche Daten die Ansicht nutzt (alle Profile aus der Datenbank)
    serializer_class = ProfileSerializer                                        # Verwende ProfilSerializer zur Umwandlung zwischen JSON und Datenbank-Objekten
    permission_classes = [IsAuthenticated, IsOwnProfile]                        # Erfordere zwei Berechtigungen: 1) Anmeldung, 2) Nur eigenes Profil bearbeiten
    http_method_names = ['get', 'patch']                                        # Erlaube nur ABRUFEN (Profil abrufen) und ÄNDERN (Profil aktualisieren), verbiete AKTUALISIEREN/LÖSCHEN/etc
