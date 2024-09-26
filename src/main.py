import logging

from time import sleep
from tb_gateway_mqtt import TBGatewayMqttClient
from paho.mqtt.client import MQTTMessageInfo


def gateway_attribute_update_callback(*args, **kwargs):
    print(f"gateway_attribute_update_callback {args} - {kwargs}")


def device_attribute_update_callback(*args, **kwargs):
    print(f"device_attribute_update_callback {args} - {kwargs}")


if __name__ == '__main__':
    logging.basicConfig(format='[%(asctime)s] [%(levelname)8s] [%(filename)-20s %(lineno)4d]: %(message)s', level=logging.DEBUG)
    logging.info("SW0172 started...")

    client = TBGatewayMqttClient(host="thingsboard.cloud", 
                                     username="hq3v8fa6av1fsio5snn5")
    client.connect()

    while not client.is_connected():
        print("Waiting to connect")
        sleep(1)

    client.subscribe_to_all_attributes(gateway_attribute_update_callback)

    result: MQTTMessageInfo = client.gw_connect_device(device_name="debug_sub-1", device_type="debug_subscription_device")
    client.gw_subscribe_to_all_device_attributes(device="debug_sub-1", callback=device_attribute_update_callback)

    print("Start")
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        pass
    print("Stop")

    result: MQTTMessageInfo = client.gw_disconnect_device(device_name="debug_sub-1")
    print(f"gw_disconnect_device result {result}")

    client.disconnect()
    