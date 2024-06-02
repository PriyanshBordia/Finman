import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class Earning(models.Model):
	"""
	"""
	class IncomeType(models.IntegerChoices):
		SALARY = 0, _("Salary")
		CAPITAL_GAINS = 1, _("Capital Gains")

	uuid = models.UUIDField(default=uuid.uuid4, editable=False) 
	
	type = models.IntegerField(choices=IncomeType)
	amount = models.DecimalField(max_digits=10, decimal_places=2)

	date = models.DateTimeField()

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	meta = models.JSONField(default=dict)

	class Meta:
		"""
		"""
		verbose_name = "Earning"
		verbose_name_plural = "Earnings"


class Investment(models.Model):
	"""
	A model representing an investment.

	Attributes:
		name (str): The name of the investment.
		amount (Decimal): The amount invested.
		rate (Decimal): The interest rate of the investment.
		year

	Meta:
		verbose_name (str): A human-readable name for the model.
		verbose_name_plural (str): A human-readable plural name for the model.
	"""

	class AssetClass(models.IntegerChoices):
		BONDS = 0, _("Bond")
		RARE_EARTH_METALS = 1, _("Rare Earth Metal")
		REAL_ESTATE = 2, _("Real Estate")
	
	class Asset(models.IntegerChoices):
		SILVER = 0, _("Silver")
		GOLD = 1, _("Gold")
		PLATINUM = 2, _("Platinum")
		GSEC = 3, _("Government Security")
		SDL = 4, _("State Development Loan")
		SGB = 5, _("Soverign Gold Bond")
		TBill = 6, _("Treasury Bill")

	uuid = models.UUIDField(default=uuid.uuid4, editable=False) 

	asset = models.CharField(max_length=255, choices=Asset, default=Asset.GOLD)
	type = models.CharField(max_length=255, choices=AssetClass, default=AssetClass.RARE_EARTH_METALS)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	
	date = models.DateTimeField()
	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	meta = models.JSONField(default=dict)
	
	class Meta:
		"""
		This class defines metadata options for the Investment model.
		"""
		verbose_name = "Investment"
		verbose_name_plural = "Investments"


class Purchase(models.Model):
	"""
	"""
	class Category(models.IntegerChoices):
		ELECTRONICS = 0, _("Electronics")

	uuid = models.UUIDField(default=uuid.uuid4, editable=False) 

	type = models.IntegerField(choices=Category)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	invoice = models.FileField()
	
	date = models.DateTimeField()

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	meta = models.JSONField(default=dict)	
	
	class Meta:
		"""
		"""
		verbose_name = "Purchase"
		verbose_name_plural = "Purchases"


class Tax(models.Model):
	"""
	"""
	class TaxType(models.IntegerChoices):
		INCOME = 0, _("Income Tax")

	uuid = models.UUIDField(default=uuid.uuid4, editable=False) 

	type = models.IntegerField(choices=TaxType)

	date = models.DateTimeField()

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	meta = models.JSONField(default=dict)

	class Meta:
		"""
		"""
		verbose_name = "Tax"
		verbose_name_plural = "Taxes"
