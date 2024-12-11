from django.urls import path
from . import views
from .analytics import members, membership_earning, product_earning
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r"memberships", views.MembershipViewSet, basename="membership")
router.register(r"products", views.ProductViewSet, basename="product")
router.register(r"members", views.MemberViewSet, basename="member")
router.register(r"purchases", views.PurchaseViewSet, basename="purchase")
router.register(
    r"membership-transactions",
    views.MembershipTransactionViewSet,
    basename="membership-transaction",
)
router.register(
    r"memberships/members/membership-transactions",
    views.MembershipTransactionMembershipMemberViewSet,
    basename="membership-transaction-membership-member",
)
router.register(
    r"excel/memberships", views.ExcelMembershipViewSet, basename="excel-membership"
)
router.register(r"excel/products", views.ExcelProductViewSet, basename="excel-product")
router.register(r"excel/members", views.ExcelMemberViewSet, basename="excel-member")
router.register(
    r"excel/purchases", views.ExcelPurchaseViewSet, basename="excel-purchase"
)
router.register(
    r"excel/membership-transaction",
    views.ExcelMembershipTransactionViewSet,
    basename="excel-membership-transaction",
)

urlpatterns = router.urls + [
    path("secret-key/", views.SecretKeyAPIView.as_view()),
    path("analytics/members/week/", members.get_members_by_this_week),
    path("analytics/members/year/", members.get_members_by_this_year),
    path("analytics/members/day/", members.get_members_by_this_day),
    path("analytics/members/month/", members.get_members_by_this_month),
    path("analytics/members/", members.get_members),
    path("analytics/membership-earnings/", membership_earning.get_membership_earnings),
    path("analytics/membership-earnings/month/", membership_earning.get_membership_earnings_by_month),
    path("analytics/membership-earnings/day/", membership_earning.get_membership_earnings_by_this_day),
    path("analytics/membership-earnings/week/", membership_earning.get_membership_earnings_by_this_week),
    path("analytics/membership-earnings/year/", membership_earning.get_membership_earnings_by_this_year),
    path("analytics/product-earnings/", product_earning.get_product_earnings),
    path("analytics/product-earnings/month/", product_earning.get_product_earnings_by_month),
    path("analytics/product-earnings/day/", product_earning.get_product_earnings_by_this_day),
    path("analytics/product-earnings/week/", product_earning.get_product_earnings_by_this_week),
    path("analytics/product-earnings/year/", product_earning.get_product_earnings_by_this_year),
]
