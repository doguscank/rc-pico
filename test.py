from led_utils import set_led_state
from network_utils import connect, open_socket
from web_server import serve

import machine

if __name__ == '__main__':
    try:
        ip = connect()
        print(f"Connected to IP: {ip}")
        connection = open_socket(ip)
        serve(connection, set_led_state)
    except KeyboardInterrupt:
        machine.reset()