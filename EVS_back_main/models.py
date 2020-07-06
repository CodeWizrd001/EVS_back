from django.db import models
from mongoengine import Document
from mongoengine import StringField , FloatField , IntField , BooleanField
from mongoengine import ListField

class Radiation(Document) :
    rUID = StringField(required=True)
    rIns = FloatField() 
    rMin = FloatField()
    rMax = FloatField()
    rAvg = FloatField()
    rCountry = StringField()

    meta = {'collection':'Radiation'}

    def toDict(self) :
        return {
            'id' : self.rUID ,
            'ins' : self.rIns ,
            'min' : self.rMin ,
            'avg' : self.rAvg ,
            'max' : self.rMax ,
            'Country' : self.rCountry
        }

class User(Document) :
    uUID = StringField(required=True) 
    uCoins = IntField(default = 0)
    uPurchased = ListField(default=[
        True,False,
        False,False,
        False,False])
    uPremium = BooleanField(default=False)

    meta = {'collection':'User'}
    
    def toDict(self) :
        return {
            'id' : self.uUID  ,
            'uCoins' : self.uCoins ,
            'uPurchased' : self.uPurchased, 
            'uPremium' : self.uPremium
        }