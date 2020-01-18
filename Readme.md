This is a sample project to demonstrate how Django REST Framework can be used to create RESTful API's

- installation :

To setup the application run
```
bash setup.bash
```

> If there is any error running above command, open the file and try to run each command manually, most of the time this errors are due to older version of virtulaenv

> Post setup instruction will also gets printed when you run setup.bash

Core BO related to Project/Problem statement are inside `core` package of the project which can be shared and extended among multiple projects.

There are two Django Applications inside this Project

1. Consumer
2. PAdmin

Consumer can use following endpoints

POST /consumer/invoice/<id> -> to upload invoice

GET /consumer/invoice/<id> -> to view invoice / to check it's status

GET /consumer/digital_invoice/<id> -> to get Digitized Invoice Information

GET /consumer/digital_invoice?inv_id=<invoice_id> -> to get Digitized Invoice Information by invoice id

Admin can use following endpoints

GET /admin/invoice/<id> -> to see uploaded invoices

POST /admin/update_invoice_status -> to update status of any particular invoice

GET /admin/digital_invoice/<id> -> to view invoices that processing/processed and digitized

GET /admin/digital_invoice?inv_id=<invoice_id> -> to get Digitized Invoice Information by invoice id

POST/PATCH /admin/digital_invoice/<id> -> to manually update any particular invoice

GET/POST/PATCH /admin/invoice_item/<id> -> to view/create/update invoice line items


All of these endpoints are accessible in the DRF's web ui.

sample payload to create or update digital invoice is as given below:
```
{
    "raw_invoice_id": null,
    "invoice_number": "",
    "invoice_date": null,
    "due_date": null,
    "vendor_name": "",
    "vendor_address": {
        "street_address": "",
        "city": "",
        "state": "",
        "postal_code": null
    },
    "buyer_name": "",
    "buyer_address": {
        "street_address": "",
        "city": "",
        "state": "",
        "postal_code": null
    },
    "sub_total": null,
    "tax_percentage": null,
    "tax_applicable": null,
    "discount_percentage": null,
    "discount_applicable": null,
    "amount_payable": null,
    "is_paid": false,
    "invoice_items": [
        {
            "description": "",
            "quantity": "1",
            "unit_price": "2.00",
            "total_price": "2.00"
        }
    ]
}
```
It is not mandatory to pass all fields together, at a time any combination of fields can be passed to create or update any fields
