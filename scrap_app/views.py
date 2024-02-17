from django.shortcuts import render
import requests
import json
from django.http import HttpResponse
from . models import Proxy_data
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from project.settings import EMAIL_HOST_USER
import subprocess


def return_499_if_chrome(request):
 
     user_agent = request.META['HTTP_USER_AGENT']
     if 'Chrome' in user_agent:
         return HttpResponse(status=499)




def get_data(request):
    url = "https://proxylist.geonode.com/api/proxy-list?limit=100&page=1&sort_by=lastChecked&sort_type=desc"
    payload = ""
    headers = {}
    response = requests.request("GET",url,data=payload,headers=headers)
    new_data=response.json()
    dump_data= json.dumps(new_data)
    data=json.loads(dump_data)
    print(data["data"])
    for k in data["data"]:
        i = Proxy_data.objects.create(ip=k['ip'],port=k['port'],protocol=k['protocols'],country=k['country'],uptime=k['upTime'])
        print(k['ip'])  
        subject = 'new data stored'
        message = 'hey here is new data'
        #send_mail(subject,message=message,EMAIL_HOST_USER=EMAIL_HOST_USER,recipient_list='',fail_silently='')
        i.save()
    json_data =(response.text)
    
    # response1=dict(json_data)
    # print(json_data['data'])
    return render(request,'scrap_app/main.html',{'context':json_data})