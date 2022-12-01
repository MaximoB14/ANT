from django.contrib import admin
from coupons.models import Coupon

# Register your models here.


class CouponAdmin(admin.ModelAdmin):
    list_display = ('name', 'valid_from', 'valid_to', 'discount', 'available')


admin.site.register(Coupon, CouponAdmin)
