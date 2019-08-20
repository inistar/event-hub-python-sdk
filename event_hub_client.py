import json
import requests

class EventHubClient():

    def __init__(self):
        self.conn_url = "http://localhost"
        self.port = 8083
        self.headers = {'content-type': 'application/x-www-form-urlencoded'}

    def publish_event(self, event_type, event_metadata):

        json_data = self.convertToJson(event_type, event_metadata)

        publish_url = self.conn_url + ':' + str(self.port) + '/publish'
        
        data = {}
        data['jsonData'] = json_data

        print(requests.post(publish_url, data=data, headers=self.headers))

    def convertToJson(self, event_type, event_metadata):
        json_dict = {'name': event_type}
        
        for key in event_metadata.keys():
            json_dict[key] = event_metadata[key]    

        json_obj = json.dumps(json_dict)
        
        return str(json_obj)

