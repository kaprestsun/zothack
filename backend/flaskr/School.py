class Event:
    def __init__(self, event_id, name, location, school_class, professor, major, time, date):
        self.event_id = event_id
        self.name = name
        self.school_class = school_class
        self.location = location
        self.professor = professor
        self.major = major
        self.time = time
        self.date = date
        self.attendees = 0 

    def add_attendee(self):
        self.attendees += 1

    def event_list(self):
         return [self.event_id, self.name, self.location, self.school_class, self.professor, self.major, self.time, self.date]
