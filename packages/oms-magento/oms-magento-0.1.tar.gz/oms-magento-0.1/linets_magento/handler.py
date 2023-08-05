# -*- coding: utf-8 -*-
import logging
from datetime import datetime, timedelta

from django.utils import timezone

from linets_magento.connector import Connector, ConnectorException
from linets_magento.settings import api_settings

logger = logging.getLogger(__name__)


class MagentoHandler:
    """
        Handler to connect with Magento
    """
    def __init__(self, base_url=api_settings.MAGENTO['BASE_URL'],
                 api_key=api_settings.MAGENTO['API_KEY'],
                 verify=True):

        self.base_url = base_url
        self.api_key = api_key
        self.verify = verify
        self.connector = Connector(self._headers(), verify_ssl=self.verify)

    def _headers(self):
        """
            Here define the headers for all connections with Magento.
        """
        return {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
            'cache-control': 'no-cache',
        }

    def order_get_last_completed(self, days_count=1):
        """
            Here it makes a request to magento to obtain the orders from a
            specific day (by default days_count = 1).
        """
        date_query = datetime.now() - timedelta(days=days_count)
        params = {
            'searchCriteria[filterGroups][0][filters][0][field]': 'status',
            'searchCriteria[filterGroups][0][filters][0][value]': 'complete',
            'searchCriteria[filterGroups][1][filters][0][field]': 'created_at',
            'searchCriteria[filterGroups][1][filters][0][value]': date_query.strftime('%Y-%m-%d %H:%M:%S'),
            'searchCriteria[filterGroups][1][filters][0][conditionType]': 'gt',
            'fields': 'items[entity_id,status,state,increment_id],search_criteria'
        }
        url = f'{self.base_url}V1/orders'

        logger.debug(params)
        try:
            response = self.connector.get(url, params)
            logger.debug(response)
            return response
        except ConnectorException as error:
            logger.error(error)
            return False

    def order_get_pending_list(self):
        """
            Here it makes a request to magento to obtain the orders with status 'pending'.
        """
        date_query = datetime.now() - timedelta(minutes=5)
        params = {
            'searchCriteria[filterGroups][0][filters][0][field]': 'status',
            'searchCriteria[filterGroups][0][filters][0][value]': 'pending',
            'searchCriteria[filterGroups][1][filters][0][field]': 'created_at',
            'searchCriteria[filterGroups][1][filters][0][value]': date_query.strftime('%Y-%m-%d %H:%M:%S'),
            'searchCriteria[filterGroups][1][filters][0][conditionType]': 'lt',
        }
        url = f'{self.base_url}V1/orders'

        logger.debug(params)
        try:
            response = self.connector.get(url, params)
            logger.debug(response)
            return response
        except ConnectorException as error:
            logger.error(error)
            return False

    def order_get_list(self, status='complete'):
        """
            Here it makes a request to magento to obtain all orders, just use a filter.
            status = 'complete'
        """
        params = {
            'searchCriteria[filterGroups][0][filters][0][field]': 'status',
            'searchCriteria[filterGroups][0][filters][0][value]': status
        }
        url = f'{self.base_url}V1/orders'

        logger.debug(params)
        try:
            response = self.connector.get(url, params)
            logger.debug(response)
            return response
        except ConnectorException as error:
            logger.error(error)
            return False

    def order_get_detail(self, identifier):
        """
        Here it a makes a request to magento to obtain order detail.
        """
        url = f'{self.base_url}V1/orders/{identifier}'

        try:
            response = self.connector.get(url)
            logger.debug(response)
            return response
        except ConnectorException as error:
            logger.error(error)
            return False

    def order_get_items(self, identifier):
        """
        Here it a makes a request to magento to obtain order detail but only
        with the items to ship.

        return:
        {
            "items": [
                {
                    "item_id": 140,
                    "qty_ordered": 1,
                    "sku": "ALCNHDA01B57Z"
                }
            ]
        }
        """
        params = {'fields': 'items[qty_ordered,sku,item_id]'}
        url = f'{self.base_url}V1/orders/{identifier}'
        logger.debug(params)

        try:
            response = self.connector.get(url, params)
            logger.debug(response)
            return response
        except ConnectorException as error:
            logger.error(error)
            return False

    def order_post_ship(self, identifier, items):
        """
        Endpoint calling order ship, this adds the items
        to a shipment to substract the used stock

        Arguments:
        - identity -> Magento order id
        - items -> list with dictionary containing order_item_id and qty
        - items = [{'order_item_id': 9999, 'qty': 1}]

        Return: 999 -> ID Shipment
        """
        payload = {
            'items': [
                {
                    'order_item_id': item['order_item_id'],
                    'qty': item['qty']
                } for item in items
            ],
            'notify': False,
            'appendComment': False
        }

        url = f'{self.base_url}V1/order/{identifier}/ship'

        logger.debug(payload)
        try:
            response = self.connector.post(url, payload)
            logger.debug(response)
            return response
        except ConnectorException as error:
            logger.error(error)
            return False

    def order_post_invoice(self, identifier, items):
        """
        Endpoint calling order invoice, this adds the items
        to a invoice and completes the order

        Arguments:
        - identifier -> Magento order id
        - items -> list with dictionary containing order_item_id and qty
        - items = [{'order_item_id': 9999, 'qty': 1}]

        Return: 999 -> ID Invoice
        """
        payload = {
            'items': [
                {
                    'order_item_id': item['order_item_id'],
                    'qty': item['qty']
                } for item in items
            ],
            'notify': False,
            'appendComment': False
        }

        url = f'{self.base_url}V1/order/{identifier}/invoice'

        logger.debug(payload)
        try:
            response = self.connector.post(url, payload)
            logger.debug(response)
            return response
        except ConnectorException as error:
            logger.error(error)
            return False

    def order_post_comment(self, identifier, comment, status, notify_customer=True):
        """
        Endpoint calling order comment, with this endpoint a comment can be added
        to the order.

        Arguments:
        - identifier -> Magento order id
        - comment -> String with the comment
        - notify_customer -> Boolean to set notify by email to the customer

        Return: True
        """
        payload = {
            'statusHistory': {
                'comment': comment,
                'created_at': timezone.now().strftime('%Y-%m-%d %H:%M:%S'),
                'is_customer_notified': 1 if notify_customer else 0,
                'is_visible_on_front': 1 if notify_customer else 0,
                'status': status,
                'extension_attributes': {}
            }
        }
        url = f'{self.base_url}V1/orders/{identifier}/comments'

        logger.debug(payload)
        try:
            response = self.connector.post(url, payload)
            logger.debug(response)
            return response
        except ConnectorException as error:
            logger.error(error)
            return False

    def order_post_cancel(self, identifier):
        """
        Endpoint calling order cancel, this calling cancels the order
        Arguments:

        - identifier -> Magento order id

        Return: True
        """
        payload = {}
        url = f'{self.base_url}V1/orders/{identifier}/cancel'

        logger.debug(payload)
        try:
            response = self.connector.post(url, payload)
            logger.debug(response)
            return response
        except ConnectorException as error:
            logger.error(error)
            return False
