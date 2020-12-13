#!/usr/bin/python3


#imports
import socket
import struct
import binascii
#platform module to check the system type
#import os
import platform

platform_ = str(platform.system()).lower()
#for packet interface, we'll use PF_PACKET for linux and
#AF_INET for window
if 'linux' or 'x' in platform_:
    s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
    #recvfrom to receive packets...using 2048(from tutorials(seems to be the best guess!))
    while True:
        packet = s.recvfrom(2048)
        #ripping ethernet header
        eth_header = packet[0][0:14]
        #unpacking the header with the struct method
        eth_header = struct.unpack("!6s6s2s", eth_header)
        print(f'DESTINATION MAC: {binascii.hexlify(eth_header[0])} Source MAC:{binascii.hexlify(eth_header[1])} TYPE: {binascii.hexlify(eth_header[2])}')
        ipheader = packet[0][14:34]
        ip_header = struct.unpack("!12s4s4s", ipheader)
        print(f'SOURCE UP:{socket.inet_ntoa(ip_header[1])} DESTINATION IP:{socket.inet_ntoa(ip_header[2])}')
elif 'windows' or 'win' in platform:
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.htons(0x0800))
    #recvfrom to receive packets...using 2048(from tutorials(seems to be the best guess!))
    while True:
        packet = s.recvfrom(2048)
        #ripping ethernet header
        eth_header = packet[0][0:14]
        #unpacking the header with the struct method
        eth_header = struct.unpack("!6s6s2s", eth_header)
        print(f'DESTINATION MAC: {binascii.hexlify(eth_header[0])} Source MAC:{binascii.hexlify(eth_header[1])} TYPE: {binascii.hexlify(eth_header[2])}')
        ipheader = packet[0][14:34]
        ip_header = struct.unpack("!12s4s4s", ipheader)
        print(f'SOURCE UP:{socket.inet_ntoa(ip_header[1])} DESTINATION IP:{socket.inet_ntoa(ip_header[2])}')
else:
    print('Unknown platform!Modify script!')
