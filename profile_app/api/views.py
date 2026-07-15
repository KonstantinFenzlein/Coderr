from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView         # Importiere allgemeine Ansichten für einzelne Objekte und Listen
from rest_framework.permissions import IsAuthenticated                          # Importiere Berechtigungs-Klasse die Anmeldung verlangt

from profile_app.models import Profile                                         # Importiere das Profil-Modell aus der Datenbank
from .serializers import ProfileSerializer, BusinessProfileListSerializer, CustomerProfileListSerializer  # Importiere die Serializer für Datenumwandlung
from .permissions import IsOwnProfile                                           # Importiere die eigene Berechtigung um nur eigenes Profil zu bearbeiten


class ProfileDetailView(RetrieveUpdateAPIView):                                # Ansicht für Profil-Abruf und -Bearbeitung. Erbt von RetrieveUpdateAPIView die ABRUFEN und ÄNDERN automatisch umsetzt
    queryset = Profile.objects.all()                                            # Definiere welche Daten die Ansicht nutzt (alle Profile aus der Datenbank)
    serializer_class = ProfileSerializer                                        # Verwende ProfilSerializer zur Umwandlung zwischen JSON und Datenbank-Objekten
    permission_classes = [IsAuthenticated, IsOwnProfile]                        # Erfordere zwei Berechtigungen: 1) Anmeldung, 2) Nur eigenes Profil bearbeiten
    http_method_names = ['get', 'patch']                                        # Erlaube nur ABRUFEN (Profil abrufen) und ÄNDERN (Profil aktualisieren), verbiete AKTUALISIEREN/LÖSCHEN/etc


class BusinessProfileListView(ListAPIView):                                     # Ansicht für Liste aller Geschäftsnutzer. Erbt von ListAPIView die automatisch eine Liste zurückgibt
    queryset = Profile.objects.filter(type='business')                          # Filtere nur die Profile mit dem Typ 'Geschäft' aus der Datenbank
    serializer_class = BusinessProfileListSerializer                            # Verwende speziellen Serializer für Geschäftsnutzer-Listen
    permission_classes = [IsAuthenticated]                                      # Erfordere nur Anmeldung (jeder angemeldete Nutzer kann die Liste sehen)
    http_method_names = ['get']                                                 # Erlaube nur ABRUFEN, verbiete POST/ÄNDERN/LÖSCHEN/etc


class CustomerProfileListView(ListAPIView):                                     # Ansicht für Liste aller Kundenprofile. Erbt von ListAPIView die automatisch eine Liste zurückgibt
    queryset = Profile.objects.filter(type='customer')                          # Filtere nur die Profile mit dem Typ 'Kunde' aus der Datenbank
    serializer_class = CustomerProfileListSerializer                            # Verwende speziellen Serializer für Kundenprofile-Listen
    permission_classes = [IsAuthenticated]                                      # Erfordere nur Anmeldung (jeder angemeldete Nutzer kann die Liste sehen)
    http_method_names = ['get']                                                 # Erlaube nur ABRUFEN, verbiete POST/ÄNDERN/LÖSCHEN/etc
