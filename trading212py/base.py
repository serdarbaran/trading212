from __future__ import annotations
from enum import Enum
from datetime import datetime
from typing import List, Optional, Dict,Any
from pydantic import BaseModel
from dataclasses import dataclass


class OrderStatus(Enum): #TODO: #1 Not yet implemented. 
    LOCAL = 'LOCAL'
    NEW = 'NEW'
    PENDING = "PENDIN"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


'''
Account Data Classes
'''
class AccountMetadata(BaseModel):
    id:int
    currencyCode:str

class AccountCash(BaseModel):
    free:float
    total:float
    ppl:float
    result:float
    invested:float
    pieCash:float
    blocked:float | None

'''
Personal Portfolio Classes
'''
class Position(BaseModel):
    ticker: str
    quantity: float
    averagePrice: float
    currentPrice: float
    ppl: float
    fxPpl: float
    initialFillDate: str
    frontend: str
    maxBuy: float
    maxSell: float
    pieQuantity: float

# class Positions(BaseModel):
#     positions: List[Position]

'''
Instruments Metadata CLasses
'''
class TimeEvent(BaseModel):
    date: str
    type: str

class WorkingSchedule(BaseModel):
    id: int
    timeEvents: List[TimeEvent]

class Exchange(BaseModel):
    id: int
    name: str
    workingSchedules: Optional[List[WorkingSchedule]]

class Exchanges(BaseModel):
    exchanges: List[Exchange]


class Instrument(BaseModel):
    addedOn: str
    currencyCode:str
    isin:str
    maxOpenQuantity: int | float
    minTradeQuantity: int | float
    name:str
    shortname: Optional[str]
    ticker: str
    type: str
    workingScheduleId:int

class Instruments(BaseModel):
    instruments: List[Instrument]

'''
Pie Classes Section
'''
# Pie
class PieIssue(BaseModel):
    name: Optional[str] = None
    severity: Optional[str]= None

class Result(BaseModel):
    investedValue: Optional[float]= None
    result: Optional[float] = None
    resultCoef: Optional[float] = None
    value: Optional[float] = None

class PieInstrument(BaseModel):
    currentShare: Optional[float] = None
    expectedShare: Optional[float] = None
    #issues: Optional[List[PieIssue]] = None
    issues: Optional[Any] = None
    ownedQuantity: Optional[float] = None
    result: Optional[Result] = None
    ticker: str

class Settings(BaseModel):
    creationDate: Optional[str] = None
    dividendCashAction: Optional[str] = None
    endDate: Optional[str] = None
    goal: Optional[float] = None
    icon: Optional[str] = None
    id: Optional[int] = None
    initialInvestment: Optional[float] = None
    instrumentShares: Optional[Dict[str, float]] = None
    name: Optional[str] = None
    pubicUrl:Optional[str] = None

class Pie(BaseModel):
    instruments: Optional[List[PieInstrument]] = None
    settings: Optional[Settings] = None


# Pie List
class DividendDetails(BaseModel):
    gained:float
    inCash:float
    reinvested:float

class PieListItem(BaseModel):
    cash:float
    dividendDetails:DividendDetails
    id:int
    progress:Optional[float]
    result:Result
    status:Optional[str]

class PieList(BaseModel):
    pies:List[PieListItem]

'''
Equity Orders Classes
'''
class Order(BaseModel):
    creationTime: str = None
    filledQuantity: Optional[float] = None
    filledValue: Optional[float] = None
    id: Optional[int] = None
    status: Optional[OrderStatus] = None
    strategy: Optional[str] = None
    type: Optional[str] = None
    value: Optional[float] = None
    # New Order Parameters
    limitPrice: Optional[float] = None
    quantity: Optional[float] = None
    ticker: Optional[str] = None
    timeValidity: Optional[str] = None
    stopPrice: Optional[str] = None

class Orders(BaseModel):
    orders: List[Order]

'''
Historical Items Classes
'''
class Tax(BaseModel):
    fillId: Optional[str]
    name: Optional[str]
    quantity: Optional[float]
    timeCharged: Optional[datetime]

class HistoricalOrder(BaseModel):
    dateCreated: Optional[datetime]
    dateExecuted: Optional[datetime]
    dateModified: Optional[datetime]
    executor: Optional[str]
    fillCost: Optional[float]
    fillId: Optional[int]
    fillPrice: Optional[float]
    fillResult: Optional[float]
    fillType: Optional[str]
    filledQuantity: Optional[float]
    filledValue: Optional[float]
    id: Optional[int]
    limitPrice: Optional[float]
    orderedQuantity: Optional[float]
    orderedValue: Optional[float]
    parentOrder: Optional[int]
    status: Optional[str]
    stopPrice: Optional[int]
    taxes: Optional[List[Tax]]
    ticker: Optional[str]
    timeValidity: Optional[str]
    type: Optional[str]

class HistoricalOrderResponseModel(BaseModel):
    items: Optional[List[HistoricalOrder]]
    nextPagePath: Optional[str] = None

class HistoricalItem(BaseModel):
    cursor:Optional[int]=None
    ticker:Optional[str]=None
    limit:Optional[int]=None

# Dividend
class DividendItem(BaseModel):
    amount: Optional[float]
    amountInEuro: Optional[float]
    grossAmountPerShare: Optional[float]
    paidOn: Optional[datetime]
    quantity: Optional[float]
    reference: Optional[str]
    ticker: Optional[str]
    type: Optional[str]

class DividendResponseModel(BaseModel):
    items: Optional[List[DividendItem]]
    nextPagePath: Optional[str]

# Export
class DataIncluded(BaseModel):
    includeDividends: bool
    includeInterest: bool
    includeOrders: bool
    includeTransactions: bool

class ExportReport(BaseModel):
    dataIncluded: Optional[DataIncluded]
    downloadLink: Optional[str]
    reportId: Optional[int]
    status: Optional[str]
    timeFrom: Optional[datetime]
    timeTo: Optional[datetime]
    response: Optional[str]