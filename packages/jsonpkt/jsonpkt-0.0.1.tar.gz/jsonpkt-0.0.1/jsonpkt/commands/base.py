from typing import List


class BaseCommand(object):
    def process(self, args: List[str]):
        raise NotImplementedError()
