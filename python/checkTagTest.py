from time import sleep
import unittest
import tracemalloc
import threading
from pynput.keyboard import Key, Controller
import os

from checkTag import CheckTag

os.system("clear")
tracemalloc.start()
#          Incorrect,  Incorrect,   Correct,     Incorrect len, Correct,    Correct test-tag
tagList = ["67523475", "876348574", "952224470", "7978497850", "537059654", "101051865"]
keyboard = Controller()


def sendKeys():
    for tag in tagList:
        sleep(4.5)
        keyboard.type(tag)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)


class Test(unittest.TestCase):
    def test_checkTag(self):
        threading.Thread(target=lambda: sendKeys()).start()
        CheckTag()


if __name__ == '__main__':
    unittest.main()
