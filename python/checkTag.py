import json
from termios import tcflush, TCIOFLUSH

from checkTime import CheckTime
from modal import Modal
from ui import UI
import turtle


class CheckTag:
    def __init__(self):
        self.ui = UI()
        file = open("./data/tags.json")
        # Creates a dictionary that contains all the tags and the connected class,
        # to be able to search for specific tags
        self.file: dict = json.load(file)
        file.close()

        self.ui.idleScreen()

        self.keyList = []
        self.finished = True

        self.keys_activate()
        turtle.mainloop()

    def keys_activate(self):
        turtle.onkey(lambda: self.append("0"), "0")
        turtle.onkey(lambda: self.append("1"), "1")
        turtle.onkey(lambda: self.append("2"), "2")
        turtle.onkey(lambda: self.append("3"), "3")
        turtle.onkey(lambda: self.append("4"), "4")
        turtle.onkey(lambda: self.append("5"), "5")
        turtle.onkey(lambda: self.append("6"), "6")
        turtle.onkey(lambda: self.append("7"), "7")
        turtle.onkey(lambda: self.append("8"), "8")
        turtle.onkey(lambda: self.append("9"), "9")
        turtle.onkey(lambda: self.start(), "Return")
        turtle.listen()

    def keys_deactivate(self):
        turtle.onkey(None, "0")
        turtle.onkey(None, "1")
        turtle.onkey(None, "2")
        turtle.onkey(None, "3")
        turtle.onkey(None, "4")
        turtle.onkey(None, "5")
        turtle.onkey(None, "6")
        turtle.onkey(None, "7")
        turtle.onkey(None, "8")
        turtle.onkey(None, "9")
        turtle.onkey(None, "Return")
        turtle.listen()

    def getTag(self, tag: str):
        if tag not in self.file.keys():
            return Modal("", "")
        return Modal(tag=tag, cls=self.file[tag])

    def timeCheck(self, modal: Modal):
        # os.system("clear")
        result = CheckTime(modal).check()
        if result[0] == False:
            self.ui.wrongTime(result)
        if result[0] == True:
            self.ui.onTime()

    def start(self):
        self.keys_deactivate()

        value = "".join(self.keyList)
        self.keyList.clear()

        # The length of the NFC tags MFR number is 9
        if len(value) == 0 or len(value) > 9 or len(value) < 9:
            self.ui.invalidTag()
            self.keys_activate()
            return

        self.ui.idleScreen()
        modal = self.getTag(value)

        if modal.tag == "" or modal.cls == "":
            print("sdhf8sd8yh8fy9sdf98sd8hfb98d")
            self.ui.invalidTag()
            self.keys_activate()
            return

        print(modal.tag, modal.cls)
        self.timeCheck(modal)
        self.keys_activate()

    def append(self, key):
        if len(self.keyList) <= 9:
            self.keyList.append(key)
        if len(self.keyList) > 9:
            self.keyList.clear()
