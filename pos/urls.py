from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r"memberships", views.MembershipViewSet, basename="membership")
router.register(r"products", views.ProductViewSet, basename="product")
router.register(r"members", views.MemberViewSet, basename="member")
router.register(r"purchases", views.PurchaseViewSet, basename="purchase")
router.register(r"membership-transactions", views.MembershipTransactionViewSet, basename="membership-transaction")
router.register(r"memberships/members/membership-transactions", views.MembershipTransactionMembershipMemberViewSet, basename="membership-transaction-membership-member")
router.register(r"excel/memberships", views.ExcelMembershipViewSet, basename="excel-membership")
router.register(r"excel/products", views.ExcelProductViewSet, basename="excel-product")
router.register(r"excel/members", views.ExcelMemberViewSet, basename="excel-member")
router.register(r"excel/purchases", views.ExcelPurchaseViewSet, basename="excel-purchase")
router.register(r"excel/membership-transaction", views.ExcelMembershipTransactionViewSet, basename="excel-membership-transaction")

urlpatterns = router.urls + [
    path("secret-key/", views.SecretKeyAPIView.as_view())
]