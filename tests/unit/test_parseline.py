# Overzicht
# @bd0nd4lds
# See LICENSE for details

import unittest

from overzicht import _parse_line


class TestParseLine(unittest.TestCase):
    def test_TCP_OUT(self):
        line = "TCP OUT 1428: <x02>ANS<x02> A01271I                                  00       <>"
        result = _parse_line(line)
        self.assertTrue(result)

    def test_TCP_IN(self):
        line = "TCP IN 1428: <x02>ANS<x02> A01271I                                  00       <>"
        result = _parse_line(line)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
