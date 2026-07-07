from django.contrib.auth.models import User
from rest_framework import serializers

from profile_app.models import Profile


class ProfileSerializer(serializers.ModelSerializer):                                           # Serializer für das Profilmodell. Es definiert, wie die Profildaten serialisiert und deserialisiert werden, einschließlich der Felder, die im API-Endpunkt zurückgegeben werden sollen.
    user = serializers.IntegerField(source='user.id', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)

    class Meta:
        model = Profile
        fields = [
            'user', 'username', 'first_name', 'last_name',
            'email', 'file', 'location', 'tel', 'description',
            'working_hours', 'type', 'created_at'
        ]
        read_only_fields = ['user', 'username', 'email', 'created_at', 'type', 'first_name', 'last_name']       # Der User kann sein Profil bearbeiten, aber nicht seine Benutzer-ID ändern

    def to_representation(self, instance):                                                  # Die Felder ... dürfen im Response nicht null sein, sondern müssen mit einem leeren String ('') belegt werden
        data = super().to_representation(instance)                                          # Erstelle die normale JSON-Response und gib mir den Wert vom Feld, oder None wenn nicht vorhanden
        data['first_name'] = data.get('first_name') or ''                                   # or = Falls None, benutze einen leeren String stattdessen
        data['last_name'] = data.get('last_name') or ''
        data['location'] = data.get('location') or ''
        data['tel'] = data.get('tel') or ''
        data['description'] = data.get('description') or ''
        data['working_hours'] = data.get('working_hours') or ''
        data['file'] = data.get('file') or ''
        return data
