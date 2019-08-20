import requests

class EventHubClient():

    def __init__(self):
        self.conn_url = "http://localhost"
        self.port = 8083
        self.headers = {'content-type': 'application/x-www-form-urlencoded'}

    def publish_event(self, json_data):
        
        publish_url = self.conn_url + ':' + str(self.port) + '/publish'
        
        data = {}
        data['jsonData'] = json_data

        print(requests.post(publish_url, data=data, headers=self.headers))
