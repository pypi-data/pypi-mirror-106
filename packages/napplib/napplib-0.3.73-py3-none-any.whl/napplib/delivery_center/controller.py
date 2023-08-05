import requests, json, logging
from requests.auth import HTTPBasicAuth

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(threadName)-11s %(levelname)-10s %(message)s")

class DeliveryCenterController:

    @classmethod
    def upload_products(self, url, username, password, store_id, product):
        headers = dict()
        headers['Content-Type'] = 'application/json'

        r = requests.post(f'{url}/stores/{store_id}/products',
            headers=headers,
            data=json.dumps(product),
            auth=HTTPBasicAuth(username, password)
        )

        if r.status_code == 201 or r.status_code == 200:
            logging.info(f'Product sent... [{r.status_code}]')
        else:
            logging.error(f'Failed to send Product [{r.status_code}] - {r.content.decode("utf-8")}')

        return r

    @classmethod
    def update_products(self, url, username, password, store_id, product_id, product):
        headers = dict()
        headers['Content-Type'] = 'application/json'

        r = requests.patch(f'{url}/stores/{store_id}/products/{product_id}',
            headers=headers,
            data=json.dumps(product),
            auth=HTTPBasicAuth(username, password)
        )

        if r.status_code == 201 or r.status_code == 200:
            logging.info(f'Product sent... [{r.status_code}]')
        else:
            logging.error(f'Failed to send Product [{r.status_code}] - {r.content.decode("utf-8")}')

        return r

    @classmethod
    def upload_variants(self, url, username, password, store_id, product_id, variants):
        headers = dict()
        headers['Content-Type'] = 'application/json'

        r = requests.post(f'{url}/stores/{store_id}/products/{product_id}/variants',
            headers=headers,
            data=json.dumps(variants),
            auth=HTTPBasicAuth(username, password)
        )

        if r.status_code == 201 or r.status_code == 200:
            logging.info(f'Product sent... [{r.status_code}]')
        else:
            logging.error(f'Failed to create variants [{r.status_code}] - {r.content.decode("utf-8")}')

        return r

    @classmethod
    def update_variants(self, url, username, password, store_id, product_id, variant_id, variants):
        headers = dict()
        headers['Content-Type'] = 'application/json'

        r = requests.patch(f'{url}/stores/{store_id}/products/{product_id}/variants/{variant_id}',
            headers=headers,
            data=json.dumps(variants),
            auth=HTTPBasicAuth(username, password)
        )

        if r.status_code == 201 or r.status_code == 200:
            logging.info(f'Inventory update... [{r.status_code}]')
        else:
            logging.error(f'Failed to update variants [{r.status_code}] - {r.content.decode("utf-8")}')

        return r

    '''
    @classmethod
    def get_variants(self, url, username, password, store_id, external_code):
        headers = dict()
        headers['Content-Type'] = 'application/json'

        params = dict()
        params['store_id'] = store_id
        params['external_code'] = external_code

        r = requests.get(f'{url}/stores/{store_id}/variants',
            headers=headers,
            params=params,
            auth=HTTPBasicAuth(username, password)
        )

        if r.status_code == 200:
            logging.info(f'Get variants... [{r.status_code}]')
        else:
            logging.error(f'Failed to create Inventory [{r.status_code}] - {r.content.decode("utf-8")}')

        return r

    @classmethod
    def get_variants_by_id(self, url, username, password, store_id, variant_id, external_code):
        headers = dict()
        headers['Content-Type'] = 'application/json'

        r = requests.get(f'{url}/stores/{store_id}/variants/{variant_id}',
            headers=headers,
            auth=HTTPBasicAuth(username, password)
        )

        if r.status_code == 200:
            logging.info(f'Get variants by id... [{r.status_code}]')
        else:
            logging.error(f'Failed to create Inventory [{r.status_code}] - {r.content.decode("utf-8")}')

        return r

    @classmethod
    def get_variants_by_store_id(self, url, username, password, store_id, dc_code, external_code):
        headers = dict()
        headers['Content-Type'] = 'application/json'

        r = requests.get(f'{url}/stores/{store_id}/variants?dc_code={dc_code}&external_code={external_code}',
            headers=headers,
            auth=HTTPBasicAuth(username, password)
        )

        if r.status_code == 200:
            logging.info(f'Get variants by id... [{r.status_code}]')
        else:
            logging.error(f'Failed to create Inventory [{r.status_code}] - {r.content.decode("utf-8")}')

        return r

    @classmethod
    def get_product_by_id(self, url, username, password, store_id, product_id):
        headers = dict()
        headers['Content-Type'] = 'application/json'

        r = requests.get(f'{url}/stores/{store_id}/products/{product_id}',
            headers=headers,
            auth=HTTPBasicAuth(username, password)
        )

        if r.status_code == 200:
            logging.info(f'Get variants by id... [{r.status_code}]')
        else:
            logging.error(f'Failed to create Inventory [{r.status_code}] - {r.content.decode("utf-8")}')

        return r


    @classmethod
    def get_categories_by_title_product(self, url, username, password, title_product):
        headers = dict()
        header['Content-Type'] = 'application/json'

        r = requests.get(f'{url}/categories/search?q={title_product}',
            headers=headers,
            auth=HTTPBasicAuth(username, password)
        )
    '''

