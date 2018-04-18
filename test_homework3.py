# File: test_homework3.py
# Author: Andrew Smith
# Date: 4/17/2018

import homework3 as hw
import unittest

class TestHomework3(unittest.TestCase):

    _db_path = './class.db'

    def test_create_dataframe_path(self):
        bad_path = ''
        with self.assertRaises(ValueError):
            hw.create_dataframe(bad_path)

    def test_create_dataframe_language_column(self):
        column_name = 'language'
        data = hw.create_dataframe(self._db_path)
        self.assertTrue(column_name in data.columns)

    def test_create_dataframe_key(self):
        key = ['video_id', 'language']
        data = hw.create_dataframe(self._db_path)
        grouped = data.groupby(key)
        size = grouped.size().reset_index()
        self.assertGreater(len(size[size[0] > 1]), 0)

