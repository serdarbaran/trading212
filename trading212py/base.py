from __future__ import annotations
from enum import Enum
from datetime import datetime
from typing import List, Optional, Dict
from pydantic import BaseModel
from dataclasses import dataclass

class Order(BaseModel):
    ticker: str #"AAPL_US_EQ"
    quantity: float #0.1
    timeValidity: str #"DAY"
    limitPrice: Optional[float] #100.23
    creationTime: Optional[datetime]
    filledQuantity: Optional[float]
    filledValue: Optional[float]
    id: Optional[int]
    limitPrice: Optional[float]
    status: Optional[str]
    stopPrice: Optional[float]
    strategy: Optional[str]
    type: Optional[str]
    value: Optional[float]

@dataclass
class Dividend(BaseModel):
    gained: Optional[float]
    inCash: Optional[float]
    reinvested: Optional[float]

class Result(BaseModel):
    investedValue: float
    result: float
    resultCoef: float
    value: float

class Pie(BaseModel):
    # Pie Out
    cash: Optional[float] = None
    dividendDetails: Optional[Dividend] = None
    id: Optional[int] = None
    progress: Optional[float] = None
    result: Optional[Result] = None
    status: Optional[str] = None
    # New Pie Input
    name: Optional[str] = None
    dividendCashAction: Optional[str] = None
    endDate: Optional[datetime] = None
    goal: Optional[float] = None
    icon: Optional[Icon] = None
    instrumentShares: Optional[Dict[str, float]] = None
    # New Pie Output
    instruments: Optional[List[Instrument]] = None
    settings: Optional[Settings] = None


class Instrument(BaseModel):
    ticker: str
    name: Optional[str] = None
    type: Optional[str] = None
    isin: Optional[str] = None
    addedOn: Optional[str] = None
    shortname: Optional[str] = None
    result: Optional[Result] = None
    currencyCode: Optional[str] = None
    currentShare: Optional[float] = None
    issues: Optional[List[Issue]] = None
    ownedQuantity: Optional[float] = None
    expectedShare: Optional[float] = None
    workingScheduleId: Optional[int] = None
    maxOpenQuantity: Optional[float] = None
    minTradeQuantity: Optional[float] = None