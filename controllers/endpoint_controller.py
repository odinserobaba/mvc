from models.endpoint_model import EndpointCaller


class EndpointController:
    def __init__(self, endpoints):
        self.caller = EndpointCaller(endpoints)

    def call_endpoints(self):
        self.caller.call_endpoints()
