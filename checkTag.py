import sys
import time
import json
import sys
import os
from termios import tcflush, TCIOFLUSH


class Modal:
    def __init__(self, tag: str, cls: str):
        self.tag = tag
        self.cls = cls


class CheckTag:
    def __init__(self):
        self.file = open("tags.json")
        # Creates a dictionary that contains all the tags and the connected class,
        # to be able to search for specific tags
        self.file: dict = json.load(self.file)

    def getTag(self, tag: str):
        if tag not in self.file.keys():
            # os.system("clear")
            print("Ogiltig tagg!")
            print("Se till att skanna taggen separat från plånbok, mobilskal osv.")
            return Modal("", "")
        return Modal(tag, self.file[tag])

    def start(self):
        while True:
            # Clears the terminal output
            os.system("clear")
            # Clears the previous input buffer
            sys.stdout.flush()
            tcflush(sys.stdin, TCIOFLUSH)

            print("Ready")
            value = input("")
            if (len(value) == 0 or len(value) > 9):
                continue

            print("Please Wait...")
            modal = self.getTag(value)

            if modal.tag == "" or modal.cls == "":
                time.sleep(3)
                continue

            print(modal.tag, modal.cls)
            print("")
            time.sleep(1)
