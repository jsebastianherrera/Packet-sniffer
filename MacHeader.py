import struct
import socket


class MacHeader:
    def __init__(self, raw_data):
        (self.destination_addr, self.source_addr,
         self.type, self.data) = self._MAC_header(raw_data)

    def __str__(self):
        return ('s_addr: ' + str(self.source_addr) +
                ' d_addr: ' + str(self.destination_addr) +
                ' type: ' + str(self.type))

    def _MAC_header(self, data):
        dest_addr, source_addr, protocol = struct.unpack(
            '! 6s 6s H', data[:14])
        return self._get_mac_addr(dest_addr), self._get_mac_addr(
            source_addr), socket.htons(protocol), data[14:]

    def _get_mac_addr(self, mac):
        return ':'.join(map('{0:2x}'.format, mac)).upper()
