from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):                                                # Erstellt ein Profil für jeden User, der sich registriert. Das Profil enthält Informationen über den Typ des Users (Kunde oder Unternehmen).
    class ProfileType(models.TextChoices):
        CUSTOMER = "customer", "Customer"
        BUSINESS = "business", "Business"

    user = models.OneToOneField(                                            # Jeder User bekommt genau ein Profil (keine Mehrfach-Profile)
        User, on_delete=models.CASCADE, related_name="profile"              # Wird ein User gelöscht, verschwindet automatisch auch sein Profil
    )
    type = models.CharField(max_length=10, choices=ProfileType.choices)     # Der Typ des Profils wird als CharField gespeichert, wobei die Auswahlmöglichkeiten aus der ProfileType-Klasse stammen.
    file = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    working_hours = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:                                                             # Meta-Informationen für das Model
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):                                                      # Gibt den Namen des Users und den Typ des Profils zurück, wenn das Profil-Objekt als String dargestellt wird
        return f"{self.user.username} ({self.type})"
