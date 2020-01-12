#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from mypack import mypack

class TestMyPack(unittest.TestCase):
    def test(self):
#        self.assertEqual('mymethod return.', mymethod())
        self.assertEqual('mymethod return.', mypack.mymethod())


if __name__ == '__main__':
    unittest.main()

