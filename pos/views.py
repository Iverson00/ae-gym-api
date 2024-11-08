from rest_framework.viewsets import ModelViewSet
from .models import Product, Membership, Member, Purchase  
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer, MembershipSerializer, MemberSerializer, PurchaseSerializer 


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = "__all__"

    filter_fields = [
        "name",
        "price",
        "stock",
        "product_type",
        "product_description",
    ]

    search_fields = [
        "name",
        "price",
        "stock",
        "product_type",
        "product_description",
    ]
    

class MembershipViewSet(ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = "__all__"
    filter_fields = [
        "membership_type",
        "status",
        "registered_at",
    ]
    search_fields = [
        "membership_type",
        "status",
        "registered_at",
    ]
    
    



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



