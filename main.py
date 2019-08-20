from event_hub_client import EventHubClient

if __name__ == '__main__':

    event_type = "Website Visited"
    event_metadata = {
                        "orgId": "dzFyTqq4dT7YIai8mogz",
                        "userId": "ABCDEFGHIJKLM",
                        "sourceId": "ABCDEF",
                        "timestamp": "2019-07-09T14:54:44.760Z"
                    }
    e = EventHubClient()
    e.publish_event(event_type, event_metadata)
    # e.convertToJson(event_type, event_metadata)