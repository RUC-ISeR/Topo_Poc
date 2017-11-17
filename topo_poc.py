from scapy.all import *
import threading


def thread1():
    print "start thread1"
    while True:
        receive = sniff(iface="h3-eth0",count=1)
        pkt = receive[0]
        if pkt[Ether].type == 0x88cc:
            print "forward lldp: eth0 -> eth1"
        else:
            print receive
        sendp(pkt, iface="h3-eth1")


def thread2():
    print "start thread2"
    while True:
        receive = sniff(iface="h3-eth1",count=1)
        pkt = receive[0]
        if pkt[Ether].type == 0x88cc:
            print "forward lldp: eth1 -> eth0"
        else:
            print receive
        sendp(pkt, iface="h3-eth0")


t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)
t1.start()
t2.start()

