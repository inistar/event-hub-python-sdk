from event_hub_client import EventHubClient

if __name__ == '__main__':

    event_type = "Website Visited"
    event_metadata = {
                        "orgId": "dzFyTqq4dT7YIai8mogz",
                        "userId": "ABCDEFGHIJKLM",
                        "sourceId": "ABCDEF",
                        "timestamp": "2019-07-09T14:54:44.760Z"
                    }
    
    events = []
    for i in range(5):
        events.append((event_type, event_metadata))

    e = EventHubClient()
    # e.publish_event(event_type, event_metadata)
    # e.publish_event_batch(events)
    e.publish_event_batch("sample_events_data.csv")