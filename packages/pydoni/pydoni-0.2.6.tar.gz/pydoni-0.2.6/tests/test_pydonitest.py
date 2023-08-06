#!/usr/bin/env python

"""Tests for `pydoni` package."""


import os
import unittest
import pathlib
# from click.testing import CliRunner

# from pydoni import pydoni
# from pydoni import cli
import datetime
import pandas as pd
import pydoni


class Testpydoni(unittest.TestCase):
    """
    Tests for `pydoni` package.
    """

    # def test_command_line_interface(self):
    #     """Test the CLI."""
    #     runner = CliRunner()
    #     result = runner.invoke(cli.main)
    #     assert result.exit_code == 0
    #     assert 'pydoni.cli.main' in result.output
    #     help_result = runner.invoke(cli.main, ['--help'])
    #     assert help_result.exit_code == 0
    #     assert '--help  Show this message and exit.' in help_result.output

    def test_version(self):
        main_package_dir = '..'

        with open(os.path.join(main_package_dir, 'setup.py')) as f:
            setup_py_contents = f.read().split()
            setup_py_version_str = [x for x in setup_py_contents if 'version' in x][0]
            setup_py_version = setup_py_version_str.replace('version=', '').replace(',', '').replace("'", '')

        with open(os.path.join(main_package_dir, 'setup.cfg')) as f:
            setup_cfg_contents = f.read().split('\n')
            setup_cfg_version_str = [x for x in setup_cfg_contents if 'current_version' in x][0]
            setup_cfg_version = setup_cfg_version_str.split('=')[1].strip()

        with open(os.path.join(main_package_dir, 'pydoni', '__init__.py')) as f:
            init_py_contents = f.read().split('\n')
            init_py_version_str = [x for x in init_py_contents if '__version__' in x][0]
            init_py_version = init_py_version_str.split('=')[1].replace("'", '').strip()


        self.assertEqual(setup_py_version, setup_cfg_version,
                         msg='Version numbers in setup.py and setup.cfg are out of sync!')
        self.assertEqual(setup_py_version, init_py_version,
                         msg='Version numbers in setup.py and __init__.py are out of sync!')
        self.assertEqual(setup_cfg_version, init_py_version,
                         msg='Version numbers in setup.cfg and __init__.py are out of sync!')

    def test_advanced_strip(self):
        result = pydoni.advanced_strip("""
        test   """)
        self.assertIsInstance(result, str)
        self.assertEqual(result, 'test')

    def test_syscmd(self):
        result_bytes = pydoni.syscmd('uptime')
        self.assertIsInstance(result_bytes, bytes)

        result_str = pydoni.syscmd('uptime', encoding='utf-8')
        self.assertIsInstance(result_str, str)
        self.assertIn('load averages', result_str)

    def test_listfiles(self):
        result_nonrecursive = pydoni.listfiles(path=os.path.join('test_data', 'txt', 'nonempty_dir_flat'))
        self.assertGreater(len(result_nonrecursive), 0)

        result_nonrecursive_txt = pydoni.listfiles(path=os.path.join('test_data', 'txt', 'nonempty_dir_flat'), ext='txt')
        self.assertGreater(len(result_nonrecursive_txt), 0)
        unique_extensions = list(set([os.path.splitext(x)[1] for x in result_nonrecursive_txt]))
        self.assertEqual(len(unique_extensions), 1)
        self.assertEqual(unique_extensions[0], '.txt')

        result_recursive = pydoni.listfiles(path=os.path.join('test_data', 'txt', 'nonempty_dir_subdirs'), recursive=True)
        self.assertGreater(len(result_recursive), 0)
        self.assertTrue(any(['subdir_1_1_3' in x for x in result_recursive]))

    def test_listdirs(self):
        result_nonrecursive = pydoni.listdirs(path=os.path.join('test_data', 'txt', 'nonempty_dir_flat'))
        self.assertEqual(len(result_nonrecursive), 0)

        result_recursive = pydoni.listdirs(path=os.path.join('test_data', 'txt', 'nonempty_dir_subdirs'), recursive=True)
        self.assertGreater(len(result_recursive), 0)
        self.assertTrue(any(['subdir_1_1_3' in x for x in result_recursive]))

    def test_ensurelist(self):
        result = pydoni.ensurelist('test')
        self.assertEqual(result, ['test'])

        result = pydoni.ensurelist(['test'])
        self.assertEqual(result, ['test'])

    def test_print_apple_ascii_art(self):
        pydoni.print_apple_ascii_art()
        pydoni.print_apple_ascii_art(by_line=True)
        pydoni.print_apple_ascii_art(by_char=True)

    def test_systime(self):
        now = pydoni.systime(as_string=False)
        self.assertIsInstance(now, datetime.datetime)
        self.assertLessEqual(now, datetime.datetime.now())

        now_str = pydoni.systime(as_string=True)
        self.assertRegex(now_str, r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$')

        now_str_compact = pydoni.systime(as_string=True, compact=True)
        self.assertRegex(now_str_compact, r'^\d{8}_\d{6}$')

    def test_sysdate(self):
        now = pydoni.sysdate(as_string=False)
        self.assertIsInstance(now, datetime.datetime)
        self.assertLessEqual(now, datetime.datetime.now())

        now_str = pydoni.sysdate(as_string=True)
        self.assertRegex(now_str, r'^\d{4}-\d{2}-\d{2}$')

        now_str_compact = pydoni.sysdate(as_string=True, compact=True)
        self.assertRegex(now_str_compact, r'^\d{8}$')

    def test_naturalsort(self):
        result = pydoni.naturalsort(lst=['1item', '10item', '3item', '2item'])
        expectation = ['1item', '2item', '3item', '10item']
        self.assertEqual(result, expectation)

    def test_fmt_seconds(self):
        result = pydoni.fmt_seconds(time_in_sec=91000, units='auto', round_digits=2)
        self.assertEqual(result['units'], 'days')
        self.assertEqual(result['value'], 1.05)

        result = pydoni.fmt_seconds(time_in_sec=91000, units='seconds', round_digits=2)
        self.assertEqual(result['units'], 'seconds')
        self.assertEqual(result['value'], 91000)

        result = pydoni.fmt_seconds(time_in_sec=91000, units='minutes', round_digits=2)
        self.assertEqual(result['units'], 'minutes')
        self.assertEqual(result['value'], 1516.67)

        result = pydoni.fmt_seconds(time_in_sec=91000, units='hours', round_digits=2)
        self.assertEqual(result['units'], 'hours')
        self.assertEqual(result['value'], 25.28)

        result = pydoni.fmt_seconds(time_in_sec=91000, units='days', round_digits=2)
        self.assertEqual(result['units'], 'days')
        self.assertEqual(result['value'], 1.05)

    def test_listmode(self):
        result = pydoni.listmode(lst=['a', 'b', 'a', 'a', 'c', 'd', 'b'])
        self.assertEqual(result, 'a')

    def test_cap_nth_char(self):
        result = pydoni.cap_nth_char(string='string', n=3)
        self.assertEqual(result, 'strIng')

    def test_replace_nth_char(self):
        result = pydoni.replace_nth_char(string='string', n=3, replacement='I')
        self.assertEqual(result, 'strIng')

    def test_insert_nth_char(self):
        result = pydoni.insert_nth_char(string='strng', n=3, char='I')
        self.assertEqual(result, 'strIng')

    def test_human_filesize(self):
        self.assertEqual(pydoni.human_filesize(1e0), '1 B')
        self.assertEqual(pydoni.human_filesize(1e3), '1.0 KB')
        self.assertEqual(pydoni.human_filesize(1e6), '977 KB')
        self.assertEqual(pydoni.human_filesize(1e9), '954 MB')
        self.assertEqual(pydoni.human_filesize(1e12), '931 GB')
        self.assertEqual(pydoni.human_filesize(1e15), '909 TB')
        self.assertEqual(pydoni.human_filesize(1e18), '888 PB')
        self.assertEqual(pydoni.human_filesize(1e21), '867 EB')
        self.assertEqual(pydoni.human_filesize(1e24), '847 ZB')
        self.assertEqual(pydoni.human_filesize(1e27), '827 YB')

    def test_split_at(self):
        result = pydoni.split_at(lst=['a', 'b', 'c'], idx=1)
        self.assertEqual(result, [['a'], ['b', 'c']])

        result = pydoni.split_at(lst=[1, 2, 3, 4, 5, 6], idx=[2, 4])
        self.assertEqual(result, [[1, 2], [3, 4], [5, 6]])

    def test_duplicated(self):
        result = pydoni.duplicated(lst=['a', 'b', 'b', 'c', 'c', 'c'])
        self.assertEqual(result, [False, False, True, False, True, True])

    def test_test_value(self):
        self.assertEqual(pydoni.test_value('True', 'bool'), True)
        self.assertEqual(pydoni.test_value('true', 'bool'), True)
        self.assertEqual(pydoni.test_value('t', 'bool'), True)
        self.assertEqual(pydoni.test_value('yes', 'bool'), True)
        self.assertEqual(pydoni.test_value('y', 'bool'), True)
        self.assertEqual(pydoni.test_value('False', 'bool'), True)
        self.assertEqual(pydoni.test_value('false', 'bool'), True)
        self.assertEqual(pydoni.test_value('f', 'bool'), True)
        self.assertEqual(pydoni.test_value('no', 'bool'), True)
        self.assertEqual(pydoni.test_value('n', 'bool'), True)
        self.assertEqual(pydoni.test_value('false', 'bool', return_coerced_value=True), False)

        self.assertEqual(pydoni.test_value('abc', 'int'), False)
        self.assertEqual(pydoni.test_value('5', 'int'), True)
        self.assertEqual(pydoni.test_value('5.5', 'integer'), False)

        self.assertEqual(pydoni.test_value('abc', 'float'), False)
        self.assertEqual(pydoni.test_value('5', 'float'), False)
        self.assertEqual(pydoni.test_value('5.5', 'float'), True)

        self.assertEqual(pydoni.test_value('2021-05-16', 'date'), True)
        self.assertEqual(pydoni.test_value('2021-05-16  ', 'date'), True)
        self.assertEqual(pydoni.test_value('2021-05-16 11:46:45', 'date'), False)
        self.assertEqual(pydoni.test_value('abc', 'date'), False)
        self.assertEqual(pydoni.test_value('5.5', 'date'), False)

        self.assertEqual(pydoni.test_value('2021-05-16', 'datetime'), False)
        self.assertEqual(pydoni.test_value('2021-05-16 11:46:45', 'datetime'), True)
        self.assertEqual(pydoni.test_value('abc', 'datetime'), False)
        self.assertEqual(pydoni.test_value('5.5', 'datetime'), False)

        self.assertEqual(pydoni.test_value(os.path.expanduser('~/Desktop'), 'path'), True)
        self.assertEqual(pydoni.test_value(os.path.expanduser('~/Desktop'), 'path exists'), True)

    def test_extract_colorpalette(self):
        result = pydoni.extract_colorpalette('Blues')
        self.assertEqual(result[0:3], ['#f7fbff', '#f6faff', '#f5fafe'])

    def test_rename_dict_keys(self):
        dct = {'a': 1, 'b': 2, 'c': 3}
        result = pydoni.rename_dict_keys(dct=dct, key_dict={'c': 'd'})
        expectation = {'a': 1, 'b': 2, 'd': 3}
        self.assertEqual(result, expectation)

    def test_append_filename_suffix(self):
        testfile = os.path.expanduser('~/Desktop/testfile.txt')
        expectation = os.path.expanduser('~/Desktop/testfile-1.txt')
        self.assertEqual(pydoni.append_filename_suffix(fpath=testfile, suffix='-1'), expectation)

    def test_textfile_len(self):
        testfile = 'test_data/txt/nonempty_dir_subdirs/textfile_15.txt'
        self.assertEqual(pydoni.textfile_len(fpath=testfile), 10)

    def test_dirsize(self):
        testdir = 'test_data/txt/nonempty_dir_subdirs/subdir_1'
        self.assertEqual(pydoni.dirsize(dpath=testdir), 25187)

    def test_collapse_df_columns(self):
        testdf = pd.Series([1, 2, 3], index=['a','b','c']).to_frame().T
        testdf.columns = pd.MultiIndex.from_product([['col_group'], testdf.columns])
        result = list(pydoni.collapse_df_columns(testdf).columns)
        expectation = ['col_group_a', 'col_group_b', 'col_group_c']
        self.assertEqual(result, expectation)

    def test_print_columns(self):
        pydoni.print_columns(lst=['a', 'b', 'c', 'd'], ncol=1)
        pydoni.print_columns(lst=['a', 'b', 'c', 'd'], ncol=2)
        pydoni.print_columns(lst=['a', 'b', 'c', 'd'], ncol=3)
        pydoni.print_columns(lst=['a', 'b', 'c', 'd'], ncol=3, delay=.01)

    def test_stabilize_postfix(self):
        result = pydoni.stabilize_postfix(key='test', max_len=20, fillchar='•', side='right')
        self.assertEqual(result, '••••••••••••••••test')
        result = pydoni.stabilize_postfix(key='test', max_len=10, fillchar='•', side='left')
        self.assertEqual(result, 'test••••••')
        result = pydoni.stabilize_postfix(key='test', max_len=3, fillchar='•', side='left')
        self.assertEqual(result, 'tes')

    def test_postgres(self):
        try:
            pg = pydoni.Postgres()
            connected = True
        except:
            connected = False

        if connected:
            # Not all users of this library will have Postgres set up, so only execute
            # tests if Postgres connected successfully.
            #
            # Now perform a series of commands to ensure that Postgres class methods are
            # working as intended.

            # Method: read_sql(). Choose a default table that always exists
            result = pg.read_sql('select * from information_schema.tables limit 1')

            # Method: get_table_name()
            self.assertEqual(pg.get_table_name(schema_name=None, table_name='pg_stat'), 'pg_stat')
            self.assertEqual(pg.get_table_name(schema_name='information_schema', table_name='tables'), 'information_schema.tables')

            # Method: validate_dtype()
            result = pg.validate_dtype(schema_name='information_schema',
                                       table_name='tables',
                                       col='table_catalog',
                                       val='string value')
            self.assertEqual(result, True)
            result = pg.validate_dtype(schema_name='information_schema',
                                       table_name='tables',
                                       col='table_catalog',
                                       val=5)
            self.assertEqual(result, False)

            # Method: infoschema()
            result = sorted(pg.infoschema(infoschema_table='tables').columns)
            result_sql_direct = sorted(pg.read_sql('select * from information_schema.tables limit 1').columns)
            self.assertEqual(result, result_sql_direct)

            # Method: build_update()
            result = pg.build_update(schema_name='pg_catalog',
                                     table_name='pg_stat_database',
                                     pkey_name='datid',
                                     pkey_value=12345,
                                     columns=['tup_returned', 'tup_fetched'],
                                     values=[11111, 22222],
                                     validate=True,
                                     newlines=False)
            expectation = 'UPDATE pg_catalog.pg_stat_database SET "tup_returned"=11111, "tup_fetched"=22222 WHERE "datid" = 12345'
            self.assertEqual(result, expectation)
            result = pg.build_update(schema_name='pg_catalog',
                                     table_name='pg_stat_database',
                                     pkey_name='datid',
                                     pkey_value=12345,
                                     columns=['tup_returned', 'tup_fetched'],
                                     values=[11111, 22222],
                                     validate=False,
                                     newlines=True)
            expectation = 'UPDATE pg_catalog.pg_stat_database\nSET "tup_returned"=11111, \n    "tup_fetched"=22222\nWHERE "datid" = 12345'
            self.assertEqual(result, expectation)

            # Method: build_insert()
            result = pg.build_insert(schema_name='pg_catalog',
                                     table_name='pg_stat_database',
                                     columns=['tup_returned', 'tup_fetched'],
                                     values=[11111, 22222],
                                     validate=True,
                                     newlines=False)
            expectation = 'insert into pg_catalog.pg_stat_database ("tup_returned", "tup_fetched") values (11111, 22222)'
            self.assertEqual(result, expectation)
            result = pg.build_insert(schema_name='pg_catalog',
                                     table_name='pg_stat_database',
                                     columns=['tup_returned', 'tup_fetched'],
                                     values=[11111, 22222],
                                     validate=False,
                                     newlines=True)
            expectation = 'insert into pg_catalog.pg_stat_database ("tup_returned", "tup_fetched")\nvalues (11111, 22222)'
            self.assertEqual(result, expectation)

            # Method: build_delete()
            result = pg.build_delete(schema_name='pg_catalog',
                                     table_name='pg_stat_database',
                                     pkey_name='datid',
                                     pkey_value=12345,
                                     newlines=False)
            expectation = 'delete from pg_catalog.pg_stat_database where datid = 12345'
            self.assertEqual(result, expectation)
            result = pg.build_delete(schema_name='pg_catalog',
                                     table_name='pg_stat_database',
                                     pkey_name='datid',
                                     pkey_value=12345,
                                     newlines=True)
            expectation = 'delete from pg_catalog.pg_stat_database\nwhere datid = 12345'
            self.assertEqual(result, expectation)

            # Method: col_names()
            result = pg.col_names(schema_name='pg_catalog', table_name='pg_stat_database')
            self.assertIn('datid', result)

            # Method: col_dtypes()
            result = pg.col_dtypes(schema_name='pg_catalog', table_name='pg_stat_database')
            self.assertEqual(result['datid'], 'oid')

            # Method: read_table()
            result = pg.read_table(schema_name='pg_catalog', table_name='pg_stat_database')
            self.assertGreater(result.shape[0], 0)
            self.assertGreater(result.shape[1], 0)

            # Method: dump()
            # Just make sure pg_dump is installed
            # find_binary('pg_dump')




os.chdir(os.path.dirname(__file__))
test = Testpydoni()

test_methods = [x for x in dir(test) if x.startswith('test_')]
for method in test_methods:
    getattr(test, method)()
