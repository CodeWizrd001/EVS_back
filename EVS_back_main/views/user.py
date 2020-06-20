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
from django.contrib.auth.decorators import login_required , permission_required
from django.contrib.auth import login , logout , authenticate
from ..utils import check_logged_in

# Exception Imports
from django.http.request import RawPostDataException
from django.db.utils import IntegrityError