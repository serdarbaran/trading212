# /bin/bash
import requests
from trading212py.config import API_VERSION,ACCOUNT_TYPE,API_KEY
from typing import Optional,Dict

class T212:
    def __init__(self) -> None:
        self._base_url: str = f'https://{ACCOUNT_TYPE}.trading212.com/api/{API_VERSION}'
        self._session: requests.Session = requests.Session()
        self._api_key: str | None = self.__get_api_key()
    
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
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
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
    def _get_account_metadata(self):
        return self.__request(method='GET', endpoint='/equity/account/info')
    
    def _get_account_cash(self):
        return self.__request(method='GET', endpoint='/equity/account/cash')
    
    # Personal Portfolio
    def _get_portfolio(self):
        return self.__request(method='GET', endpoint='/equity/portfolio')
    
    def _get_portfolio_ticker(self, ticker):
        return self.__request(method='GET', endpoint=f'/equity/portfolio/{ticker}')

    # Instruments Metadata
    def _get_exchange_list(self):
        return self.__request(method='GET', endpoint='/equity/metadata/exchanges')
    
    def _get_instrument_list(self):
        return self.__request(method='GET', endpoint='/equity/metadata/instruments')
    
    # Pies
    def _get_pie_list(self):
        return self.__request(method='GET', endpoint='/equity/pies')
    
    def _post_create_pie(self, payload):
        return self.__request(method='POST', endpoint='/equity/pies', json=payload)
    
    def _delete_delete_pie(self, pie_id):
        return self.__request(method='DELETE', endpoint=f'/equity/pies/{pie_id}')

    def _get_pie(self, pie_id):
        return self.__request(method='GET', endpoint=f'/equity/pies/{pie_id}')
    
    def _post_update_pie(self, pie_id, payload):
        return self.__request(method='POST', endpoint=f'/equity/pies/{pie_id}', json=payload)

    # Equity Orders
    def _get_all_orders(self):
        return self.__request(method='GET', endpoint='/equity/orders')
    
    def _post_place_limit_order(self, payload):
        return self.__request(method='POST', endpoint='/equity/orders/limit', json=payload)
    
    def _post_place_market_order(self, payload):
        return self.__request(method='POST', endpoint='/equity/orders/market', json=payload)
    
    def _post_stop_order(self, payload):
        return self.__request(method='POST', endpoint='/equity/orders/stop', json=payload)
                              
    def _post_stop_limit_order(self, payload):
        return self.__request(method='POST', endpoint='/equity/orders/stop_limit', json=payload)
    
    def _delete_cancel_order(self, order_id):
        return self.__request(method='DELETE', endpoint=f'/equity/orders/{order_id}')
    
    def _get_order(self, order_id):
        return self.__request(method='GET', endpoint=f'/equity/orders/{order_id}')
    
    # Historical Items
    def _get_historical_orders(self):
        return self.__request(method='GET', endpoint='/equity/history/orders')
    
    def _get_dividends(self):
        return self.__request(method='GET', endpoint='/equity/history/dividends')
    
    def _get_exports_list(self):
        return self.__request(method='GET', endpoint='/equity/history/exports')
    
    def _post_exports(self,payload):
        return self.__request(method='GET', endpoint=f'/equity/history/exports', json=payload)
    
    def _get_transactions(self):
        return self.__request(method='GET', endpoint='/equity/history/transactions')
    

    # Methods
    # Account Data
    def account_metadata(self):
        '''Returns the account metadata, including account type, currency, and other account details.'''
        return self._get_account_metadata()
    
    def account_cash(self):
        '''Returns the account cash balance.'''
        return self._get_account_cash()

    # Personal Portfolio
    def portfolio(self):
        '''Returns the portfolio, including the positions and metadata for each position.
        '''
        return self._get_portfolio()

    def portfolio_ticker(self, ticker):
        '''Returns the portfolio details for a specific ticker.

        Args:
            ticker (str): The ticker symbol of the position to retrieve.
        '''
        return self._get_portfolio_ticker(ticker=ticker)

    # Instruments Metadata
    def exchange_list(self):
        '''Returns the list of exchanges supported by Trading212.'''
        return self._get_exchange_list()

    def instrument_list(self):
        '''Returns the list of instruments supported by Trading212.'''
        return self._get_instrument_list()

    # Pies
    def pie_list(self):
        '''Returns the list of Pies (Portfolio Investment Environments) created by XXX user.'''
        return self._get_pie_list()

    def create_pie(self, payload):
        '''Creates a new Pie (Portfolio Investment Environment) with the provided payload.

        Args:
            payload (dict): The payload containing the details of the new Pie.
        '''
        return self._post_create_pie(payload=payload)
    
    def delete_pie(self, pie_id):
        '''Deletes the Pie with the specified pie_id.

        Args:
            pie_id (str): The ID of the Pie to delete.
        '''
        return self._delete_delete_pie(pie_id=pie_id)

    def get_pie(self, pie_id):
        '''Returns the details of the Pie with the specified pie_id.

        Args:
            pie_id (str): The ID of the Pie to retrieve.
        '''
        return self._get_pie(pie_id=pie_id)

    def update_pie(self, pie_id, payload):
        '''Updates the Pie with the specified pie_id using the provided payload.

        Args:
            pie_id (str): The ID of the Pie to update.
            payload (dict): The payload containing the updated details of the Pie.
        '''
        return self._post_update_pie(pie_id=pie_id, payload=payload)

    # Equity Orders
    def all_orders(self):
        '''Returns all orders placed by XXX user.'''
        return self._get_all_orders()

    def place_limit_order(self, payload):
        '''Places a limit order with the provided payload.

        Args:
            payload (dict): The payload containing the details of the limit order.
        '''
        return self._post_place_limit_order(payload=payload)

    def place_market_order(self, payload):
        '''Places a market order with the provided payload.

        Args:
            payload (dict): The payload containing the details of the market order.
        '''
        return self._post_place_market_order(payload=payload)

    def stop_order(self, payload):
        '''Places a stop order with the provided payload.

        Args:
            payload (dict): The payload containing the details of the stop order.
        '''
        return self._post_stop_order(payload)

    def stop_limit_order(self, payload):
        '''Places a stop limit order with the provided payload.

        Args:
            payload: (dict) The payload containing the details of the stop limit order.
        '''
        return self._post_stop_limit_order(payload=payload)

    def cancel_order(self, order_id):
        '''Cancels the order with the specified order_id.

        Args:
            order_id (str): The ID of the order to cancel.
        '''
        return self._delete_cancel_order(order_id=order_id)

    def order(self, order_id):
        '''Returns the details of the order with the specified order_id.

        Args:
            order_id (str): The ID of the order to retrieve.
        '''
        return self._get_order(order_id)

    # Historical Items
    def historical_orders(self):
        '''Returns the historical orders for XXX user.'''
        return self._get_historical_orders()

    def dividends(self):
        '''Returns the dividends for XXX user.'''
        return self._get_dividends()

    def exports_list(self):
        '''Returns the list of exports for XXX user.'''
        return self._get_exports_list()

    def exports(self, payload):
        '''Creates a new export with the provided payload.

        Args:
            payload (dict): The payload containing the details of the export.
        '''
        return self._post_exports(payload=payload)

    def transactions(self):
        '''Returns the transactions for XXX user.'''
        return self._get_transactions()