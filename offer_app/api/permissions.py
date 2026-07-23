from rest_framework.permissions import BasePermission                           # Importiere Basis-Permission-Klasse
from profile_app.models import Profile                                        # Importiere Profil-Modell


class IsBusinessUser(BasePermission):                                          # Custom Permission um zu überprüfen ob Benutzer Business-Typ ist
    message = "Nur Geschäftsbenutzer können Angebote erstellen."               # Fehlermeldung wenn Permission abgelehnt

    def has_permission(self, request, view):                                   # Prüfe ob Benutzer die Permission hat
        if not request.user.is_authenticated:                                  # Prüfe ob Benutzer authentifiziert ist
            return False                                                       # Wenn nicht, verweigere Permission

        try:                                                                   # Versuche das Profil zu finden
            profile = Profile.objects.get(user=request.user)                   # Hole Profil des Benutzers
            return profile.type == 'business'                                  # Gib True zurück wenn Typ 'business' ist
        except Profile.DoesNotExist:                                           # Wenn Profil nicht existiert
            return False                                                       # Verweigere Permission


class IsOwnOffer(BasePermission):                                              # Custom Permission um zu überprüfen ob Benutzer Eigentümer des Angebots ist
    message = "Sie können nur Ihr eigenes Angebot aktualisieren."              # Fehlermeldung wenn Permission abgelehnt

    def has_object_permission(self, request, view, obj):                       # Prüfe Objekt-Level Permission
        return obj.user == request.user                                        # Gib True zurück wenn Benutzer Eigentümer ist


class IsCustomer(BasePermission):                                              # Custom Permission um zu überprüfen ob Benutzer Customer-Typ ist
    message = "Nur Kunden können Bestellungen erstellen."                      # Fehlermeldung wenn Permission abgelehnt

    def has_permission(self, request, view):                                   # Prüfe ob Benutzer die Permission hat
        if not request.user.is_authenticated:                                  # Prüfe ob Benutzer authentifiziert ist
            return False                                                       # Wenn nicht, verweigere Permission

        try:                                                                   # Versuche das Profil zu finden
            profile = Profile.objects.get(user=request.user)                   # Hole Profil des Benutzers
            return profile.type == 'customer'                                  # Gib True zurück wenn Typ 'customer' ist
        except Profile.DoesNotExist:                                           # Wenn Profil nicht existiert
            return False                                                       # Verweigere Permission


class IsOrderBusinessPartner(BasePermission):                                  # Custom Permission um zu überprüfen ob Benutzer Business-Partner der Order ist
    message = "Nur der Business-Partner dieser Bestellung kann den Status aktualisieren."  # Fehlermeldung

    def has_object_permission(self, request, view, obj):                       # Prüfe Objekt-Level Permission
        # Prüfe ob Benutzer Business-Partner ist
        try:                                                                   # Versuche das Profil zu finden
            profile = Profile.objects.get(user=request.user)                   # Hole Profil des Benutzers
            is_business = profile.type == 'business'                           # Prüfe ob Business-Typ
        except Profile.DoesNotExist:                                           # Wenn Profil nicht existiert
            return False                                                       # Verweigere Permission

        # Prüfe ob Benutzer der Business-Partner der Order ist
        return is_business and obj.business_user == request.user               # Gib True zurück wenn Business und Business-Partner


class IsAdmin(BasePermission):                                                 # Custom Permission um zu überprüfen ob Benutzer Admin ist
    message = "Nur Admin-Benutzer können Bestellungen löschen."                # Fehlermeldung wenn Permission abgelehnt

    def has_permission(self, request, view):                                   # Prüfe ob Benutzer die Permission hat
        return request.user and request.user.is_staff                          # Gib True zurück wenn Benutzer ist_staff ist


class IsOwnRating(BasePermission):                                             # Custom Permission um zu überprüfen ob Benutzer Ersteller der Bewertung ist
    message = "Sie können nur Ihre eigene Bewertung aktualisieren."             # Fehlermeldung wenn Permission abgelehnt

    def has_object_permission(self, request, view, obj):                       # Prüfe Objekt-Level Permission
        return obj.reviewer == request.user                                     # Gib True zurück wenn Benutzer der Reviewer ist
