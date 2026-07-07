from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from profile_app.models import Profile
from .serializers import ProfileSerializer


class ProfileDetailView(RetrieveUpdateAPIView): # Empfängt Requests, prüft, ob der Benutzer authentifiziert ist, holt die Daten aus der Datenbank und sender die Antwort zurück
    queryset = Profile.objects.all()            # Schau in der Profile-Tabelle nach
    serializer_class = ProfileSerializer        # Benutze diesen Serializer zur Umwandlung   
    permission_classes = [IsAuthenticated]      # Der Benutzer muss angemeldet sein
    http_method_names = ['get', 'patch']        # Nur diese Methoden erlauben, PUT/DELETE/etc. verbieten
