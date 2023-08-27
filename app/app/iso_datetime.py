from dateutil import parser
import pytz


class IsoDateTime:
    def __init__(self, isodate_str: str):
        dt = parser.parse(isodate_str)
        self.udt = dt.astimezone(tz=pytz.utc)

    def localize(self, tzname: str):
        local = pytz.timezone(tzname)
        dt = self.udt.astimezone(local)
        return dt.strftime("%Y-%m-%dT%H:%M:%S%Z")
