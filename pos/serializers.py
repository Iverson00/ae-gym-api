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

    class Meta:
        model = MembershipTransaction
        fields = "__all__"

class MembershipTransactionMembershipMemberSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    membership = MembershipSerializer()

    class Meta:
        model = MembershipTransaction
        fields = "__all__"

    def create(self, validated_data):
        member_data = validated_data.pop('member')
        membership_data = validated_data.pop('membership')

        member_serializer = MemberSerializer(data=member_data)
        member_serializer.is_valid(raise_exception=True)
        member = member_serializer.save()  

        membership_serializer = MembershipSerializer(data=membership_data)
        membership_serializer.is_valid(raise_exception=True)
        membership = membership_serializer.save()  

        membership_transaction = MembershipTransaction.objects.create(
            member=member,
            membership=membership,
            **validated_data 
        )

        return membership_transaction
