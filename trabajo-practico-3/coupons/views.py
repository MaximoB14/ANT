from django.shortcuts import render
from .models import Coupon
from .serializers import CouponSerializer
from rest_framework import  viewsets
# Create your views here.


class CouponViewSet(viewsets.ModelViewSet):
    serializer_class = CouponSerializer

    def get_queryset(self):
        coupons = Coupon.objects.all()
        return coupons
