import struct


class ICMP:
    _type_dic = {0: 'reply', 3: 'Destination unreachable', 8: 'request'}
    _code_dic = {0: 'reply', 1: 'Destination host unreachable'}

    def __init__(self, packet):
        self.type, self.code, self.checksum = struct.unpack(
            '! B B H 4x', packet[:8])
        self.type = (self.type, self._type_dic[self.type])
        self.code = (self.code, self._code_dic[self.code])

    def __str__(self):
        return 'type:' + str(self.type) + ' code:' + str(self.code)
