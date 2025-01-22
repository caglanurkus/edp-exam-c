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

