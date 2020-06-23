from django.db import models
from mongoengine import Document
from mongoengine import StringField , FloatField

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