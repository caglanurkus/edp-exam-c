import queue
from typing import Any

class Event:
    def __init__(self, payload: Any):
        self.payload = payload

class ApplicationSentEvent(Event):
    def __init__(self, student_name, university_name):
        super().__init__({"student": student_name, "university": university_name})

class ApplicationAcceptedEvent(Event):
    def __init__(self, student_name, university_name):
        super().__init__({"student": student_name, "university": university_name})

class ApplicationRejectedEvent(Event):
    def __init__(self, student_name, university_name):
        super().__init__({"student": student_name, "university": university_name})
class CommunicationQueue:
    def __init__(self):
        self.queue = queue.Queue()

    def send_event(self, event: Event):
        self.queue.put(event)

    def receive_event(self):
        if not self.queue.empty():
            return self.queue.get()
        return None
class Student:
    def __init__(self, name):
        self.name = name

    def apply_to_university(self, university, communication_queue):
        print(f"{self.name} is applying to {university.name}.")
        event = ApplicationSentEvent(self.name, university.name)
        communication_queue.send_event(event)
class University:
    def __init__(self, name):
        self.name = name

    def process_application(self, communication_queue):
        event = communication_queue.receive_event()
        if isinstance(event, ApplicationSentEvent):
            student_name = event.payload["student"]
            print(f"{self.name} received an application from {student_name}.")

            if student_name.lower().startswith("a"):  # Example rule
                response_event = ApplicationAcceptedEvent(student_name, self.name)
                print(f"{student_name}'s application has been accepted by {self.name}.")
            else:
                response_event = ApplicationRejectedEvent(student_name, self.name)
                print(f"{student_name}'s application has been rejected by {self.name}.")

            communication_queue.send_event(response_event)

if __name__ == "__main__":
    communication_queue = CommunicationQueue()
    student = Student("Alice")
    university = University("Tech University")

    student.apply_to_university(university, communication_queue)

    university.process_application(communication_queue)

    response_event = communication_queue.receive_event()
    if response_event:
        if isinstance(response_event, ApplicationAcceptedEvent):
            print(f"Event: {response_event.payload['student']} was accepted by {response_event.payload['university']}.")
        elif isinstance(response_event, ApplicationRejectedEvent):
            print(f"Event: {response_event.payload['student']} was rejected by {response_event.payload['university']}.")
