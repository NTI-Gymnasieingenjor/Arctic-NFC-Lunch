from time import time
from typing import List
import datetime
import json

from modal import Modal


class CheckTime:
    def __init__(self, modal: Modal):
        self.modal = modal
        self.time = datetime.datetime.now().time()

        scheduleFile = open("./data/schedule.json")
        self.schedule = json.load(scheduleFile)
        scheduleFile.close()

        self.weekday = datetime.datetime.now().weekday()

    def check(self):
        if self.weekday > 4:
            return [False, "", ""]
        startTime = self.schedule[self.modal.cls][self.weekday][0]
        endTime = self.schedule[self.modal.cls][self.weekday][1]
        lunchTime: List[str] = startTime.split(":")
        lunchTimeEnd: List[str] = endTime.split(":")

        if self.time.hour >= int(lunchTime[0]) and self.time.minute >= int(lunchTime[1]):
            if self.time.hour <= int(lunchTimeEnd[0]) and self.time.minute <= int(lunchTimeEnd[1]):
                return [True, startTime, endTime]
        return [False, startTime, endTime]
