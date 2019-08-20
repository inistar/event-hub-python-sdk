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

    def publish_event_batch(self, events):
        
        if type(events) == list:
            for event in events:
                self.publish_event(event[0], event[1])
        elif type(events) == str:
            print("string")
        else:
            print("Unknown parameters passed")
        
    def convertToJson(self, event_type, event_metadata):
        json_dict = {'name': event_type}
        
        for key in event_metadata.keys():
            json_dict[key] = event_metadata[key]    

        json_obj = json.dumps(json_dict)
        
        return str(json_obj)
