#simple lightweight python port scanner!
#not meant for production scale!

from socket import *
import argparse
import sys

def scan(ip, port):
    print('---Port Scanner Started---')
    print('-.-'*100)
    print(f'Scanning ip: {ip} on port: {port}')
    print('-.-'*100)

    try:
        #AF_INET is used for IPv4 protocols and SOCK_STREAM is used for tcp
        s = socket(AF_INET, SOCK_STREAM)
        #set timeout
        s.settimeout(1)
        found_results = s.connect((ip, port))
        if found_results == 0:
            print(f'Open port: {port}')
        else:
            print(f'Closed port: {port} ')
        s.close()
    except gaierror:
        print('hostname could not be resolved')
        exit(1)
    except timeout:
        print('Connection timed out')
        exit(1)
    except error as e:
        print('Could not connect to server\nPort probably is wrong!')
        print('Another issue could be that there is no server up')
        print('Try the httpserver from github: https://github.com/malgulam/100ProjectsOfCode/blob/main/httpserver/httpserver.py\n\n')
        print(e)
        exit(1)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scan for open ports on network')
    argsparser = argparse.ArgumentParser(prog='pyscanner.py', usage=f'pyscanner.py [options] -ip "ip or hostname" -port "port to scan"')
    argsparser.add_argument('-ip', required=True, type=str, help='ip or hostname')
    argsparser.add_argument('-port', required=True, type=int, help='port to scan')
    argss = argsparser.parse_args()
    ip = str(argss.ip)
    port = int(argss.port)
    #run the scan function
    scan(ip, port)


