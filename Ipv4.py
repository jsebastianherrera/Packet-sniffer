import struct


class Ipv4:
    def __init__(self, data):
        ################
        #  1-4 octect  #
        ################
        version_ihl = data[0]  # 8 bits -> 4 version and 4 IHL
        # bitwise right shift moving 4 bites to the right
        self.version = version_ihl >> 4
        # 15 maximum value in 4 bits representation  1111
        # getting last 4 bits
        self.header_length = (version_ihl & 15) * 4
        self.total_length = struct.unpack('! H', data[2:4])[0]
        ################
        #  4-8 octect  #
        ################
        self.identification, flag_fragment_off = struct.unpack(
            '! H H', data[4:8])
        self.flag = flag_fragment_off >> 13
        # 2^13 -1 = 8191
        self.fragment_offset = (flag_fragment_off & 8191)
        ################
        #  8-20 octect #
        ################
        (self.ttl, self.protocol,
         self.checksum, source_ip, dest_ip) = struct.unpack(
            '! B B 2s 4s 4s', data[8:20])
        self.source_ip = self._ipv4_ip(source_ip)
        self.dest_ip = self._ipv4_ip(dest_ip)
        self.data = data[self.header_length:]

    def _ipv4_ip(self, addr):
        return '.'.join(map(str, addr))
