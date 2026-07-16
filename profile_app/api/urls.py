from django.urls import path                                                   # Importiere die Pfad-Funktion um URL-Muster zu definieren

from .views import ProfileDetailView, BusinessProfileListView, CustomerProfileListView  # Importiere alle Ansichten für Profile und Listen

urlpatterns = [                                                                 # Liste aller URL-Muster für diese Anwendung
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),     # Neue API-Struktur: /api/profiles/1/ für einzelne Profile
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail-alt'),  # Frühere Version für Frontend-Kompatibilität: /api/profile/1/
    path('profiles/business/', BusinessProfileListView.as_view(), name='business-profiles'), # Liste aller Geschäftsnutzer: /api/profiles/business/
    path('profiles/customer/', CustomerProfileListView.as_view(), name='customer-profiles'), # Liste aller Kundenprofile: /api/profiles/customer/
]
