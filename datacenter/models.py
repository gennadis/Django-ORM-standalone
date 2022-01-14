from datetime import timedelta
from django.db import models
from django.utils import timezone


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f"{self.owner_name} (inactive)"


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved="leaved at " + str(self.leaved_at)
            if self.leaved_at
            else "not leaved",
        )

    def get_duration(self) -> timedelta:
        if self.leaved_at:
            return self.leaved_at - self.entered_at
        return timezone.now() - self.entered_at

    def format_duration(duration):
        hour, min, sec = str(duration).split(":")
        return f"{hour} ч. {min} мин."
