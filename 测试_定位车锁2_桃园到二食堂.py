#  MIT License
#
#  Copyright (c) 2021 苗锦洲
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

#  MIT License
#
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#
#  MIT License
#
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#
import json
import time

from paho.mqtt import client as mqtt_client

BROKER = 'ordinaryroad.xyz'
PORT = 1883

TOPIC_POST_TELEMETRY = "v1/devices/me/telemetry"


def connect_mqtt(clientId, username):
    client = mqtt_client.Client(clientId)
    client.username_pw_set(username)
    client.connect(BROKER, PORT)
    return client


def publishLatLons(client: mqtt_client, topic, latLons):
    for latLon in latLons:
        p = {
            'lat': str(latLon[0]),
            'lon': str(latLon[1])
        }
        telemetry = {'p': p}
        telemetryJsonString = json.dumps(telemetry)
        result = client.publish(topic, telemetryJsonString)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{telemetryJsonString}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        print("press any key to continue...")
        input()


if __name__ == '__main__':
    # device2ClientId = '601bbbe0-ad97-11ec-9254-155c4a931f85'
    # device2Username = 'UwP5SrQIY9hwW01zY7RT'
    # device1ClientId = '5a49b690-ad97-11ec-9254-155c4a931f85'
    # device1Username = 'C2yLwtIgW5NakKFYNrmS'
    # device4ClientId = '74dcff30-ad97-11ec-9254-155c4a931f85'
    # device4Username = 'pXagLMuHCPREd55qhkqm'
    device5ClientId = '79ef8510-ad97-11ec-9254-155c4a931f85'
    device5Username = 'ttq0BjtKIzXpBmMv7vIi'
    latLons = [
        [31.489352, 120.26757], [31.489333, 120.267286], [31.489338, 120.267114], [31.489342, 120.266964],
        [31.489342, 120.266808], [31.489333, 120.266685], [31.489322, 120.266574], [31.489322, 120.266354],
        [31.489299, 120.266306], [31.489345, 120.266075], [31.489432, 120.265941], [31.489569, 120.265882]
    ]
    client = connect_mqtt(device5ClientId, device5Username)
    publishLatLons(client, TOPIC_POST_TELEMETRY, latLons)
    while True:
        print("waiting for input...")
        inputString = input()
        print(inputString)
        time.sleep(3)
