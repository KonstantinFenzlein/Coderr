from rest_framework.permissions import BasePermission                           # Importiere die Basis-Klasse für eigene Berechtigungen


class IsOwnProfile(BasePermission):                                            # Eigene Berechtigung, die überprüft ob ein Benutzer nur sein eigenes Profil bearbeiten darf
    message = "Sie dürfen nur Ihr eigenes Profil bearbeiten."                  # Fehlermeldung, die angezeigt wird wenn die Berechtigung verweigert wird

    def has_object_permission(self, request, view, obj):                      # Methode wird aufgerufen um zu prüfen ob der Benutzer Zugriff auf dieses spezifische Objekt hat
        return obj.user == request.user                                        # Gib Wahr zurück wenn der Profil-Besitzer der aktuelle Benutzer ist, sonst Falsch (403 Fehler)
