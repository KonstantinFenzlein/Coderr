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


class BusinessProfileListSerializer(serializers.Serializer):                    # Serializer speziell für die Liste von Geschäftsprofilen, optimiert für Listenansicht
    # Alle Felder für die Listenansicht
    user = serializers.IntegerField(read_only=True)                             # Benutzer-ID, nur lesbar
    username = serializers.CharField(read_only=True)                            # Benutzername, nur lesbar
    first_name = serializers.CharField(read_only=True)                          # Vorname, nur lesbar
    last_name = serializers.CharField(read_only=True)                           # Nachname, nur lesbar
    file = serializers.CharField(read_only=True)                                # Profilbild, nur lesbar
    location = serializers.CharField(read_only=True)                            # Ort, nur lesbar
    tel = serializers.CharField(read_only=True)                                 # Telefon, nur lesbar
    description = serializers.CharField(read_only=True)                         # Beschreibung, nur lesbar
    working_hours = serializers.CharField(read_only=True)                       # Arbeitszeiten, nur lesbar
    type = serializers.CharField(read_only=True)                                # Profiltyp, nur lesbar

    def to_representation(self, instance):                                      # Methode wird aufgerufen wenn Profildaten in JSON für die Liste umgewandelt werden
        return {                                                                 # Erstelle ein Wörterbuch mit allen Geschäftsnutzer-Feldern
            'user': instance.user.id,                                           # Benutzer-ID vom verbundenen Benutzer
            'username': instance.user.username,                                 # Benutzername vom verbundenen Benutzer
            'first_name': instance.user.first_name or '',                       # Vorname vom Benutzer, Null → ''
            'last_name': instance.user.last_name or '',                         # Nachname vom Benutzer, Null → ''
            'file': instance.file or '',                                        # Datei vom Profil, Null → ''
            'location': instance.location or '',                                # Ort vom Profil, Null → ''
            'tel': instance.tel or '',                                          # Telefon vom Profil, Null → ''
            'description': instance.description or '',                          # Beschreibung vom Profil, Null → ''
            'working_hours': instance.working_hours or '',                      # Arbeitszeiten vom Profil, Null → ''
            'type': instance.type,                                              # Profiltyp vom Profil
        }


class CustomerProfileListSerializer(serializers.Serializer):                    # Serializer speziell für die Liste von Kundenprofilen, optimiert für Listenansicht
    # Alle Felder für die Listenansicht
    user = serializers.IntegerField(read_only=True)                             # Benutzer-ID, nur lesbar
    username = serializers.CharField(read_only=True)                            # Benutzername, nur lesbar
    first_name = serializers.CharField(read_only=True)                          # Vorname, nur lesbar
    last_name = serializers.CharField(read_only=True)                           # Nachname, nur lesbar
    file = serializers.CharField(read_only=True)                                # Profilbild, nur lesbar
    location = serializers.CharField(read_only=True)                            # Ort, nur lesbar
    tel = serializers.CharField(read_only=True)                                 # Telefon, nur lesbar
    description = serializers.CharField(read_only=True)                         # Beschreibung, nur lesbar
    working_hours = serializers.CharField(read_only=True)                       # Arbeitszeiten, nur lesbar
    type = serializers.CharField(read_only=True)                                # Profiltyp, nur lesbar

    def to_representation(self, instance):                                      # Methode wird aufgerufen wenn Profildaten in JSON für die Liste umgewandelt werden
        return {                                                                 # Erstelle ein Wörterbuch mit allen Kundenprofil-Feldern
            'user': instance.user.id,                                           # Benutzer-ID vom verbundenen Benutzer
            'username': instance.user.username,                                 # Benutzername vom verbundenen Benutzer
            'first_name': instance.user.first_name or '',                       # Vorname vom Benutzer, Null → ''
            'last_name': instance.user.last_name or '',                         # Nachname vom Benutzer, Null → ''
            'file': instance.file or '',                                        # Datei vom Profil, Null → ''
            'location': instance.location or '',                                # Ort vom Profil, Null → ''
            'tel': instance.tel or '',                                          # Telefon vom Profil, Null → ''
            'description': instance.description or '',                          # Beschreibung vom Profil, Null → ''
            'working_hours': instance.working_hours or '',                      # Arbeitszeiten vom Profil, Null → ''
            'type': instance.type,                                              # Profiltyp vom Profil
        }
