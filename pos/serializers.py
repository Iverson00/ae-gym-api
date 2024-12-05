from rest_framework import serializers
from .models import Product, Member, Purchase, Membership, MembershipTransaction

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False) 

    class Meta:
        model = Product
        fields = "__all__"

class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = "__all__"

class PurchaseSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Purchase
        fields = "__all__"



class MembershipTransactionSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    membership = MembershipSerializer()

    class Meta:
        model = MembershipTransaction
        fields = "__all__"