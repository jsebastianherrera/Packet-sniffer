import socket
from Ethernet.Ethernet import Ethernet
from Ethernet.IPV4.Ipv4 import IPV4
from Ethernet.IPV4.Protocols.ICMP.ICMP import ICMP
from Ethernet.IPV4.Protocols.TCP.TCP import TCP
from Ethernet.IPV4.Protocols.TCP.Protocols.HTTP import HTTP
if __name__ == '__main__':
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    while True:
        raw_ethernet, _ = s.recvfrom(65565)
        eth = Ethernet(raw_ethernet)
        # IPV4
        if eth.type == '0x800':
            ipv4 = IPV4(eth.data)
            # ICMP
            if ipv4.protocol == 1:
                icmp = ICMP(ipv4.data)
                print(eth)
                print(ipv4)
                print(icmp)
            # TCP
            if ipv4.protocol == 6:
                tcp = TCP(ipv4.data)
                # HTTP
                if tcp.source_port == 80 or tcp.source_port == 23450:
                    print(eth)
                    print(ipv4)
                    print(tcp)
                    http = HTTP(ipv4.data[tcp.data_offset:])
                    print(http)
                    print('')
