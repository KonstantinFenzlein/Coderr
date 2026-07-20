from django.db import models                                               # Importiere Basis-Klasse für Datenbankmodelle
from django.contrib.auth.models import User                                   # Importiere Benutzer-Modell für Beziehungen
from django.utils import timezone                                              # Importiere timezone für Zeitstempel


class Offer(models.Model):                                                    # Modell für Angebote (z.B. Dienstleistungen, die ein Benutzer anbietet)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offers')  # Verbindung zum Benutzer, der das Angebot erstellt hat
    title = models.CharField(max_length=200)                                  # Titel des Angebots (z.B. "Website Design")
    image = models.CharField(max_length=255, blank=True, null=True)          # Bild-URL des Angebots (optional)
    description = models.TextField()                                          # Ausführliche Beschreibung des Angebots
    created_at = models.DateTimeField(auto_now_add=True)                     # Zeitstempel wann das Angebot erstellt wurde
    updated_at = models.DateTimeField(auto_now=True)                         # Zeitstempel wann das Angebot zuletzt aktualisiert wurde

    class Meta:                                                               # Meta-Informationen für das Modell
        verbose_name = "Angebot"                                              # Singular-Name für Django Admin
        verbose_name_plural = "Angebote"                                      # Plural-Name für Django Admin
        ordering = ['-updated_at']                                            # Sortierung: neueste Angebote zuerst

    def __str__(self):                                                        # String-Darstellung des Angebots
        return f"{self.title} von {self.user.username}"                       # Zeige Titel und Benutzer an


class OfferDetail(models.Model):                                              # Modell für Angebotsdetails (z.B. verschiedene Preise/Lieferzeiten)
    class OfferType(models.TextChoices):                                      # Aufzählung für Angebots-Typen
        BASIC = 'basic', 'Basic'                                              # Basis-Paket
        STANDARD = 'standard', 'Standard'                                      # Standard-Paket
        PREMIUM = 'premium', 'Premium'                                         # Premium-Paket

    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='details')  # Verbindung zum Angebot
    title = models.CharField(max_length=200)                                  # Titel der Angebotsdetail (z.B. "Basis-Paket")
    price = models.DecimalField(max_digits=10, decimal_places=2)             # Preis für diese Angebotsdetail
    delivery_time = models.IntegerField()                                     # Lieferzeit in Tagen (alt: delivery_time_in_days)
    revisions = models.IntegerField(default=1)                                # Anzahl der Überarbeitungen
    features = models.JSONField(default=list)                                 # Liste von Features als JSON (z.B. ["Logo Design", "Visitenkarte"])
    offer_type = models.CharField(max_length=20, choices=OfferType.choices, default=OfferType.BASIC)  # Typ des Angebots
    created_at = models.DateTimeField(auto_now_add=True)                     # Zeitstempel wann die Angebotsdetail erstellt wurde

    class Meta:                                                               # Meta-Informationen für das Modell
        verbose_name = "Angebotsdetail"                                       # Singular-Name für Django Admin
        verbose_name_plural = "Angebotsdetails"                               # Plural-Name für Django Admin
        ordering = ['price']                                                  # Sortierung: günstigste zuerst

    def __str__(self):                                                        # String-Darstellung der Angebotsdetail
        return f"{self.title} - {self.price}€"                                # Zeige Titel und Preis an


class Order(models.Model):                                                    # Modell für Bestellungen
    class OrderStatus(models.TextChoices):                                    # Aufzählung für Order-Status
        PENDING = 'pending', 'Ausstehend'                                     # Order wurde gerade erstellt
        IN_PROGRESS = 'in_progress', 'Läuft'                                  # Order wird bearbeitet
        COMPLETED = 'completed', 'Abgeschlossen'                              # Order wurde fertiggestellt
        CANCELLED = 'cancelled', 'Abgebrochen'                                # Order wurde storniert

    customer_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders_as_customer')  # Kunde der Bestellung
    business_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders_as_business')  # Business-Partner
    offer_detail = models.ForeignKey(OfferDetail, on_delete=models.SET_NULL, null=True, related_name='orders')  # Referenz zur OfferDetail

    # Kopie der Angebotsdetail-Daten (für historische Zwecke)
    title = models.CharField(max_length=200)                                   # Titel der Bestellung
    price = models.DecimalField(max_digits=10, decimal_places=2)              # Preis der Bestellung
    delivery_time = models.IntegerField()                                      # Lieferzeit in Tagen
    revisions = models.IntegerField(default=1)                                 # Anzahl der Überarbeitungen
    features = models.JSONField(default=list)                                  # Features der Bestellung
    offer_type = models.CharField(max_length=20, choices=OfferDetail.OfferType.choices, default=OfferDetail.OfferType.BASIC)  # Typ

    # Status und Zeitstempel
    status = models.CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.PENDING)  # Status der Bestellung
    created_at = models.DateTimeField(auto_now_add=True)                      # Wann wurde die Bestellung erstellt
    updated_at = models.DateTimeField(auto_now=True)                          # Wann wurde die Bestellung zuletzt aktualisiert

    class Meta:                                                               # Meta-Informationen für das Modell
        verbose_name = "Bestellung"                                            # Singular-Name für Django Admin
        verbose_name_plural = "Bestellungen"                                   # Plural-Name für Django Admin
        ordering = ['-created_at']                                             # Sortierung: neueste zuerst

    def __str__(self):                                                        # String-Darstellung der Bestellung
        return f"Order #{self.id} - {self.title} ({self.status})"            # Zeige Order-ID, Titel und Status


class Rating(models.Model):                                                   # Modell für Bewertungen
    business_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings_received')  # Business-User der bewertet wird
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings_given')  # Benutzer der bewertet
    rating = models.IntegerField()                                             # Bewertung von 1-5
    description = models.TextField()                                           # Beschreibung der Bewertung
    created_at = models.DateTimeField(auto_now_add=True)                      # Zeitstempel wann Bewertung erstellt wurde
    updated_at = models.DateTimeField(auto_now=True)                          # Zeitstempel wann Bewertung zuletzt aktualisiert wurde

    class Meta:                                                               # Meta-Informationen für das Modell
        verbose_name = "Bewertung"                                             # Singular-Name für Django Admin
        verbose_name_plural = "Bewertungen"                                    # Plural-Name für Django Admin
        ordering = ['-updated_at']                                             # Sortierung: neueste zuerst

    def __str__(self):                                                        # String-Darstellung der Bewertung
        return f"Rating #{self.id} - {self.rating}★ von {self.reviewer.username} für {self.business_user.username}"  # Zeige Details
