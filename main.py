from communication_queue import CommunicationQueue
from student import Student
from university import University
from event import ApplicationAcceptedEvent, ApplicationRejectedEvent

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
 