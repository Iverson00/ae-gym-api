from rest_framework import serializers
from .models import Product, Membership, Member, Purchase



class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class MembershipSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Membership
            fields = "__all__"



class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = "__all__"


class PurchaseSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Purchase
        fields = "__all__"
