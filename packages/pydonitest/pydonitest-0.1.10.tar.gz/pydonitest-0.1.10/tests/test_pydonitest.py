#!/usr/bin/env python

"""Tests for `pydonitest` package."""


import os
import unittest
import pathlib
# from click.testing import CliRunner

# from pydonitest import pydonitest
# from pydonitest import cli
import pydonitest
import datetime


class TestPydonitest(unittest.TestCase):
    """
    Tests for `pydonitest` package.
    """

    # def test_command_line_interface(self):
    #     """Test the CLI."""
    #     runner = CliRunner()
    #     result = runner.invoke(cli.main)
    #     assert result.exit_code == 0
    #     assert 'pydonitest.cli.main' in result.output
    #     help_result = runner.invoke(cli.main, ['--help'])
    #     assert help_result.exit_code == 0
    #     assert '--help  Show this message and exit.' in help_result.output

    def test_advanced_strip(self):
        result = pydonitest.advanced_strip("""
        test   """)
        self.assertIsInstance(result, str)
        self.assertEqual(result, 'test')

    def test_syscmd(self):
        result_bytes = pydonitest.syscmd('uptime')
        self.assertIsInstance(result_bytes, bytes)

        result_str = pydonitest.syscmd('uptime', encoding='utf-8')
        self.assertIsInstance(result_str, str)
        self.assertIn('load averages', result_str)

    def test_listfiles(self):
        result_nonrecursive = pydonitest.listfiles(path=os.path.join('test_data', 'txt', 'nonempty_dir_flat'))
        self.assertGreater(len(result_nonrecursive), 0)

        result_nonrecursive_txt = pydonitest.listfiles(path=os.path.join('test_data', 'txt', 'nonempty_dir_flat'), ext='txt')
        self.assertGreater(len(result_nonrecursive_txt), 0)
        unique_extensions = list(set([os.path.splitext(x)[1] for x in result_nonrecursive_txt]))
        self.assertEqual(len(unique_extensions), 1)
        self.assertEqual(unique_extensions[0], '.txt')

        result_recursive = pydonitest.listfiles(path=os.path.join('test_data', 'txt', 'nonempty_dir_subdirs'), recursive=True)
        self.assertGreater(len(result_recursive), 0)
        self.assertTrue(any(['subdir_1_1_3' in x for x in result_recursive]))

    def test_listdirs(self):
        result_nonrecursive = pydonitest.listdirs(path=os.path.join('test_data', 'txt', 'nonempty_dir_flat'))
        self.assertEqual(len(result_nonrecursive), 0)

        result_recursive = pydonitest.listdirs(path=os.path.join('test_data', 'txt', 'nonempty_dir_subdirs'), recursive=True)
        self.assertGreater(len(result_recursive), 0)
        self.assertTrue(any(['subdir_1_1_3' in x for x in result_recursive]))

    def test_ensurelist(self):
        result = pydonitest.ensurelist('test')
        self.assertEqual(result, ['test'])

        result = pydonitest.ensurelist(['test'])
        self.assertEqual(result, ['test'])

    def test_print_apple_ascii_art(self):
        pydonitest.print_apple_ascii_art()
        pydonitest.print_apple_ascii_art(by_line=True)
        pydonitest.print_apple_ascii_art(by_char=True)

    def test_systime(self):
        now = pydonitest.systime(as_string=False)
        self.assertIsInstance(now, datetime.datetime)
        self.assertLessEqual(now, datetime.datetime.now())

        now_str = pydonitest.systime(as_string=True)
        self.assertRegex(now_str, r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$')

        now_str_compact = pydonitest.systime(as_string=True, compact=True)
        self.assertRegex(now_str_compact, r'^\d{8}_\d{6}$')

    def test_sysdate(self):
        now = pydonitest.sysdate(as_string=False)
        self.assertIsInstance(now, datetime.datetime)
        self.assertLessEqual(now, datetime.datetime.now())

        now_str = pydonitest.sysdate(as_string=True)
        self.assertRegex(now_str, r'^\d{4}-\d{2}-\d{2}$')

        now_str_compact = pydonitest.sysdate(as_string=True, compact=True)
        self.assertRegex(now_str_compact, r'^\d{8}$')

    def test_naturalsort(self):
        result = pydonitest.naturalsort(lst=['1item', '10item', '3item', '2item'])
        expectation = ['1item', '2item', '3item', '10item']
        self.assertEqual(result, expectation)

    def test_fmt_seconds(self):
        result = pydonitest.fmt_seconds(time_in_sec=91000, units='auto', round_digits=2)
        self.assertEqual(result['units'], 'days')
        self.assertEqual(result['value'], 1.05)

        result = pydonitest.fmt_seconds(time_in_sec=91000, units='seconds', round_digits=2)
        self.assertEqual(result['units'], 'seconds')
        self.assertEqual(result['value'], 91000)

        result = pydonitest.fmt_seconds(time_in_sec=91000, units='minutes', round_digits=2)
        self.assertEqual(result['units'], 'minutes')
        self.assertEqual(result['value'], 1516.67)

        result = pydonitest.fmt_seconds(time_in_sec=91000, units='hours', round_digits=2)
        self.assertEqual(result['units'], 'hours')
        self.assertEqual(result['value'], 25.28)

        result = pydonitest.fmt_seconds(time_in_sec=91000, units='days', round_digits=2)
        self.assertEqual(result['units'], 'days')
        self.assertEqual(result['value'], 1.05)

    def test_listmode(self):
        result = pydonitest.listmode(lst=['a', 'b', 'a', 'a', 'c', 'd', 'b'])
        self.assertEqual(result, 'a')

    def test_cap_nth_char(self):
        result = pydonitest.cap_nth_char(string='string', n=3)
        self.assertEqual(result, 'strIng')

    def test_replace_nth_char(self):
        result = pydonitest.replace_nth_char(string='string', n=3, replacement='I')
        self.assertEqual(result, 'strIng')

    def test_insert_nth_char(self):
        result = pydonitest.insert_nth_char(string='strng', n=3, char='I')
        self.assertEqual(result, 'strIng')

    def test_human_filesize(self):
        self.assertEqual(pydonitest.human_filesize(1e0), '1 B')
        self.assertEqual(pydonitest.human_filesize(1e3), '1.0 KB')
        self.assertEqual(pydonitest.human_filesize(1e6), '977 KB')
        self.assertEqual(pydonitest.human_filesize(1e9), '954 MB')
        self.assertEqual(pydonitest.human_filesize(1e12), '931 GB')
        self.assertEqual(pydonitest.human_filesize(1e15), '909 TB')
        self.assertEqual(pydonitest.human_filesize(1e18), '888 PB')
        self.assertEqual(pydonitest.human_filesize(1e21), '867 EB')
        self.assertEqual(pydonitest.human_filesize(1e24), '847 ZB')
        self.assertEqual(pydonitest.human_filesize(1e27), '827 YB')

    def test_split_at(self):
        result = pydonitest.split_at(lst=['a', 'b', 'c'], idx=1)
        self.assertEqual(result, [['a'], ['b', 'c']])

        result = pydonitest.split_at(lst=[1, 2, 3, 4, 5, 6], idx=[2, 4])
        self.assertEqual(result, [[1, 2], [3, 4], [5, 6]])

    def test_duplicated(self):
        result = pydonitest.duplicated(lst=['a', 'b', 'b', 'c', 'c', 'c'])
        self.assertEqual(result, [False, False, True, False, True, True])

    def test_test_value(self):
        self.assertEqual(pydonitest.test_value('True', 'bool'), True)
        self.assertEqual(pydonitest.test_value('true', 'bool'), True)
        self.assertEqual(pydonitest.test_value('t', 'bool'), True)
        self.assertEqual(pydonitest.test_value('yes', 'bool'), True)
        self.assertEqual(pydonitest.test_value('y', 'bool'), True)
        self.assertEqual(pydonitest.test_value('False', 'bool'), True)
        self.assertEqual(pydonitest.test_value('false', 'bool'), True)
        self.assertEqual(pydonitest.test_value('f', 'bool'), True)
        self.assertEqual(pydonitest.test_value('no', 'bool'), True)
        self.assertEqual(pydonitest.test_value('n', 'bool'), True)
        self.assertEqual(pydonitest.test_value('false', 'bool', return_coerced_value=True), False)

        self.assertEqual(pydonitest.test_value('abc', 'int'), False)
        self.assertEqual(pydonitest.test_value('5', 'int'), True)
        self.assertEqual(pydonitest.test_value('5.5', 'integer'), False)

        self.assertEqual(pydonitest.test_value('abc', 'float'), False)
        self.assertEqual(pydonitest.test_value('5', 'float'), False)
        self.assertEqual(pydonitest.test_value('5.5', 'float'), True)

        self.assertEqual(pydonitest.test_value('2021-05-16', 'date'), True)
        self.assertEqual(pydonitest.test_value('2021-05-16  ', 'date'), True)
        self.assertEqual(pydonitest.test_value('2021-05-16 11:46:45', 'date'), False)
        self.assertEqual(pydonitest.test_value('abc', 'date'), False)
        self.assertEqual(pydonitest.test_value('5.5', 'date'), False)

        self.assertEqual(pydonitest.test_value('2021-05-16', 'datetime'), False)
        self.assertEqual(pydonitest.test_value('2021-05-16 11:46:45', 'datetime'), True)
        self.assertEqual(pydonitest.test_value('abc', 'datetime'), False)
        self.assertEqual(pydonitest.test_value('5.5', 'datetime'), False)

        self.assertEqual(pydonitest.test_value(os.path.expanduser('~/Desktop'), 'path'), True)
        self.assertEqual(pydonitest.test_value(os.path.expanduser('~/Desktop'), 'path exists'), True)




os.chdir(os.path.dirname(__file__))
test = TestPydonitest()

test_methods = [x for x in dir(test) if x.startswith('test_')]
for method in test_methods:
    getattr(test, method)()
