# Trading212_py Module

This is an unofficial Python client for the [Trading212 API](https://t212public-api-docs.redoc.ly/)
## Installation

You can install the package using pip:

```bash
pip install trading212py
```

## Configuration
### Environment Variables
Create a directory and call it .env
Create two separate files called .secret and .shared

```
.env/
|
|- .secret
|- .shared
```

#### Content of the .shared file
Add `ACCOUNT_TYPE` variable.

Options:
`ACCOUNT_TYPE="demo"` or `ACCOUNT_TYPE="live"`

#### Content of the .secret file
Add `T212_API_KEY` and `T212_DEMO_API_KEY` variables. 

Example: `T212_API_KEY='1234.....abcd'`

>Note: If the app is pushed to Production or running inside a docker container, then these variables will be overwitten with the existing environment variables. For that reason, add those KEYS in your platform's environments variables. 


## Usage

```
from trading212py import T212

def main():

    t212 = T212()
    print(t212.account_metadata())

if __name__ == '__main__':
    main()
```

### Orders
```python
newLimitOrder: Order = Order(limitPrice=90.23, quantity=0.1, ticker='AAPL_US_EQ', timeValidity='DAY')
print(t212.place_limit_order(payload=newLimitOrder))

>>> creationTime='2024-09-07T03:05:32.603+03:00' filledQuantity=0.0 filledValue=None id=19150387579 status=<OrderStatus.NEW: 'NEW'> strategy='QUANTITY' type='LIMIT' value=None limitPrice=90.23 quantity=0.1 ticker='AAPL_US_EQ' timeValidity=None stopPrice=None
```

Alternatively you can pass the json payload to the relevant Class.
```python
payload = {
    "limitPrice":90.23,
    "quantity":0.1,
    "ticker":'AAPL_US_EQ',
    "timeValidity"='DAY'
}
print(t212.place_limit_order(payload=Order(**payload)))
```

```python
newMarketOrder: Order = Order(quantity=0.1, ticker='AAPL_US_EQ')
t212.place_market_order(payload=newMarketOrder)
```


```python
from trading212py.base import ExportPayload
payload = {
    "dataIncluded": {
        "includeDividends": True,
        "includeInterest": True,
        "includeOrders": True,
        "includeTransactions": True
    },
    "timeFrom": "2019-08-24T14:15:22Z",
    "timeTo": "2024-09-07T14:15:22Z"
    }
print(t212.exports(payload=ExportPayload(**payload)))
```


# Disclaimer
Nor me or Trading212 are responsible for the use of this API, first make sure that everything works well through the use of a DEMO account, then switch to REAL mode.

In addition, I don't take responsibility for the accuracy of the information reported here and the proper functioning of the API

All trademarks, logos and brand names are the property of their respective owners. All company, product and service names used in this website are for identification purposes only.