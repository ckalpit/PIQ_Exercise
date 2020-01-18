from django.contrib import admin

from plateiq.core.models.invoice import RawInvoice, InvoiceItem, DigitalInvoice

admin.site.register(DigitalInvoice)
admin.site.register(RawInvoice)
admin.site.register(InvoiceItem)
