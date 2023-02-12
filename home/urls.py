from django.contrib import admin
from django.urls import path
from home import views
#import home.mqtt

urlpatterns = [
    path("",views.index,name="home"),
    path("mobile",views.mobile,name="mobile"),
    #path("about",views.about,name="about"),
    path("mob",views.mob,name="mob"),
    path("mob1",views.mob1,name="mob1"),
    path("new",views.new,name="new"),
    path("new1",views.new1,name="new1"),
    path("new_otp",views.new_otp,name="new_otp"),
    path("success_collect",views.success_collect,name="success_collect")
]