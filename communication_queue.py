import queue
from event import Event

class CommunicationQueue:
    def __init__(self):
        self.queue = queue.Queue()

    def send_event(self, event: Event):
        self.queue.put(event)

    def receive_event(self):
        if not self.queue.empty():
            return self.queue.get()
        return None
