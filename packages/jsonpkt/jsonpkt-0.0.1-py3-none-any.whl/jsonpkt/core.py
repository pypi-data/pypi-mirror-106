import argparse
import sys
from typing import List

from jsonpkt.commands import SendCommand, SendRecvCommand, ViewCommand


argparser = argparse.ArgumentParser()
subparsers = argparser.add_subparsers()

subparser_send = subparsers.add_parser('send', help='Generate and send packet by JSON file. See "jsonpkt send -h"')
subparser_send.add_argument('file', help='Packet definition file. (JSON)')
subparser_send.add_argument('-l', '--layer', required=False, default=3, type=int, help='Packet layer.')
subparser_send.set_defaults(handler=lambda args: SendCommand().process(args))

subparser_sendrecv = subparsers.add_parser('sendrecv', help='Generate, send and receive packet by JSON file. See "jsonpkt sendrecv -h"')
subparser_sendrecv.add_argument('file', help='Packet definition file. (JSON)')
subparser_sendrecv.add_argument('-l', '--layer', required=False, default=3, type=int, help='Packet layer.')
subparser_sendrecv.set_defaults(handler=lambda args: SendRecvCommand().process(args))

subparser_view = subparsers.add_parser('view', help='View packet prettierly. See "jsonpkt view -h"')
subparser_view.add_argument('file', help='Packet definition file. (JSON)')
subparser_view.add_argument('-f', '--format', required=False, default='scapy', help='Output format.')
subparser_view.add_argument('-i', '--indent', required=False, default=2, type=int, help='Indent width. (using format "json")')
subparser_view.set_defaults(handler=lambda args: ViewCommand().process(args))


def main(args: List[str] = sys.argv):
    _, *args = args
    parsed_args = argparser.parse_args(args=args)
    parsed_args.handler(parsed_args)
    
