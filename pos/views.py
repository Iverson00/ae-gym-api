from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Product, Member, Purchase, Membership, MembershipTransaction
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    ProductSerializer,
    MemberSerializer,
    PurchaseSerializer,
    MembershipSerializer,
    MembershipTransactionSerializer,
)
from rest_framework.viewsets import ReadOnlyModelViewSet
from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer
from .excel_style import COLUMN_HEADER, COLUMN_BODY_STYLES, BODY


class MembershipViewSet(ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = "__all__"

    filter_fields = [
        "membership_type",
        "price",
    ]

    search_fields = [
        "membership_type",
        "price",
    ]


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = "__all__"

    filter_fields = [
        "name",
        "price",
        "image",
        "product_type",
    ]

    search_fields = [
        "name",
        "price",
        "image",
        "product_type",
    ]

    parser_classes = [MultiPartParser, FormParser]


class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = "__all__"
    filter_fields = [
        "first_name",
        "last_name",
        "birth_date",
        "gender",
        "contact",
        "emergency_contact",
    ]
    search_fields = [
        "first_name",
        "last_name",
        "birth_date",
        "gender",
        "contact",
        "emergency_contact",
    ]


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = "__all__"

    filter_fields = [
        "member",
        "product",
        "quantity",
        "price",
        "purchased_at",
    ]

    search_fields = [
        "member",
        "product",
        "quantity",
        "price",
        "purchased_at",
    ]


class MembershipTransactionViewSet(ModelViewSet):
    queryset = MembershipTransaction.objects.all().select_related(
        "member", "membership"
    )
    serializer_class = MembershipTransactionSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = "__all__"

    filter_fields = [
        "member__first_name",
        "member__last_name",
        "member__birth_date",
        "member__gender",
        "member__contact",
        "member__emergency_contact",
        "membership__membership_type",
        "membership__price",
    ]
    search_fields = [
        "member__first_name",
        "member__last_name",
        "member__birth_date",
        "member__gender",
        "member__contact",
        "member__emergency_contact",
        "membership__membership_type",
        "membership__price",
    ]


class ExcelMembershipViewSet(XLSXFileMixin, ReadOnlyModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    renderer_classes = (XLSXRenderer,)
    filename = "memberships.xlsx"

    column_header = COLUMN_HEADER
    body = BODY
    column_data_styles = COLUMN_BODY_STYLES 

class ExcelProductViewSet(XLSXFileMixin, ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    renderer_classes = (XLSXRenderer,)
    filename = "products.xlsx"

    column_header = COLUMN_HEADER
    body = BODY
    column_data_styles = COLUMN_BODY_STYLES 

class ExcelMemberViewSet(XLSXFileMixin, ReadOnlyModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    renderer_classes = (XLSXRenderer,)
    filename = "members.xlsx"

    column_header = COLUMN_HEADER
    body = BODY
    column_data_styles = COLUMN_BODY_STYLES 

class ExcelPurchaseViewSet(XLSXFileMixin, ReadOnlyModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    renderer_classes = (XLSXRenderer,)
    filename = "purchases.xlsx"

    column_header = COLUMN_HEADER
    body = BODY
    column_data_styles = COLUMN_BODY_STYLES 

class ExcelMembershipTransactionViewSet(XLSXFileMixin, ReadOnlyModelViewSet):
    queryset = queryset = MembershipTransaction.objects.all().select_related(
        "member", "membership"
    )
    serializer_class = MembershipTransactionSerializer
    renderer_classes = (XLSXRenderer,)
    filename = "membership_transactions.xlsx"

    column_header = COLUMN_HEADER
    body = BODY
    column_data_styles = COLUMN_BODY_STYLES 
