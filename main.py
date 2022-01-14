import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == "__main__":
    test_passcard = Passcard.objects.all()[0]
    test_passcard_info = {
        "owner_name": test_passcard.owner_name,
        "passcode": test_passcard.passcode,
        "created_at": test_passcard.created_at,
        "is_active": test_passcard.is_active,
    }

    print(test_passcard_info)
