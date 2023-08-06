# Linets Magento

## Starting

These instructions will allow you to install the library in your django project.

## Current features

1. List orders by filters.
1. Get order detail.
1. Get order products.
1. Create shipment.
1. Create invoice.
1. Update order.
1. Cancel order.

## Pre-requisitos

1. Python >= 3.7
1. requests >= 2
1. Django >= 3,

## Installation

To get the latest stable release from PyPi:

```bash
pip install django-magento
```

or From a build

```bash
git clone https://gitlab.com/linets/ecommerce/oms/integrations/oms-magento
cd {{project}} && git checkout develop
python setup.py sdist
```

and, install in your project Django.

```shell
pip install {{path}}/oms-magento/dist/{{tar.gz file}}
```

### Settings in django project

```python
DJANGO_MAGENTO = {
    'MAGENTO': {
        'BASE_URL': '<MAGENTO_API_URL>',
        'API_KEY': '<MAGENTO_API_KEY>',
    },
}
```

## Usage

```python
from magento.handler import MagentoHandler
handler = MagentoHandler()
```

### List orders in Magento:

Basic list orders.

```python
default_data = handler.get_orders()
```

You can send filter parameters.

```python
params = {
    'searchCriteria[filterGroups][1][filters][0][field]': 'created_at',
    'searchCriteria[filterGroups][1][filters][0][value]': '2021-05-10 12:12:50',
    'searchCriteria[filterGroups][1][filters][0][conditionType]': 'gt',
    'fields': 'items[entity_id,status,state,increment_id],search_criteria'
}

# if params is empty, filter by status will be equal to 'complete'.
default_data = handler.get_orders(params)
```

```python
# Output:
{
    'items': [....],
    'search_criteria': {
        'filter_groups': [
            {
                'filters': [
                    {
                        'field': 'status',
                        'value': 'pending',
                        'condition_type': 'eq'
                    }
                  ]
            },
            {
                'filters': [
                    {
                        'field': 'created_at',
                        'value': '2021-05-14 15:00:37',
                        'condition_type': 'lt'
                    }
                ]
            }
        ]
    },
    'total_count': 0
}
```

Get order detail in Magento:

```python
default_data = handler.get_order_detail(identifier)

# Output:
{
    'base_currency_code': 'CLP',
    'base_discount_amount': 0,
    'base_discount_invoiced': 0,
    'base_grand_total': 31990,
    'base_discount_tax_compensation_amount': 0,
    'base_discount_tax_compensation_invoiced': 0,
    'base_shipping_amount': 0,
    'base_shipping_discount_amount': 0,
    'base_shipping_discount_tax_compensation_amnt': 0,
    'base_shipping_incl_tax': 0,
    'base_shipping_invoiced': 0,
    'base_shipping_tax_amount': 0,
    'base_subtotal': 31990,
    'items': [...],
    'billing_address': {...},
    'payment': {...},
    'status_histories': {...},
    'extension_attributes': {...},
    'payment_additional_info': {...},
    'gift_cards': [...],
    'base_gift_cards_amount': 0,
    'gift_cards_amount': 0,
    'applied_taxes': [...],
    'item_applied_taxes': [...],
    'gw_base_price': '0.0000',
    'gw_price': '0.0000',
    'gw_items_base_price': '0.0000',
    'gw_items_price': '0.0000',
    'gw_card_base_price': '0.0000',
    'gw_card_price': '0.0000',
    'checkout_request_invoice': 'No',
    'rut': '17.716.251-5
}
```

Get products for order:

```python
response = handler.get_order_products(identifier)

# Output:
{
    "items": [
        {
            "item_id": 140,
            "qty_ordered": 1,
            "sku": "ALCNHDA01B57Z"
        }
    ]
}
```

Create shipment:

```python
items = [{'order_item_id': 9999, 'qty': 1}]
response = handler.create_shipment(identifier, items)

Output:
9999
```

Create invoice:

```python
items = [{'order_item_id': 9999, 'qty': 1}]
response = handler.create_invoice(identifier, items)

# Output:
9999
```

Update order:

```python
response = handler.update_order(identifier, comment, status, notify_customer)

# Output:
True
```

Cancel order in Magento:

```python
response = handler.cancel_order(identifier)

# Output:
True
```
