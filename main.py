import socket
from termcolor import colored
from ICMP import ICMP
from TCP import TCP
from Ipv4 import Ipv4
from MacHeader import MacHeader

if __name__ == '__main__':
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    while True:
        raw_ethernet, _ = s.recvfrom(65565)
        mac_header = MacHeader(raw_ethernet)
        if mac_header.type == 8:
            ipv4 = Ipv4(mac_header.data)
            # ICMP green
            if ipv4.protocol == 1:
                icmp = ICMP(ipv4.data)
                print(colored("ICMP", "green"), icmp)
            # TCP blue
            elif ipv4.protocol == 6:
                tcp = TCP(ipv4.data)
                print(colored("TCP:", "blue"), tcp)
            # HTTP
