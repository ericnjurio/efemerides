
from rest_framework import serializers

from .models import Commemoration


class CommemorationSerializer(serializers.Serializer):

    day = serializers.DateField(write_only=True)
    hoy = serializers.SerializerMethodField()
    mes = serializers.SerializerMethodField()

    @classmethod
    def __commemorations_to_str(cls, commemorations):
        return '\n\n'.join(
            f'On {str(c.date)}; {c.event}' for c in commemorations
        )

    def get_hoy(self, obj):
        return self.__commemorations_to_str(
            Commemoration.objects.on_date(obj.get('day'))
        )

    def get_mes(self, obj):
        commemorations = Commemoration.objects.of_month_on_date(obj.get('day'))
        days = sorted(set(c.date.day for c in commemorations))
        return {
            d: self.__commemorations_to_str(
                c for c in commemorations if c.date.day == d
            ) for d in days
        }
