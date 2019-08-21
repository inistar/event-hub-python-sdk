import json
import requests

class EventHubClient():

    def __init__(self):
        self.conn_url = "http://localhost"
        self.port = 8083
        self.headers = {'content-type': 'application/json'}

    def publish_event(self, event_type, event_metadata):
        """
        Publish event to /publish endpoint. 

        :param event_type: Name of the event.
        :type event_type: str
        :param event_metadata: Event metadata.
        :type event_metadata: dict
        """
        json_data = self.convertToJson(event_type, event_metadata)
        
        publish_url = self.conn_url + ':' + str(self.port) + '/publish'

        print(requests.post(publish_url, data=json_data, headers=self.headers))

    def publish_event_batch(self, events):
        
        if type(events) == list:
            json_data = self.convertToJsonBatch(events)

        elif type(events) == str:
            data = []
            with open(events) as fp:
                for line in fp:

                    event = line.split(";")
                    event[0] = event[0].replace("'", "").replace("\"", "")
                    event[1] = json.loads(event[1].replace("'", "\""))

                    data.append((event[0], event[1]))
                
            json_data = self.convertToJsonBatch(data)
        else:
            print("Unknown parameters passed")
        
        publish_url = self.conn_url + ':' + str(self.port) + '/publishBatch'

        print(requests.post(publish_url, data=json_data, headers=self.headers))
        
    def convertToJson(self, event_type, event_metadata):
        """
        Format event data to JSON format.

        :param event_type: Name of the event.
        :type event_type: str
        :param event_metadata: Event metadata.
        :type event_metadata: dict
        """
        json_dict = {'name': event_type}
        
        for key in event_metadata.keys():
            json_dict[key] = event_metadata[key]    

        json_obj = json.dumps(json_dict)
        
        return str(json_obj)
    
    def convertToJsonBatch(self, events):
        results = []

        for event in events:
            json_data = self.convertToJson(event[0], event[1])
            results.append(json_data)
        
        results = str(results).replace("'", "")

        return results