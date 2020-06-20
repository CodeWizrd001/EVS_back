from django.db import models
from mongoengine import Document
from mongoengine import StringField , FloatField

class Radiation(Document) :
    rUID = StringField(unique=True,required=True)
    rIns = FloatField() 
    rMin = FloatField()
    rMax = FloatField()
    rAvg = FloatField()
    rCountry = StringField()

    meta = {'collection':'Radiation'}