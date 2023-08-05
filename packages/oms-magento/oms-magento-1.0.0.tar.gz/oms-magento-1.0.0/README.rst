# Linets Magento

## Starting

These instructions will allow you to install the library in your django project.

## Current features

1. Generate order in Magento.
1. Generate default data for create order in Magento.

## Pre-requisitos

1. Python >= 3.7
1. requests >= 2
1. Django >= 3,

## Installation

To get the latest stable release from PyPi:

```bash
pip install oms-magento
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
LINETS_MAGENTO = {
    'MAGENTO': {
        'BASE_URL': 'https://linets.api.magento.io/rest/all/',
        'API_KEY': '7d06682sdgff6d06682sdgff66d06682sdgff66',
    },
}
```

## Usage

```python
from linets_magento.handler import MagentoHandler
handler = MagentoHandler()
```

### List orders in Magento:

List oders by days count.

```python
default_data = handler.order_get_last_completed(days_count=5)
```

List orders with status pending.

```python
default_data = handler.order_get_pending_list()
```

List all orders, can filter by status, default(status = 'complete')

```python
default_data = handler.order_get_list(status='complete')
```

All list methods return:

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

Get detail order in Magento:

```python
default_data = handler.order_get_detail(identifier)

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

Get items for order:

```python
response = handler.order_get_items(identifier)

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

Add the items to a shipment to substract the used stock:

```python
from linets_magento.handler import MagentoHandler

handler = MagentoHandler()
response = handler.order_post_ship(identifier, items)

Output:
9999
```

Adds the items to a invoice and completes the order:

```python
response = handler.order_post_invoice(identifier, items)

# Output:
9999
```

Add comment and update status for order in Magento:

```python
response = handler.order_post_comment(identifier, comment, status, notify_customer)

# Output:
True
```

Cancel order in Magento:

```python
response = handler.order_post_cancel(identifier)

# Output:
True
```
