from event import ApplicationSentEvent
from communication_queue import CommunicationQueue

class Student:
    def __init__(self, name):
        self.name = name

    def apply_to_university(self, university, communication_queue: CommunicationQueue):
        print(f"{self.name} is applying to {university.name}.")
        event = ApplicationSentEvent(self.name, university.name)
        communication_queue.send_event(event)
