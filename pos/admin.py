from django.contrib import admin
from .models import Member, Product, Purchase, Membership


admin.site.register(Member)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(Membership)