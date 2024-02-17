from django.shortcuts import render
import requests
import json
from celery import shared_task
from . models import Proxy_data




@shared_task
def get_data():
    url = "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc"
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
        i.save()
    json_data =(response.text)
    
    # response1=dict(json_data)
    # print(json_data['data'])
    # return render(request,'scrap_app/main.html',{'context':json_data})