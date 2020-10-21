import sys
import json
import os
from termios import tcflush, TCIOFLUSH
from time import sleep

from checkTime import CheckTime
from modal import Modal


sleepTime = 1
errorSleepTime = 2


class CheckTag:
    def __init__(self):
        file = open("./data/tags.json")
        # Creates a dictionary that contains all the tags and the connected class,
        # to be able to search for specific tags
        self.file: dict = json.load(file)
        file.close()

    def getTag(self, tag: str):
        if tag not in self.file.keys():
            # Clears the terminal output
            os.system("clear")
            print("Ogiltig tagg!")
            print("Se till att skanna taggen separat från plånbok, mobilskal osv.")
            return Modal("", "")
        return Modal(tag=tag, cls=self.file[tag])

    def timeCheck(self, modal: Modal):
        os.system("clear")
        if CheckTime(modal).check()[0] == False:
            print("DU HAR INTE TID NU!")
            print("DIN TID ÄR", CheckTime(modal).check()[1])
            sleep(errorSleepTime)
        if CheckTime(modal).check()[0] == True:
            print("Välkommen in!")
            sleep(sleepTime)

    def start(self, runs=0):
        loop = False
        index: int = 0
        while loop == False:
            if runs <= 0:
                os.system("clear")
                # Clears the previous input buffer
                sys.stdout.flush()
                tcflush(sys.stdin, TCIOFLUSH)

            if runs > 0 and index == runs - 1:
                # Ends the loop if the index has reached its limit
                loop = True
            index += 1

            print("Ready")
            value = input("")
            # The length of the NFC tags MFR number is 9
            if len(value) == 0 or len(value) > 9 or len(value) < 9:
                print("Var snäll skanna en korrekt tagg.")
                print("")
                sleep(errorSleepTime)
                continue

            print("Please Wait...")
            modal = self.getTag(value)

            if modal.tag == "" or modal.cls == "":
                # When the swiped tag isn't valid, continue the loop from the beginning
                sleep(errorSleepTime)
                continue

            print(modal.tag, modal.cls)
            self.timeCheck(modal)
            sleep(sleepTime)
