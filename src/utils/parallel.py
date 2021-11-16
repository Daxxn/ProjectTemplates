from threading import Thread
from typing import Iterable


class Parallel:
    def __init__(self) -> None:
        self.threads: list[Thread] = []

    def start(self, func: function, args: Iterable):
        thread = Thread(target=func, args=args)
        self.threads.append(thread)
        thread.start()
