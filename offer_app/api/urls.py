from django.urls import path, include                                          # Importiere path und include für URL-Routing
from rest_framework.routers import SimpleRouter                                # Importiere Router für ViewSet-Routing

from .views import OfferViewSet, OfferDetailViewSet, OrderViewSet, RatingViewSet, BusinessUserOrderCountView, BusinessUserCompletedOrderCountView, PlatformStatsView  # Importiere ViewSets und Views

router = SimpleRouter()                                                        # Erstelle neuen Router
router.register(r'offers', OfferViewSet, basename='offer')                    # Registriere OfferViewSet unter 'offers'
router.register(r'offerdetails', OfferDetailViewSet, basename='offerdetail')  # Registriere OfferDetailViewSet unter 'offerdetails'
router.register(r'orders', OrderViewSet, basename='order')                    # Registriere OrderViewSet unter 'orders'
router.register(r'ratings', RatingViewSet, basename='rating')                 # Registriere RatingViewSet unter 'ratings'

urlpatterns = [                                                               # Liste aller URL-Muster für diese Anwendung
    path('', include(router.urls)),                                           # Füge Router-URLs ein
    path('business-users/<int:business_user_id>/order-count/', BusinessUserOrderCountView.as_view(), name='business-user-order-count'),  # Business-User Order-Count
    path('business-users/<int:business_user_id>/completed-order-count/', BusinessUserCompletedOrderCountView.as_view(), name='business-user-completed-order-count'),  # Business-User Completed Order-Count
    path('stats/', PlatformStatsView.as_view(), name='platform-stats'),        # Plattform-Statistiken
]
