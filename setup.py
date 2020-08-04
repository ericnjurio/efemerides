"""Setup efemerides project."""

import os

from django import setup


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'efemerides_api.settings')
setup()

WIKIPEDIA_EFEMERIDES_AR_FILE = 'efemerides/wikipedia_efemerides_ar.psv'


def load_commemorations():
    """Load commemorations from wikipedia_efemerides_ar as model in the DB."""
    from efemerides.models import Commemoration

    if Commemoration.objects.count() < 15:
        with open(WIKIPEDIA_EFEMERIDES_AR_FILE) as file:
            Commemoration.objects.bulk_create(
                Commemoration(
                    **dict(zip(('date', 'event'), line.split('|')))
                )
                for line in file
                if 'date|event' not in line
            )
    print('Commemorations loaded.')


load_commemorations()
