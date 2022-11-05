class HTTP:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f'{bytes.decode(self.data,errors="ignore")}'
