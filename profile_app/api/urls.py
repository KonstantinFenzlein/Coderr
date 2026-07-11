from django.urls import path

from .views import ProfileDetailView

urlpatterns = [
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),     # Neue API-Struktur: /api/profiles/1/
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail-alt'),  # Frühere Version für Frontend-Kompatibilität: /api/profile/1/
]
