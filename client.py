import sys
import json
import http.client

class eggClient():
    def __init__(self, server_str):
        self.connection = http.client.HTTPSConnection(server_str)
    def post(self, json_data):
        headers = {'Content-type': 'application/json'}
        self.connection.request('POST', '?', json_data, headers)
        response = self.connection.getresponse()
        print("response: {}".format(response.read().decode()))
        
# new_val returns json format value for POST
def new_val(timestamp, location, crowd_num, crowd_favor) :
    values = {
        'time':timestamp,
        'location':location,
        'crowd_num': crowd_num,
        'crowd_favor': crowd_favor,
    }
    return  json.dumps(values)

if __name__ == '__main__':
    e = eggClient(sys.argv[1])
    val = new_val("2019-8-27", "Taipei", 300, 0)
    e.post(val)