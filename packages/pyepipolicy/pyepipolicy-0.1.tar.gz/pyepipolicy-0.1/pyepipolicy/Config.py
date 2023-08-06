
class Config:
    def __init__(self, address, port=8042):
        self.connection_string = 'http://{}:{}/'.format(address, port)