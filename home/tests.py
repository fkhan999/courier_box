from django.test import TestCase

from home.models import boxes,courierRecieved


def reset_status():
    a=boxes.objects.filter()
    for x in a:
        x.status=0
        x.save()

def delete_all():
    b=courierRecieved.objects.filter()
    for x in b:
        x.delete()

def createbox(n):
    for x in range(1,n+1):
        try:
            boxes.objects.create(id=x,status=0)
        except:
            print("failed to create with id "+str(x))

def delete_all_boxes():
    b=boxes.objects.filter()
    for x in b:
        x.delete()


#createbox(10)
#delete_all_boxes()





# Create your tests here.
