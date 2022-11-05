import struct


class Ethernet:
    def __init__(self, raw_data):
        self.dest_mac, self.src_mac, self.type = struct.unpack(
            '! 6s 6s H', raw_data[:14])
        self.dest_mac = self._getmac(self.dest_mac)
        self.src_mac = self._getmac(self.src_mac)
        self.type = hex(self.type)
        self.data = raw_data[14:]

    def __str__(self):
        return (f'Ethernet frame: \nSource mac: {self.src_mac} -> Dest mac: {self.dest_mac}\nType: {self.type} ')

    def _getmac(self, mac):
        return ':'.join(map('{0:2x}'.format, mac)).upper()
