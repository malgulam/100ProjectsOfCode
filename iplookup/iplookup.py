#!/usr/bin/python3

#iplookup.py => script to lookup geolaction of a given ip or group of ips
#you need an https://ipstack.com/ account and API key to run this code

#imports

import argparse
import requests

#main
parser = argparse.ArgumentParser()
parser.add_argument("-a", '--auto',action='store_true',  help="This argument sets the iplocator to auto and will use"
                               "your current ip\nand retrieve information on it.")
parser.add_argument("-ip", '-ipaddr',help="This argument sets the ip you want to retrieve infromation  on.Eg.) python3 iplookup.py -ip xxx.xxx.xxx")
parser.add_argument("-m", '--multiple', nargs='+',  help="This argument enables you to pass multiple i[ps to the program"
                               "\n to retrieve information on.Eg.)python3 iplookup.py -m zzz.zzz.zzz, xxx.xxx.xxx, yyy.yyy.yyy")
args = parser.parse_args()

print(args)
# todo: commandline arguments => iplookup.py -a (auto! will use requester part of api)
if args.auto:
    try:
        url = 'http://api.ipstack.com/check?access_key=your_api_key&fields=ip,location,security&output=json'
        resp = requests.get(url)
        print(resp.content)
        exit(0)
    except Exception as e:
        print(e)

#todo: commandline arguments => iplookup.py -ip xxxx(where x is the ip)
if args.ip:
    ip = str(args.ip)
    try:
        url = f'http://api.ipstack.com/{ip}?access_key=your_api_key&fields=ip,location,security&output=json'
        resp = requests.get(url)
        print(resp.content)
        exit(0)
    except Exception as e:
        print(e)

#todo: commandline arguments => ipllokup.py -m xxx,xxxx,xxxx(where xxx are ip addresses)
if args.multiple:
    multiple = str(args.multiple)
    multiple_as_str = ''
    for ip in multiple:
        if multiple[-1] != ip:
            multiple_as_str += f'{ip},'
        else:
            multiple_as_str += f'{ip}'
    try:
        url = f'http://api.ipstack.com/{multiple_as_str}?access_key=your_api_key&fields=ip,location,security&output=json'
        resp = requests.get(url)
        print(resp.content)
        exit(0)
    except Exception as e:
        print(e)
