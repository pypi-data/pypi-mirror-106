import os
import typing
from functools import reduce
from operator import truediv

from scapy import all as scapy


def replace_with_environment_var(value: typing.Union[int, str]) -> typing.Union[int, str]:
    if isinstance(value, str) and value.startswith('${') and value.endswith('}'):
        value = value[len('${'):-len('}')]
        value = os.getenv(value, '')
        
    return value


def resolve_environment_vars(packet_json: dict) -> dict:
    for key, value in packet_json.items():
        if key == 'payload':
            continue
        packet_json[key] = replace_with_environment_var(value)
        
    return packet_json


def parse_packet_json(packet_json: dict) -> scapy.Packet:
    packets = []
    while packet_type := next(iter(packet_json), None):
        packet = packet_json.get(packet_type, {})
        packet = resolve_environment_vars(packet)
        payload = packet.pop('payload', {})
        scapy_packet = getattr(scapy, packet_type, None)
        if scapy_packet:
            packets.append(scapy_packet(**packet))
        packet_json = payload
        
    return reduce(truediv, packets)


def to_packet_json(packet: scapy.Packet) -> dict:
    packet_jsons = []
    while not isinstance(packet, scapy.packet.NoPayload):
        packet_type = type(packet).__name__
        packet_fields = {
            key: value if isinstance(value, int) else str(value)
            for key, value in packet.fields.items()
            if key != 'options'
        }
        packet_jsons.append({ packet_type: packet_fields })
        packet = packet.payload
        
    for i in range(len(packet_jsons) - 1):
        if not packet_jsons[i]:
            continue
        packet_type, packet_fields = list(packet_jsons[i].items())[0]
        packet_fields['payload'] = packet_jsons[i + 1]
        
    return packet_jsons[0]
