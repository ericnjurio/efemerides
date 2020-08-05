from django.db import models


class CommemorationManager(models.Manager):
    """Manager of commemorations."""

    def on_date(self, date):
        """Commemorations on a date."""
        return self.filter(
            date__day=date.day,
            date__month=date.month,
            date__year__lte=date.year
        ).order_by("date__year")

    def of_month_on_date(self, date):
        """Commemorations of the month on a date."""
        return self.filter(
            date__month=date.month,
            date__year__lte=date.year
        ).order_by("date__day", "date__year")
