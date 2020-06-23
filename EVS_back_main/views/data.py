# Functional Imports
from rest_framework_mongoengine import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

# Utility Imports
from passlib.hash import pbkdf2_sha256
import pycountry
import datetime
import pymongo
import json
import time

# Custom Error Imports
from EVS_back_main import *
from EVS_back.settings import MONGO_NAME

# Authentication Imports
from django.contrib.auth.decorators import login_required , permission_required
from django.contrib.auth import login , logout , authenticate
from ..utils import check_logged_in

# Exception Imports
from django.http.request import RawPostDataException
from django.db.utils import IntegrityError

# Model Imports
from EVS_back_main.models import Radiation

def getCountry(country) :
    country = country.title()
    country = country.replace("_"," ")
    countriesData = Radiation.objects(rCountry=country)
    countryData = {
        'Country' : country,
        'ins' : [] ,
        'max' : [] ,
        'min' : [] ,
        'avg' : [] ,
    }
    for radiation in countriesData :
        countryData['ins'].append(radiation.rIns)
        countryData['max'].append(radiation.rMax)
        countryData['min'].append(radiation.rMin)
        countryData['avg'].append(radiation.rAvg)
    return(countryData)

@api_view(["POST"])
def addData(request) :
    body = json.loads(request.body)
    cur = Radiation(
        rUID=body['id'] ,
        rIns=body['data'],
        rMax=body['max'],
        rMin=body['min'],
        rAvg=body['avg'],
        rCountry=pycountry.countries.get(alpha_2=body['locale']).name, 
        )
    cur.save()
    return Response({"STATUS":SUCCESS}) 

@api_view(["POST"])
def getData(request) :
    client = pymongo.MongoClient()
    db = client[MONGO_NAME]
    collection = db['Radiation']
    countries = collection.distinct('rCountry')
    countriesData = [] 
    for country in countries :
        countriesData.append(getCountry(country))
    return Response({
        "CountriesData" : countriesData
    })

@api_view(["POST"])
def getDataByCountry(request,country) :
    country = pycountry.countries.get(alpha_2=country).name
    return Response(getCountry(country))

@api_view(["POST"])
def getDataById(request,id) :
    data = Radiation.objects(rUID=id)
    retData = {
        'id':id ,
        'ins' : [] ,
        'min' : [] ,
        'avg' : [] ,
        'max' : [] ,
        'Country': '',
    } 
    for i in data :
        dictData = i.toDict()
        retData['ins'].append(dictData['ins'])
        retData['min'].append(dictData['min'])
        retData['avg'].append(dictData['avg'])
        retData['max'].append(dictData['max'])
    if data != [] :
        retData['Country'] = data[0].rCountry
    return Response(retData)