import sys
import time
import json
import sys
import os
from termios import tcflush, TCIOFLUSH
from time import sleep


class Modal:
    def __init__(self, tag: str, cls: str):
        self.tag = tag
        self.cls = cls


class CheckTag:
    def __init__(self):
        file = open("tags.json")
        # Creates a dictionary that contains all the tags and the connected class,
        # to be able to search for specific tags
        self.file: dict = json.load(file)
        file.close()

    def getTag(self, tag: str):
        if tag not in self.file.keys():
            # os.system("clear")
            print("Ogiltig tagg!")
            print("Se till att skanna taggen separat från plånbok, mobilskal osv.")
            print("")
            return Modal("", "")
        return Modal(tag, self.file[tag])

    def start(self, runs=0):
        loop = False
        index: int = 0
        while loop == False:
            if runs <= 0:
                # Clears the terminal output
                os.system("clear")
                # Clears the previous input buffer
                sys.stdout.flush()
                tcflush(sys.stdin, TCIOFLUSH)

            if runs > 0 and index == runs - 1:
                loop = True

            index += 1

            print("Ready")
            value = input("")
            if (len(value) == 0 or len(value) > 9):
                print("Var snäll skanna en korrekt tagg.")
                print("")
                sleep(3)
                continue

            print("Please Wait...")
            modal = self.getTag(value)

            if modal.tag == "" or modal.cls == "":
                time.sleep(3)
                continue

            print(modal.tag, modal.cls)
            print("")
            time.sleep(1)
