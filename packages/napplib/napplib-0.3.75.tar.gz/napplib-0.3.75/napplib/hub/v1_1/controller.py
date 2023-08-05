import json
import logging
import requests

from typing import List
from napplib.hub.v1_1.models.product import Product

class HubController:

    @staticmethod
    def patch_inventories(server_url, token, store_id, marketplace_id, inventory_list):
        headers = dict()
        headers['Authorization'] = f'Bearer {token}'

        payload = json.dumps(inventory_list)

        r = requests.patch(f'{server_url}/updateInventory/{store_id}/{marketplace_id}', headers=headers, data=payload)

        return r

    @staticmethod
    def get_store_product_marketplace_limit(server_url, token, marketplace_id, store_id, offset=0, status=None, updatedAfter=None):
        # create headers
        headers = dict()
        headers['Authorization'] = f'Bearer {token}'
        status_list = ['pending_register_product', 'done']

        url = '/storeProductsMarketplace/'

        params = {
            "marketplaceId": marketplace_id,
            "storeId": store_id,
            "offset": offset,
            "limit": 20
        }

        if status:
            if not status in status_list:
                raise Exception(f'{status} Status is not in the default list')
            params["statusProcessing"] = status
        if updatedAfter:
            params["updatedAfter"] = updatedAfter

        response = requests.get(
            f"{server_url}{url}",
            headers=headers,
            params=params
        )

        if response.status_code != 200:
            logging.error(f"/storeProductsMarketplace/ ERROR - {response.status_code} - {response.content if not 'html' in str(response.content) else 'Error'} - {status if status else ''}")
            return []

        if json.loads(response.content)['total'] == 0:
            logging.info(f"/storeProductsMarketplace/ is empty - {status if status else ''}")
            return []

        return json.loads(response.content)

    @staticmethod
    def patch_store_product_marketplace(server_url, token, storeProducts):
        headers = dict()
        headers['Authorization'] = f'Bearer {token}'

        payload = json.dumps(storeProducts)

        r = requests.patch(f'{server_url}/storeProductsMarketplace/?list=true&type=2', headers=headers, data=payload)

        return r

    @staticmethod
    def post_products(server_url, token, products: List[Product]):
        return __post_integrate_products(server_url, token, products)

    @staticmethod
    def post_store_products(server_url, token, store_id, products: List[Product]):
        return __post_integrate_products(server_url, token, products, store_id)

    @staticmethod
    def post_store_products_marketplace(server_url, token, store_id, marketplace_id, products: List[Product]):
        return __post_integrate_products(server_url, token, products, store_id, marketplace_id)


def __post_integrate_products(server_url, token, products: List[Product], store_id=None, marketplace_id=None):
    headers = dict()
    headers['Authorization'] = f'Bearer {token}'

    payload = json.dumps(products)

    url = '/integrateProducts/'

    if store_id:
        url += f'{store_id}/'

        if marketplace_id:
            url += f'{marketplace_id}/'

    r = requests.post(f'{server_url}{url}', headers=headers, data=payload)

    return r         