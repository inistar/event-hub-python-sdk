import requests

class EventHubClient():

    def __init__(self, conn_url=, port):
        self.conn_url = conn_url
        self.port = port
        self.headers = {'content-type': 'application/x-www-form-urlencoded'}

    def publish_event(self, json_data):
        publish_url = self.conn_url + ':' + str(self.port) + '/publish'
        print(requests.post(publish_url, data=json_data, headers=self.headers))
