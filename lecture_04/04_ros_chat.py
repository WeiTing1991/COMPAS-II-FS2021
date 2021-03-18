import json

from compas_fab.backends import RosClient
from roslibpy import Topic

from helpers import get_current_buffer
from helpers import get_input

print('Enter your name:')
name = get_input()

client = RosClient('ros-vzby-dzht.yaler.io', port=80)

def start_chat():
    print('Connected as {}! [type a message or q to quit]'.format(name))

    talker = Topic(client, '/messages', 'std_msgs/String')
    talker.advertise()

    listener = Topic(client, '/messages', 'std_msgs/String')
    listener.subscribe(receive_message)

    while client.is_connected:
        text = get_input()
        if text == 'q': break
        send_message(talker, text)

    client.terminate()

def receive_message(message):
    data = json.loads(message['data'])
    if data['name'] != name:
        print('\r[{}]: {}\r'.format(
            data['name'],
            data['text'].ljust(80),
        ))
        print('> {}'.format(get_current_buffer()), end='', flush=True)

def send_message(talker, message):
    talker.publish({'data': json.dumps(dict(text=message, name=name))})

client.on_ready(start_chat)
client.run_forever()
