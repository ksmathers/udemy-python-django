from django.test import SimpleTestCase as TestCase

from app.iso_datetime import IsoDateTime


class TestIsoDateTime(TestCase):
    def test_to_local(self):
        tz = "America/Los_Angeles"
        dtz = IsoDateTime("2023-03-11T12:00:00Z")
        self.assertEqual(dtz.localize(tz), "2023-03-11T04:00:00PST")

        dtz = IsoDateTime("2023-03-12T12:00:00Z")
        self.assertEqual(dtz.localize(tz), "2023-03-12T05:00:00PDT")

        dtz = IsoDateTime("2007-03-10T12:00:00Z")
        self.assertEqual(dtz.localize(tz), "2007-03-10T04:00:00PST")

        dtz = IsoDateTime("2007-03-11T12:00:00Z")
        self.assertEqual(dtz.localize(tz), "2007-03-11T05:00:00PDT")

        dtz = IsoDateTime("2006-04-01T12:00:00Z")
        self.assertEqual(dtz.localize(tz), "2006-04-01T04:00:00PST")

        dtz = IsoDateTime("2006-04-02T12:00:00Z")
        self.assertEqual(dtz.localize(tz), "2006-04-02T05:00:00PDT")

        dtz = IsoDateTime("1944-01-01T12:00:00Z")
        self.assertEqual(dtz.localize(tz), "1944-01-01T05:00:00PWT")

        dtz = IsoDateTime("1920-06-30T12:00:00Z")
        self.assertEqual(dtz.localize(tz), "1920-06-30T04:00:00PST")

        dtz = IsoDateTime("1941-06-30T12:00:00Z")
        self.assertEqual(dtz.localize(tz), "1941-06-30T04:00:00PST")

        dtz = IsoDateTime("1965-06-30T12:00:00Z")
        self.assertEqual(dtz.localize(tz), "1965-06-30T05:00:00PDT")
