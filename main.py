from ast import Pass
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == "__main__":
    all_passcards = Passcard.objects.all()
    active_passcards = [passcard for passcard in all_passcards if passcard.is_active]
    print(f"Всего пропусков {len(all_passcards)}")
    print(f"Активных пропусков {len(active_passcards)}")
