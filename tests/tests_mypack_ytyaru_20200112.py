#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from mypack_ytyaru_20200112 import mypack_ytyaru_20200112

class TestMyPack(unittest.TestCase):
    def test(self):
        self.assertEqual('mymethod return.', mypack_ytyaru_20200112.mymethod())


if __name__ == '__main__':
    unittest.main()

