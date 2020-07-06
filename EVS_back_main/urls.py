from django.urls import path,include
from EVS_back_main.views import user , data

urlpatterns = [
    path("add",data.addData),
    path("get",data.getData),
    path("get/<str:country>",data.getDataByCountry),
    path("getMy/<str:id>",data.getDataById),
    path("getuser",user.getUser),
    path("coins",user.updateCoins)
]
