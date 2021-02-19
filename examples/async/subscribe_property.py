import time
from openstuder import SIAsyncGatewayClient, SIProtocolError, SIStatus


def on_error(error: SIProtocolError):
    print(f'Unable to connect: {error.reason()}')


def on_connected(access_level: str, gateway_version: str):
    client.subscribe_to_property('demo.sol.11004')


def on_property_subscribed(status: SIStatus, id_: str):
    print(f'Subscribed to {id_}, status = {status}')


def on_property_updated(id_: str, value: any):
    print(f'Property {id_} updated, value = {value}')


def on_property_unsubscribed(status: SIStatus, id_: str):
    print(f'Unsubscribed from {id_}, status = {status}')


client = SIAsyncGatewayClient()
client.on_error = on_error
client.on_connected = on_connected
client.on_property_subscribed = on_property_subscribed
client.on_property_updated = on_property_updated
client.on_property_unsubscribed = on_property_unsubscribed
client.connect('localhost')
time.sleep(10)
client.unsubscribe_from_property('demo.sol.11004')
time.sleep(2)
