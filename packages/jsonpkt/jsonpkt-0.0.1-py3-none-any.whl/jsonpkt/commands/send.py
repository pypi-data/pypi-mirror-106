import json

from scapy import all as scapy

from jsonpkt.commands import BaseCommand
from jsonpkt.utils import parse_packet_json


class SendCommand(BaseCommand):
    def process(self, args):
        file = args.file
        with open(file) as fp:
            packet_json = json.load(fp)
            packet = parse_packet_json(packet_json)
            sender = scapy.sendp if args.layer < 3 else scapy.send
            sender(packet, verbose=False)
        
