import json
import unittest
from unittest.mock import patch

from checkTag import CheckTag

import tracemalloc

tracemalloc.start()
#          Incorrect,  Incorrect,   Correct,     Incorrect len, Correct,    Correct
tagList = ["67523475", "876348574", "952224470", "7978497850", "537059654", "536961030"]


class Test(unittest.TestCase):
    @patch('builtins.input', side_effect=tagList)
    def test_checkTag(self, mock):
        CheckTag().start(runs=len(tagList))


if __name__ == '__main__':
    unittest.main()
