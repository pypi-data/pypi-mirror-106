import json

from jsonpkt.commands import BaseCommand
from jsonpkt.utils import parse_packet_json, to_packet_json


class ViewCommand(BaseCommand):
    def process(self, args):
        file = args.file
        with open(file) as fp:
            packet_json = json.load(fp)
            packet = parse_packet_json(packet_json)
            if args.format == 'json':
                print(json.dumps(to_packet_json(packet), indent=args.indent))
            else:
                packet.show()
