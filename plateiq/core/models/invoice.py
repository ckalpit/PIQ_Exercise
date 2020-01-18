from django.core.validators import FileExtensionValidator
from django.db import models

from plateiq.core.models.common import Address


class RawInvoice(models.Model):
    STATUS = [
        (10, 'To Be Digitized'),
        (20, 'Digitization Started'),
        (30, 'Digitization Validated'),
        (40, 'Digitized'),
    ]
    code = models.CharField(max_length=30, editable=False)
    file = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    file_name = models.CharField(max_length=30, editable=False)
    uploaded_by = models.IntegerField(null=False)
    uploaded_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS)

    def __str__(self):
        return self.file.name


class DigitalInvoice(models.Model):
    code = models.CharField(max_length=30)
    raw_invoice_id = models.OneToOneField(RawInvoice, on_delete=models.CASCADE, db_index=True,
                                          db_column='raw_invoice_id', null=False)
    invoice_number = models.CharField(max_length=50, null=True)
    invoice_date = models.DateField(null=True)
    due_date = models.DateField(null=True)
    vendor_name = models.CharField(max_length=50, null=True)
    vendor_address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='vendor_address', null=True,
                                       blank=True)
    buyer_name = models.CharField(max_length=50, null=True)
    buyer_address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='buyer_address', null=True,
                                      blank=True)
    sub_total = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    tax_percentage = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    tax_applicable = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    discount_percentage = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    discount_applicable = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    amount_payable = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    is_paid = models.BooleanField(default=False, null=True)
    created_on = models.DateTimeField(auto_now=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)


class InvoiceItem(models.Model):
    digital_invoice_id = models.ForeignKey(DigitalInvoice, on_delete=models.CASCADE, db_column='digital_invoice_id')
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(decimal_places=2, max_digits=10)
    total_price = models.DecimalField(decimal_places=2, max_digits=10)


"""
{
    "raw_invoice_id": "1",
    "invoice_number": "123",
    "invoice_items": [
{"description" : "item 2", 
"quantity" : "1", 
"unit_price" : "2", 
"total_price" : "2"}
]
}
"""
