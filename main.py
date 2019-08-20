from event_hub_hook import EventHub

def publish_event():
    conn_url = "http://localhost"
    port = 8083
    data = {}
    json_data = """{
                    "name": "Website Visited",
                    "orgId": "dzFyTqq4dT7YIai8mogz",
                    "userId": "ABCDEFGHIJKLM",
                    "sourceId": "ABCDEF",
                    "timestamp": "2019-07-09T14:54:44.760Z"
                }"""

    data['jsonData'] = json_data
    e = EventHub(conn_url, port)
    e.publish_event(data)

if __name__ == '__main__':
    publish_event()