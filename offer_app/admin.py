from django.contrib import admin                                              # Importiere Django Admin
from offer_app.models import Offer, OfferDetail                               # Importiere Angebots-Modelle


class OfferDetailInline(admin.TabularInline):                                  # Inline-Admin für Angebotsdetails
    model = OfferDetail                                                        # Verwende OfferDetail-Modell
    extra = 1                                                                 # Ermögliche das Hinzufügen von 1 neuer Detail


@admin.register(Offer)                                                        # Registriere Offer im Admin
class OfferAdmin(admin.ModelAdmin):                                            # Admin-Klasse für Angebote
    inlines = [OfferDetailInline]                                             # Zeige Angebotsdetails inline
    list_display = ['title', 'user', 'created_at', 'updated_at']             # Spalten in der Liste
    list_filter = ['user', 'created_at']                                      # Filter-Optionen
    search_fields = ['title', 'description']                                  # Suchbare Felder


@admin.register(OfferDetail)                                                  # Registriere OfferDetail im Admin
class OfferDetailAdmin(admin.ModelAdmin):                                      # Admin-Klasse für Angebotsdetails
    list_display = ['title', 'offer', 'price', 'delivery_time']              # Spalten in der Liste
    list_filter = ['offer__user', 'price', 'delivery_time']                  # Filter-Optionen
    search_fields = ['title', 'offer__title']                                 # Suchbare Felder
