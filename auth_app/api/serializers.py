from django.contrib.auth.models import User
from rest_framework import serializers

from profile_app.models import Profile


class RegistrationSerializer(serializers.ModelSerializer):                                              # Serializer für die Registrierung von Benutzern. Es validiert die Eingabedaten und erstellt einen neuen Benutzer sowie ein zugehöriges Profil.
    repeated_password = serializers.CharField(write_only=True)
    type = serializers.ChoiceField(choices=Profile.ProfileType.choices)

    class Meta:                                                                                         # Meta-Klasse definiert die Modellzuordnung und die Felder, die im Serializer verwendet werden.
        model = User
        fields = ["username", "email", "password", "repeated_password", "type"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_email(self, value):                                                                    # Validiert, ob die eingegebene E-Mail-Adresse bereits von einem anderen Benutzer verwendet wird. Wenn ja, wird eine Validierungsfehlermeldung ausgelöst.
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already in use.")
        return value

    def validate(self, attrs):                                                                          # Validiert, ob das eingegebene Passwort und das wiederholte Passwort übereinstimmen. Wenn nicht, wird eine Validierungsfehlermeldung ausgelöst.
        if attrs["password"] != attrs["repeated_password"]:
            raise serializers.ValidationError(
                {"repeated_password": "Passwords do not match."}
            )
        return attrs

    def create(self, validated_data):                                                                   # Erstellt einen neuen Benutzer und ein zugehöriges Profil basierend auf den validierten Daten. Das Passwort wird verschlüsselt gespeichert, und das Profil wird mit dem angegebenen Typ erstellt.
        profile_type = validated_data.pop("type")
        validated_data.pop("repeated_password")
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user, type=profile_type)
        return user
