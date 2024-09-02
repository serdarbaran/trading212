# /bin/bash
import requests
from trading212_py.config import API_VERSION,ACCOUNT_TYPE,API_KEY
from typing import Optional,Dict

#BASE_URL = "https://api.t212.com/v1"

class T212:
    def __init__(self) -> None:
        self._base_url: str = f'https://{ACCOUNT_TYPE}.trading212.com/api/{API_VERSION}'
        self._session: requests.Session = requests.Session()
        self._api_key: str | None = self.__get_api_key()
        self._headers = {
            'Authorization': f'{self._api_key}',
            'Content-Type': 'application/json'
        }
    
    def __get_api_key(self) -> str:
        try:
            if API_KEY is None: raise Exception("T212_API_KEY environment variable has been retreived.")
            else: return API_KEY
        except KeyError as e:
            raise Exception(f"{e} - Please set the T212_API_KEY environment variable.")

    def __request(self, method:str=None, endpoint:str=None, query_params=None, json:Optional[Dict]=None, **kwargs) -> requests.Response:
        try:
            response: requests.Response = self._session.request(
                method=method.upper(),
                url=f'{self._base_url}{endpoint}',
                headers={
                    "Authorization": self._api_key,
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    "content-type": "application/json; charset=UTF-8",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9"
                },
                json=json,
                params=query_params, **kwargs
            )
            response.raise_for_status()
            if response.status_code == 200: return response.json()
        except Exception as e:
            raise Exception(f"Error making request: {e}")

    # Account Data
    def get_account_metadata(self):
        return self.__request(method='GET', endpoint='/equity/account/info')
    
    def get_account_balance(self):
        return self.__request(method='GET', endpoint='/equity/account/balance')
    
    # Personal Portfolio
    def get_portfolio(self):
        return self.__request(method='GET', endpoint='/equity/portfolio')
    
    def get_portfolio_ticker(self, ticker):
        return self.__request(method='GET', endpoint=f'/equity/portfolio/{ticker}')

    # Instruments Metadata
    def get_exchange_list(self):
        return self.__request(method='GET', endpoint='equity/metadata/exchanges')
    
    def get_instrument_list(self):
        return self.__request(method='GET', endpoint='equity/metadata/instruments')
    
    # Pies
    def get_pie_list(self):
        return self.__request(method='GET', endpoint='/equity/pies')
    
    def create_pie(self, payload):
        return self.__request(method='POST', endpoint='/equity/pies', json=payload)
    
    def delete_pie(self, pie_id):
        return self.__request(method='DELETE', endpoint=f'/equity/pies/{pie_id}')

    def get_pie(self, pie_id):
        return self.__request(method='GET', endpoint=f'/equity/pies/{pie_id}')
    
    def update_pie(self, pie_id, payload):
        return self.__request(method='POST', endpoint=f'/equity/pies/{pie_id}', json=payload)

    # Equity Orders
    def get_all_orders(self):
        return self.__request(method='GET', endpoint='/equity/orders')
    
    def post_place_limit_order(self, payload):
        return self.__request(method='POST', endpoint='/equity/orders/limit', json=payload)
    
    def post_place_market_order(self, payload):
        return self.__request(method='POST', endpoint='/equity/orders/market', json=payload)
    
    def post_stop_order(self, payload):
        return self.__request(method='POST', endpoint='/equity/orders/stop', json=payload)
                              
    def post_stop_limit_order(self, payload):
        return self.__request(method='POST', endpoint='/equity/orders/stop_limit', json=payload)
    
    def cancel_order(self, order_id):
        return self.__request(method='DELETE', endpoint=f'/equity/orders/{order_id}')
    
    def get_order(self, order_id):
        return self.__request(method='GET', endpoint=f'/equity/orders/{order_id}')
    
    # Historical Items
    def get_historical_orders(self):
        return self.__request(method='GET', endpoint='/equity/history/orders')
    
    def get_dividends(self):
        return self.__request(method='GET', endpoint='/equity/history/dividends')
    
    def get_exports_list(self):
        return self.__request(method='GET', endpoint='/equity/history/exports')
    
    def post_exports(self,payload):
        return self.__request(method='GET', endpoint=f'/equity/history/exports', json=payload)
    
    def get_transactions(self):
        return self.__request(method='GET', endpoint='/equity/history/transactions')
    