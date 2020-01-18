from django.urls import path, include
from dynamic_rest.routers import DynamicRouter

from plateiq.consumer.views import InvoiceView, DigitalInvoiceView

router = DynamicRouter()
router.register('invoice', InvoiceView)
router.register('digital_invoice', DigitalInvoiceView, base_name='DigitalInvoiceDetail')

urlpatterns = [
    path('', include(router.urls)),
]
