from django.urls import path

from .views import ProfileDetailView

urlpatterns = [
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
]
