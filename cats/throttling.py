import datetime

from rest_framework import throttling


class WorkingHoursRateThrotlle(throttling.BaseThrottle):

    def allow_request(self, request, view):
        now = datetime.datetime.now().hour
        return 3 <= now <= 5
