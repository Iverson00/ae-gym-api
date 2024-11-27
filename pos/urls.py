from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r"memberships", views.MembershipViewSet)
router.register(r"products", views.ProductViewSet)
router.register(r"members", views.MemberViewSet)
router.register(r"purchases", views.PurchaseViewSet)

urlpatterns = router.urls