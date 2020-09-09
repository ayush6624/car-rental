from datetime import date
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class PickUpDropOff:
    def __init__(self, pickUpLocation, pickUpDate):
        self.pickUpDate = pickUpDate
        self.pickUpLocation = pickUpLocation

    def dropOff(self, dropOffLocation, dropOffDate, returnToSameLocation):
        if(returnToSameLocation == 1):
            self.dropOffLocation = self.pickUpLocation
        else:
            self.dropOffLocation = dropOffLocation

        self.dropOffDate = dropOffDate


class Car(BaseModel):
    carId: int
    carCategory: str
    carModel: str
    carCondition: str
    carRegistrationNo: int
    nameplate: str
    meterReading: float
    fuelType: str
    seater: int
    availability: bool
    transmition: str
    basePrice: float

    def __init__(self, carId):
        self.carId = carId

    class CarModel():
        def __init__(self, carModel):
            self.carModel = carModel

        def car_info(self):
            pass


class BillingDB(BaseModel):
    billId: int
    initialAmount: float
    discountAmount: float
    taxAmount: float
    securityDeposit: float
    finalAmount: float
    billStatus: str
    billDate: date


class Billing(BillingDB):
    def __init__(self, billId):
        self.promo = None
        self.billId = billId

    def new_bill(self, initialAmount, discountAmount, securityDeposit) -> None:
        self.initialAmount = initialAmount
        self.discountAmount = discountAmount
        self.securityDeposit = securityDeposit
        self.taxAmount = (self.initialAmount * 0.18)

    def final_Amount(self, finalAmount) -> float:
        money = 0
        if self.promo:
            money = PromoCode(self.promo).discounted_price(self.initialAmount)
        finalAmount = self.initialAmount + self.securityDeposit + self.taxAmount - money
        return finalAmount


class BookingDetails(Billing):
    bookingStatus: str
    bookingDate: date


class PromoCodeDB(BaseModel):
    code: str
    discountPercentage: float
    minPurchase: float
    expDate: date


class PromoCode(PromoCodeDB):
    def __init__(self, code):
        self.code = code

    def new_code(self, code, discount, minPurchase, exp) -> None:
        self.code = code
        self.discount = discount
        self.minPurchase = minPurchase
        self.expDate = exp

    def validator(self, initial_price: float) -> bool:
        if(initial_price < self.minPurchase):
            return False
        if (datetime.now() > self.expDate):
            return False
        return True

    def discounted_price(self, initial_price: float) -> float:
        money = 0
        if(self.validator(initial_price)):
            money = initial_price * self.discountPercentage/100
            return money
        else:
            return money
