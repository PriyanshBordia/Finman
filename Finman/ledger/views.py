
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import *
from .models import *
from .serializers import *


def home(request):
	return render(request, "home.html")


@api_view(['GET'])
def api(request):
	return Response({"success": True, "data": request.user.username})


class EarningModelViewSet(viewsets.ModelViewSet):
	queryset = Earning.objects.all().order_by('id')
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