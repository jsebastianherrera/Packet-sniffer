import struct


class TCP:
    def __init__(self, packet):
        (self.source_port, self.destination_port,
         self.sequence_number) = struct.unpack('! H H I', packet[:8])
        self.data_offset = (struct.unpack('! B', packet[12:13])[0] >> 4)*4

    def __str__(self):
        return f'Transmission Control Protocol\nSource Port: {self.source_port}\nDestination Port: {self.destination_port}\nData offset: {self.data_offset}'
