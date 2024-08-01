from rest_framework.routers import DefaultRouter
from .viewsets import *

router = DefaultRouter()
router.register(r'earning', EarningModelViewSet)
router.register(r'tax', InvestmentModelViewSet)
router.register(r'tax', PurchaseModelViewSet)
router.register(r'tax', TaxModelViewSet)