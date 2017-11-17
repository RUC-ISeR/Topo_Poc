from scapy.all import *
import time

fake_src = "00:00:00:00:00:02"

def get_random_mac():
    mac = [0x52, 0x54, 0x00,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, mac))


while True:
    rd_dst = get_random_mac()
    pkt = Ether(src=fake_src, dst=rd_dst) / IP(src="10.0.0.9", dst="10.0.0.10") / ICMP()
    sendp(pkt)
    time.sleep(1)

