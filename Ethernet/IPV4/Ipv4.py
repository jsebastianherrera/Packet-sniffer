import struct


class IPV4:
    def __init__(self, data):
        version_ihl = data[0]  # 8 bits -> 4 version and 4 IHL
        self.version = version_ihl >> 4
        self.header_length = (version_ihl & 15) * 4
        self.total_length = struct.unpack('! H', data[2:4])[0]
        self.identification, flag_fragment_off = struct.unpack(
            '! H H', data[4:8])
        self.flag = flag_fragment_off >> 13
        self.fragment_offset = (flag_fragment_off & 8191)
        (self.ttl, self.protocol,
         self.checksum, source_ip, dest_ip) = struct.unpack(
            '! B B 2s 4s 4s', data[8:20])
        self.source_ip = self._ipv4_ip(source_ip)
        self.dest_ip = self._ipv4_ip(dest_ip)
        self.data = data[self.header_length:]

    def _ipv4_ip(self, addr):
        return '.'.join(map(str, addr))

    def __str__(self):
        return (f'Internet Protocol Version 4\nSource: {self.source_ip} -> Destination: {self.dest_ip}\nHeader length: {self.header_length}\nTotal length: {self.total_length}\nProtocol: {self.protocol} ')
