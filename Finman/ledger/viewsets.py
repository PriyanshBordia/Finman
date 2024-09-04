from rest_framework import viewsets

from .models import *
from .serializers import *


class EarningModelViewSet(viewsets.ModelViewSet):
	queryset = Earning.objects.all()
	serializer_class = EarningSerializer


class InvestmentModelViewSet(viewsets.ModelViewSet):
	queryset = Investment.objects.all()
	serializer_class = InvestmentSerializer


class PurchaseModelViewSet(viewsets.ModelViewSet):
	queryset = Purchase.objects.all()
	serializer_class = PurchaseSerializer


class TaxModelViewSet(viewsets.ModelViewSet):
	queryset = Tax.objects.all()
	serializer_class = TaxSerializer