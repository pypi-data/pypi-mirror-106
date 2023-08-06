# -*- coding: utf-8 -*-
import logging

from django.db.models import Sum

from linets_enviame.connector import Connector, ConnectorException
from linets_enviame.settings import api_settings

logger = logging.getLogger(__name__)


class EnviameHandler:
    """
        Handler to send shipping payload to Enviame
    """
    def __init__(self, base_url=api_settings.ENVIAME['BASE_URL'],
                 company_id=api_settings.ENVIAME['COMPANY_ID'],
                 api_key=api_settings.ENVIAME['API_KEY'],
                 verify=True):

        self.base_url = base_url
        self.company_id = company_id
        self.api_key = api_key
        self.verify = verify
        self.connector = Connector(self._headers(), verify_ssl=self.verify)

    def _headers(self):
        """
            Here define the headers for all connections with Enviame.
        """
        return {
            'Accept': 'application/json',
            'api-key': self.api_key,
            'Content-Type': 'application/json.1',
        }

    def create_shipping(self):
        raise NotImplementedError(
            'create_shipping is not a method implemented for EnviameHandler')

    def get_shipping_label(self):
        raise NotImplementedError(
            'get_shipping_label is not a method implemented for EnviameHandler')

    def _build_content_description(self, instance):
        """
            This method generates a description in the following form:

                product name one | product name two | product name three or
                UNABLE TO CREATE CONTENT DESC FROM PRODUCTS

            based is the submitted instance.
        """
        items = [
            detail.product.name[:10] for detail in instance.order_details.all()
        ]
        products_str = ' | '.join(items)
        return products_str[0:59] if products_str else 'UNABLE TO CREATE CONTENT DESC FROM PRODUCTS'

    def get_default_payload(self, instance):
        """
            This method generates by default all the necessary data with
            an appropriate structure for Enviame courier.
        """
        try:
            totals = instance.order_details.all().aggregate(
                total_order_weight=Sum('total_weight'), total_price=Sum('total_price')
            )
            total_order_weight = totals['total_order_weight']
            total_price = totals['total_price']
            customer = instance.address.customer
            payload = {
                'shipping_order': {
                    'imported_id': f'{instance.order.external_reference} - {instance.id}',
                    'order_price': str(total_price),
                    'n_packages': instance.order_details.count(),
                    'content_description': self._build_content_description(instance),
                    'type': 'delivery',
                    'weight': str(total_order_weight),
                    'volume': ''
                },
                'shipping_destination': {
                    'customer': {
                        'name': f'{customer.first_name} {customer.last_name}',
                        'phone': customer.phone,
                        'email': customer.email
                    },
                    'delivery_address': {
                        'home_address': {
                            'place': instance.address.commune.name,
                            'full_address': str(instance.address.full_address)
                        }
                    }
                },
                'shipping_origin': {
                    'warehouse_code': api_settings.ENVIAME['COD_BOD']
                },
                'carrier': {
                    'carrier_code': '',
                    'carrier_service': '',
                    'tracking_number': ''
                }
            }

            logger.debug(payload)
            return payload
        except Exception as error:
            logger.error(error)
            return False

    def send_data(self, data):
        """
            This method generate a Enviame shipping.
            If the get_default_payload method returns data, send it here,
            otherwise, generate your own payload.
        """
        url = f'{self.base_url}companies/{self.company_id}/deliveries'

        logger.debug(data)
        try:
            response = self.connector.post(url, data)
            logger.debug(response)
            return response
        except ConnectorException as error:
            logger.error(error)
            return False

    def get_tracking(self, identifier):
        """
            This method obtain a detail a shipping of Enviame.
        """
        url = f'{self.base_url}deliveries/{identifier}'

        try:
            response = self.connector.get(url)
            logger.debug(response)
            return response
        except ConnectorException as error:
            logger.error(error)
            return False
