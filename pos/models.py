from django.db import models

class Membership(models.Model):

    membership_type = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self): 
        return self.membership_type
    
class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255) 
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=255)
    contact = models.CharField(max_length=11)
    emergency_contact = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.first_name} {self.last_name} "


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products", null=True, blank=True)
    product_type = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchased_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.member.first_name} {self.member.last_name} - {self.product.name}"


class MembershipTransaction(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.member.first_name} - {self.membership.membership_type}"