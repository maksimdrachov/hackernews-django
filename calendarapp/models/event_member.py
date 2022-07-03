from django.db import models

#from accounts.models import User
from calendarapp.models import Event, EventAbstract


class EventMember(EventAbstract):
    """ Event member model """

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="events")
    #user = models.ForeignKey(
    #    User, on_delete=models.CASCADE, related_name="event_members"
    #)
    user = models.CharField(max_length=20, blank=False)

    class Meta:
        unique_together = ["event", "user"]

    def __str__(self):
        return str(self.user)
