#!/usr/bin/python3

import requests

def geo_ip():
    response_ip = requests.get('https://api.ipify.org/?format=json')
    res_ip = response_ip.json()
    ip = res_ip["ip"]
    print(f"Your ip is: {ip} ")
    return ip

def location():
    response_geo = requests.get('https://ipinfo.io/'+geo_ip()+'/geo')
    res_geo = response_geo.json()
    loc = res_geo["loc"]
    print(f"Your location is: {loc}")
    return loc
