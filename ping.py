#!/usr/bin/env python3
from scapy.all import *
import os
import random
import sys
import time

def send_custom_ping(destination_ip, character):
    identifier = os.getpid() & 0xFFFF
    sequence_number = 1
    timestamp = int(time.time())

    payload_data = character.encode() + os.urandom(2) + b'\x00\x00\x00\x00\x00'
    payload_data += bytes(range(0x10, 0x38))

    packet = IP(dst=destination_ip) / ICMP(type="echo-request", id=identifier, seq=sequence_number) / Raw(load=payload_data)

    send(packet)
    print(f"Sent custom ping for character '{character}'")

def main():
    if len(sys.argv) != 2:
        print("Usage: python custom_ping.py <string>")
        sys.exit(1)
    
    string_to_send = sys.argv[1]
    destination_ip = "8.8.8.8"  # Google's DNS server
    
    for character in string_to_send:
        send_custom_ping(destination_ip, character)
    
    print("All custom pings sent!")

if __name__ == "__main__":
    main()


