from commons.rest_methods import RestMethods
from commons.headers import Headers

class BaseClient:
    def __init__(self):
        self.rest_requests = RestMethods()
        self.service = 'heroku_service'
        self.headers= Headers()
