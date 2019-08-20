from event_hub_client import EventHubClient

if __name__ == '__main__':
    json_data = """{
                    "name": "Website Visited",
                    "orgId": "dzFyTqq4dT7YIai8mogz",
                    "userId": "ABCDEFGHIJKLM",
                    "sourceId": "ABCDEF",
                    "timestamp": "2019-07-09T14:54:44.760Z"
                }"""

    e = EventHubClient()
    e.publish_event(json_data)