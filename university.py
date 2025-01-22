from event import ApplicationSentEvent, ApplicationAcceptedEvent, ApplicationRejectedEvent
from communication_queue import CommunicationQueue

class University:
    def __init__(self, name):
        self.name = name

    def process_application(self, communication_queue: CommunicationQueue):
        event = communication_queue.receive_event()
        if isinstance(event, ApplicationSentEvent):
            student_name = event.payload["student"]
            print(f"{self.name} received an application from {student_name}.")

            # Example rule: Accept if name starts with "A", otherwise reject
            if student_name.lower().startswith("a"):
                response_event = ApplicationAcceptedEvent(student_name, self.name)
                print(f"{student_name}'s application has been accepted by {self.name}.")
            else:
                response_event = ApplicationRejectedEvent(student_name, self.name)
                print(f"{student_name}'s application has been rejected by {self.name}.")
            
            communication_queue.send_event(response_event)
