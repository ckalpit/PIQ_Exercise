from django.urls import path, include
from rest_framework import routers

from plateiq.p_admin.views import InvoiceView, UpdateInvoiceStatusView, DigitalInvoiceDetailView, \
    InvoiceItemView

router = routers.DefaultRouter()
router.register('invoice', InvoiceView)
router.register('update_invoice_status', UpdateInvoiceStatusView)
router.register('digital_invoice', DigitalInvoiceDetailView, base_name='DigitalInvoiceDetail')
router.register('invoice_item', InvoiceItemView)

urlpatterns = [
    path('', include(router.urls)),
]
