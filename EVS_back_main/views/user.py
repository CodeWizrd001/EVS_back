# Functional Imports
from rest_framework_mongoengine import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

# Utility Imports
from passlib.hash import pbkdf2_sha256
import datetime
import json
import time

# Custom Error Imports
from EVS_back_main import *

# Authentication Imports
from ..utils import check_logged_in

# Exception Imports
from django.http.request import RawPostDataException
from django.db.utils import IntegrityError

# Model Imports
from EVS_back_main.models import User

@api_view(['POST']) 
def getUser(request) : 
    data = request.data 
    uid = data['uid']
    try :
        user = User.objects.get(uUID=uid)
    except User.DoesNotExist :
        user = User(
            uUID=uid
        )
        user.save()
    except :
        raise 
    return Response(user.toDict())

@api_view(['POST']) 
def updateCoins(request) :
    data = request.data 
    uid = data['id']
    try :
        user = User.objects.get(uUID=uid)
    except :
        raise 
    user.uCoins = data['coins'] 
    user.save() 
    return Response({})