from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []

    for visit in visits:
        visit_details = {
            "entered_at": visit.entered_at,
            "duration": visit.format_duration(visit.get_duration()),
            "is_strange": visit.is_visit_long(60),
        }
        this_passcard_visits.append(visit_details)

    context = {"passcard": passcard, "this_passcard_visits": this_passcard_visits}
    return render(request, "passcard_info.html", context)
