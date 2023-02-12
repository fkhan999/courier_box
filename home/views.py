from django.shortcuts import render, HttpResponse
import math,random
from home.models import boxes,courierRecieved
from home.mqtt import client as mqttclient
from django.contrib.auth.decorators import login_required
import requests
from courierbox.settings import FAST_SMS_API_KEY,FAST_SMS_URL
from django.shortcuts import redirect
# Create your views here.

def sms_sender(otp,mob_num):
    response=requests.get(FAST_SMS_URL+FAST_SMS_API_KEY+"&route=v3&sender_id=FTWSMS&message="+otp+" to collect courier from courier box"+"&language=english&flash=0&numbers="+str(mob_num))
    print(response.text)

def openbox(box):
    mqttclient.publish("LOCK"+str(box), payload="1", qos=1)

def closebox(box):
    mqttclient.publish("LOCK"+str(box), payload="0", qos=1)

def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP+=digits[math.floor(random.random() * 10)]
    return OTP


@login_required(login_url='/accounts/login/')
def index(request):
    box=request.GET.get("close_box")
    if box is not None:
        closebox(box)
    return render(request,"index.html")

@login_required(login_url='/accounts/login/')
def mobile(request):
    return render(request,"mobile.html")

@login_required(login_url='/accounts/login/')
def mob(request):
    mob_num=request.GET['mob_num']
    return render(request,"mob.html",{"mobile":mob_num})

@login_required(login_url='/accounts/login/')
def new(request):
    try:
        empty_box=boxes.objects.filter(status=0).first().id
    except:
        return render(request,"no_empty.html")
    return render(request,"mobile_cus.html",{"box":empty_box})

@login_required(login_url='/accounts/login/')
def new1(request):
    box=request.GET['box']
    mob_num=request.GET['mob_num']
    if mob_num==False or len(mob_num)!=10 or mob_num[0] not in {"6","7","8","9"}:
        return redirect('/new')
    openbox(box)
    return render(request,"verify.html",{"mobile":mob_num,"box":box})

@login_required(login_url='/accounts/login/')
def new_otp(request):
    box=request.GET['box']
    mob_num=request.GET['mob_num']
    otp=generateOTP()
    sms_sender(otp,mob_num)
    courierRecieved.objects.create(mobile_number=mob_num,box=box,otp=otp).save()
    edit_box=boxes.objects.get(id=box)
    edit_box.status=1
    edit_box.save()
    return render(request,"sucess_collect.html",{"msg":"COURIER WAS SUBMITTED SUCCESSFULLY"})

@login_required(login_url='/accounts/login/')
def mob1(request):
    try:
        mob_num,otp=request.GET['mob_num'],request.GET['otp']
        box=courierRecieved.objects.get(mobile_number=mob_num,otp=otp)
        concerned_box=box.box
        openbox(concerned_box)
        #box.delete()
    except:
        return render(request,"error.html")

    return render(request,"collect.html",{"box":concerned_box,"mob_num":mob_num})

    
@login_required(login_url='/accounts/login/')
def success_collect(request):
    mob_num,box=request.GET['mob_num'],request.GET['box']
    courierRecieved.objects.get(mobile_number=mob_num,box=box).delete()
    instance=boxes.objects.get(id=box)
    instance.status=0
    instance.save()
    closebox(box)
    return render(request,"sucess_collect.html")
