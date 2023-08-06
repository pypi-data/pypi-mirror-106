import json

from jsonpkt.commands import BaseCommand
from jsonpkt.utils import parse_packet_json, to_packet_json


class ViewCommand(BaseCommand):
    def process(self, file: str, format: str = 'json', indent: int = 2):
        with open(file) as fp:
            packet_json = json.load(fp)
            packet = parse_packet_json(packet_json)
            if format == 'json':
                print(json.dumps(to_packet_json(packet), indent=indent))
            else:
                packet.show()
