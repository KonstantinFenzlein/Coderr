from django.contrib.auth.models import User                                   # Importiere das Django Benutzer-Modell für Benutzerdaten (Benutzername, E-Mail, Vorname, Nachname)
from rest_framework import serializers                                          # Importiere REST Framework Serializer für Datenprüfung und Umwandlung

from profile_app.models import Profile                                         # Importiere das Profil-Modell für erweiterte Profilinformationen


class ProfileSerializer(serializers.Serializer):                                # Eigener Serializer (kein Modell-Serializer) um vollständige Kontrolle über die Felder zu haben
    # Nur lesbare Felder (vom Profil-Modell)
    user = serializers.IntegerField(read_only=True)                             # Benutzer-ID, nur lesbar
    username = serializers.CharField(read_only=True)                            # Benutzername, nur lesbar
    type = serializers.CharField(read_only=True)                                # Profiltyp (Kunde/Geschäft), nur lesbar
    created_at = serializers.DateTimeField(read_only=True)                      # Erstellungsdatum, nur lesbar

    # Benutzer-Felder (änderbar)
    email = serializers.EmailField()                                            # E-Mail vom Benutzer-Modell, änderbar
    first_name = serializers.CharField(required=False, allow_blank=True)       # Vorname vom Benutzer-Modell, optional, änderbar
    last_name = serializers.CharField(required=False, allow_blank=True)        # Nachname vom Benutzer-Modell, optional, änderbar

    # Profil-Felder (änderbar)
    file = serializers.CharField(required=False, allow_blank=True)              # Profilbildpfad, optional
    location = serializers.CharField(required=False, allow_blank=True)          # Ort, optional
    tel = serializers.CharField(required=False, allow_blank=True)               # Telefon, optional
    description = serializers.CharField(required=False, allow_blank=True)       # Beschreibung, optional
    working_hours = serializers.CharField(required=False, allow_blank=True)    # Arbeitszeiten, optional

    def to_representation(self, instance):                                      # Methode wird aufgerufen wenn Daten aus der DB in JSON umgewandelt werden (Antwort)
        return {                                                                 # Erstelle ein Wörterbuch mit allen Feldern
            'user': instance.user.id,                                           # Benutzer-ID vom verbundenen Benutzer
            'username': instance.user.username,                                 # Benutzername vom verbundenen Benutzer
            'email': instance.user.email,                                       # E-Mail vom verbundenen Benutzer
            'first_name': instance.user.first_name or '',                       # Vorname vom Benutzer, Null → ''
            'last_name': instance.user.last_name or '',                         # Nachname vom Benutzer, Null → ''
            'file': instance.file or '',                                        # Datei vom Profil, Null → ''
            'location': instance.location or '',                                # Ort vom Profil, Null → ''
            'tel': instance.tel or '',                                          # Telefon vom Profil, Null → ''
            'description': instance.description or '',                          # Beschreibung vom Profil, Null → ''
            'working_hours': instance.working_hours or '',                      # Arbeitszeiten vom Profil, Null → ''
            'type': instance.type,                                              # Typ vom Profil
            'created_at': instance.created_at,                                  # Erstellungsdatum vom Profil
        }

    def update(self, instance, validated_data):                                 # Methode wird aufgerufen wenn Daten von JSON in DB gespeichert werden (PATCH/AKTUALISIEREN)
        user = instance.user                                                    # Hole den verbundenen Benutzer

        # Aktualisiere Benutzer-Felder
        if 'email' in validated_data:                                           # Wenn E-Mail aktualisiert werden soll
            user.email = validated_data.pop('email')                             # Speichere es im Benutzer-Modell
        if 'first_name' in validated_data:                                      # Wenn Vorname aktualisiert werden soll
            user.first_name = validated_data.pop('first_name')                   # Speichere es im Benutzer-Modell
        if 'last_name' in validated_data:                                       # Wenn Nachname aktualisiert werden soll
            user.last_name = validated_data.pop('last_name')                     # Speichere es im Benutzer-Modell
        user.save()                                                             # Speichere alle Änderungen am Benutzer

        # Aktualisiere Profil-Felder (alle verbleibenden Felder)
        for field, value in validated_data.items():                             # Gehe durch alle verbleibenden Felder
            setattr(instance, field, value)                                     # Speichere den Wert im Profil-Objekt
        instance.save()                                                         # Speichere alle Änderungen am Profil

        return instance                                                         # Gib das aktualisierte Profil-Objekt zurück
