import struct


class TCP:
    def __init__(self, packet):
        (self.source_port, self.destination_port,
         self.sequence_number, _, dataoff, _) = struct.unpack('! H H I I H H',
                                                              packet[:16])
        self.data_offset = dataoff >> 12

    def __str__(self):
        return ('source port:' + str(self.source_port)
                + ' destination port:' + str(self.destination_port)
                + ' data offset:' + str(self.data_offset))
