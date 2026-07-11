from django.contrib.auth.models import User                                         # Importiere das Standard-User-Model von Django, das Login-Daten speichert
from django.db import models                                                        # Importiere die Basis-Klasse für Datenbankmodelle


class Profile(models.Model):                                                        # Erstellt ein Profil für jeden User. Das Profil speichert erweiterte Informationen wie Ort, Telefon, Arbeitszeiten und den Nutzertyp (Kunde oder Business)
    class ProfileType(models.TextChoices):                                          # Definiere die möglichen Profiltypen als Auswahlmöglichkeiten (wie ein Dropdown-Menu in der Datenbank)
        CUSTOMER = "customer", "Customer"                                           # Erste Wert = was in DB gespeichert wird, zweiter = was angezeigt wird
        BUSINESS = "business", "Business"                                           # Zweite Option: Business-Nutzer (z.B. für Unternehmen oder Dienstleister)

    user = models.OneToOneField(                                                    # Verbindung zum User-Model: JEDER User hat GENAU EIN Profil (nicht mehrere)
        User, on_delete=models.CASCADE, related_name="profile"                      # on_delete=CASCADE: wenn User gelöscht → Profil auch gelöscht. related_name="profile" ermöglicht user.profile Zugriff
    )
    type = models.CharField(max_length=10, choices=ProfileType.choices)             # Speichere den Profiltyp (customer oder business). choices begrenzt die Werte auf unsere Optionen, max_length=10 für Speicheroptimierung
    file = models.CharField(max_length=255, blank=True, null=True)                  # Profilbild-Pfad: blank=True (optional im Form), null=True (kann NULL in DB sein). CharField für Datei-Pfade statt ImageField
    location = models.CharField(max_length=255, blank=True, null=True)              # Ort/Stadt des Users. Optional, da nicht alle Nutzer diese Info angeben möchten
    tel = models.CharField(max_length=20, blank=True, null=True)                    # Telefonnummer des Users. Kurz gehalten (max 20 Zeichen), optional für Privatsphäre
    description = models.TextField(blank=True, null=True)                           # Längerer Text für Beschreibung/Bio. TextField statt CharField da theoretisch unbegrenzt lang
    working_hours = models.CharField(max_length=100, blank=True, null=True)         # Arbeitszeiten als Text (z.B. "9-17 Uhr"). Optional, nur für Business-Profile relevant
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)     # Zeitstempel wann das Profil erstellt wurde. auto_now_add setzt es automatisch beim Erstellen

    class Meta:                                                                     # Meta-Klasse enthält Einstellungen für das Model selbst (nicht für Felder)
        verbose_name = "Profile"                                                    # Singular-Name für Django Admin ("1 Profile")
        verbose_name_plural = "Profiles"                                            # Plural-Name für Django Admin ("5 Profiles")

    def __str__(self):                                                              # Diese Methode wird aufgerufen wenn das Objekt als String angezeigt wird (z.B. in Django Admin oder bei print())
        return f"{self.user.username} ({self.type})"                                # Zeige Username und Profiltyp an, z.B. "max_mustermann (business)"
