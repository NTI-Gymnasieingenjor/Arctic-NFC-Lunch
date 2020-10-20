import unittest
import datetime
from unittest.mock import patch

from checkTime import CheckTime
from modal import Modal


class SomeTestCase(unittest.TestCase):
    def setUp(self):
        class fakedatetime(datetime.datetime):
            @classmethod
            def now(cls):
                return self.time
        # Replaces the original time class with our fakeDateTime class to be able to simulate a different date
        patcher = patch('datetime.datetime', fakedatetime)
        # Adds callback to when the unittest completes
        self.addCleanup(patcher.stop)
        patcher.start()

    def testTimes(self):
        # Lunch start time
        self.time = datetime.datetime(year=2020, month=10, day=20, hour=12, minute=0)
        assert CheckTime(modal=Modal("536956630", "Na20")).check()[0] == True

        # 1 min before lunch
        self.time = datetime.datetime(year=2020, month=10, day=20, hour=11, minute=59)
        assert CheckTime(modal=Modal("536956630", "Na20")).check()[0] == False

        # 19 min after lunch start time
        self.time = datetime.datetime(year=2020, month=10, day=20, hour=12, minute=19)
        assert CheckTime(modal=Modal("536956630", "Na20")).check()[0] == True

        # 20 min after lunch start time
        self.time = datetime.datetime(year=2020, month=10, day=20, hour=12, minute=20)
        assert CheckTime(modal=Modal("536956630", "Na20")).check()[0] == True

        # 1 min after lunch end time
        self.time = datetime.datetime(year=2020, month=10, day=20, hour=12, minute=21)
        assert CheckTime(modal=Modal("536956630", "Na20")).check()[0] == False

        # Midnight
        self.time = datetime.datetime(year=2020, month=10, day=20, hour=23, minute=59)
        assert CheckTime(modal=Modal("536956630", "Na20")).check()[0] == False

        # Morning
        self.time = datetime.datetime(year=2020, month=10, day=20, hour=10, minute=0)
        assert CheckTime(modal=Modal("536956630", "Na20")).check()[0] == False

        # Winter time
        self.time = datetime.datetime(year=2020, month=10, day=25, hour=3, minute=0)
        assert CheckTime(modal=Modal("536956630", "Na20")).check()[0] == False

        # Weekend
        self.time = datetime.datetime(year=2020, month=10, day=31, hour=12, minute=00)
        assert CheckTime(modal=Modal("536956630", "Na20")).check()[0] == False

        # Leap day
        self.time = datetime.datetime(year=2024, month=2, day=29, hour=11, minute=35)
        assert CheckTime(modal=Modal("536956630", "Na20")).check()[0] == True
