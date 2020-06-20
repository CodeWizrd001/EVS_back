from rest_framework.response import Response
from .. import *

def check_logged_in(func) :

    def check(*args,**kwargs) : 
        request = args[0]
        if request.user.is_authenticated :
            return func(*args,**kwargs)
        else :
            return Response({"STATUS" : USER_NOT_LOGGED_IN})
    
    return check