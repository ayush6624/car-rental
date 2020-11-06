from datetime import date
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
# from utils.config import TAX_AMOUNT


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
    photo: str

    def __init__(self, carId):
        self.carId = carId

    class CarModel():
        def __init__(self, carModel):
            self.carModel = carModel

        def carInfo(self):
            pass


class Amount(BaseModel):
    initialAmount: float
    securityDeposit: float
    finalAmount: Optional[float] = None


class BillingDB(BaseModel):
    billId: str
    billStatus: str
    amount: Amount
    promo: Optional[str] = None
    billDate: Optional[datetime] = None

# promo:str -> Billing (if exists in db) -> return trye
# else false


class Billing:
    def __init__(self, amount: Amount, promo=None):
        self.initialAmount = amount.initialAmount
        self.securityDeposit = amount.securityDeposit
        self.taxAmount = self.initialAmount * 0.18
        self.promo = promo

    def finalAmount(self) -> float:
        money = 0
        if self.promo:
            print("here")
            money = PromoCode(self.promo).discountedPrice(self.initialAmount)
        finalAmount = self.initialAmount + self.securityDeposit + self.taxAmount - money
        return finalAmount


class BookingDetails(Billing):
    bookingStatus: str
    bookingDate: date


class PromoCodeDB(BaseModel):
    code: str
    discountPercentage: float
    minPurchase: float


class PromoCode:
    def __init__(self, code):
        self.code = code
        self.minPurchase = 1000

    def newCode(self, code, discount, minPurchase) -> None:
        """Admin Interface

        Args:
            code (str): Code
            discount (float): Percentage
            minPurchase (float): Minimum Purchase
        """
        self.code = code
        self.discount = discount
        self.minPurchase = minPurchase

    def validator(self, initial_price: float) -> bool:
        if(initial_price < self.minPurchase):
            return False
        return True

    def discountedPrice(self, initial_price: float) -> float:
        money = 0
        if(self.validator(initial_price)):
            money = initial_price * 0.10  # update the constant
        return money


amount = {"initialAmount": 1000, "securityDeposit": 2500}
bill = Billing(Amount(**amount), promo="abc")
print(bill.finalAmount())
