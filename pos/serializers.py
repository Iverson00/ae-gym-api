from rest_framework import serializers
from .models import Product, Member, Purchase, Membership

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"

class MemberSerializer(serializers.ModelSerializer):
    membership_type = serializers.CharField(source='membership.membership_type', read_only=True)

    class Meta:
        model = Member
        fields = [
            'id', 
            'first_name', 
            'last_name', 
            'birth_date', 
            'gender', 
            'contact', 
            'emergency_contact', 
            'membership',
            'membership_type',  
            'registered_at',
        ]
        
def get_membership_type(self, obj):
        return obj.membership.membership_type if obj.membership else None

class PurchaseSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Purchase
        fields = "__all__"
