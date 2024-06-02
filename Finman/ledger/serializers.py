from rest_framework import serializers

from .models import *
from decimal import Decimal

class EarningSerializer(serializers.ModelSerializer):

	class Meta:
		model = Earning
		fields = '__all__'




class InvestmentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Investment
		fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):

	class Meta:
		model = Purchase
		fields = '__all__'


class TaxSerializer(serializers.ModelSerializer):

	class Meta:
		model = Tax
		fields = '__all__'