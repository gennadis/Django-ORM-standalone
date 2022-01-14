from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []

    for visit in active_visits:
        visit_details = {
            "who_entered": visit.passcard.owner_name,
            "entered_at": visit.entered_at,
            "duration": visit.format_duration(visit.get_duration()),
        }
        non_closed_visits.append(visit_details)

    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, "storage_information.html", context)
