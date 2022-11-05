import struct


class ICMP:
    def __init__(self, packet):
        self.type, self.code, self.checksum = struct.unpack(
            '! B B H', packet[:4])
        self.type = self.type
        self.code = self.code
        self.data = packet[4:]

    def __str__(self):
        return f'\t\tInternet Control Message Protocol \n\t\t\tType: {self.type} \n\t\t\tCode: {self.code}'
