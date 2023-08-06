__author__ = 'Andoni Sooklaris'
__email__ = 'andoni.sooklaris@gmail.com'
__version__ = '0.1.15'


import click
from pandas.core.algorithms import isin
import colr
import itertools
import logging
import matplotlib
import sqlalchemy
import matplotlib.cm
import numpy as np
import os
import csv
import pandas as pd
import pydoni
import PyInquirer as inq
import pylab
import re
import subprocess
import threading
import time
import pathlib
import typing
from typing import Any
from emoji import emojize
from tqdm import tqdm, trange
from collections import OrderedDict
from datetime import datetime
from dateutil.parser import parse
from dateutil.tz import tzoffset


# Module setup ---------------

module_loglevel = logging.DEBUG


class ExtendedLogger(logging.Logger):
    """
    Extend the logging.Logger class.
    """
    def __init__(self, name, level=logging.NOTSET):
        self._count = 0
        self._countLock = threading.Lock()
        return super(ExtendedLogger, self).__init__(name, level)

    def var(self, varname, value, include_modules=True, include_extended_logger=True):
        """
        Extend .debug() method to log the name, value and datatype of a variable or variables.
        Optionally include modules and instances of this class. Functionally, this allows
        for iterating over `locals()` and automatically excluding modules and/or loggers
        from the logged output, instead leaving just the variables desired to be logged.

        For example, if `locals()` returns `{'a': 1, 'b': 2, 'logging': "<module 'logging' from..."}`

        The user can set `include_modules=False` to exclude the 'logging' module when iterating
        over `locals()`:

        >>> for k, v in locals().items():
        >>>     logger.var(k, v, include_modules=False)
        {timestamp} : DEBUG : __main__ : Variable 'a' {int}: 1
        {timestamp} : DEBUG : __main__ : Variable 'b' {int}: 2
        """
        dtype = value.__class__.__name__
        value = str(value)

        if dtype == 'module' and not include_modules:
            return None

        if 'ExtendedLogger' in dtype and not include_extended_logger:
            return None

        msg = f"Variable '{varname}' {{{dtype}}}: {value}"
        return super(ExtendedLogger, self).debug(msg)

    def logvars(self, var_dict):
        """
        Iterate over dictionary and call `self.var` on each variable name, variable value pair,
        excluding modules and instances of this class.
        """
        for varname, value in var_dict.items():
            self.var(varname, value, include_modules=False, include_extended_logger=False)


def logger_setup(name: str=__name__, level: int=logging.DEBUG, equal_width: bool=False):
    """
    Standardize logger setup across pydoni package.
    """
    logging.setLoggerClass(ExtendedLogger)
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger_fmt = '%(asctime)s : %(levelname)s : %(name)s : %(message)s'

        if equal_width:
            logger_fmt = logger_fmt.replace('%(levelname)s', '%(levelname)-8s')

        formatter = logging.Formatter(logger_fmt)

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    return logger


logger = logger_setup(__name__, module_loglevel)


# Operating and file systems ---------------

def syscmd(cmd: str, encoding: str=''):
    """
    Runs a command on the system, waits for the command to finish, and then returns the
    text output of the command. If the command produces no text output, the command's
    return code will be returned instead. Optionally decode output bytestring.
    """
    p = subprocess.Popen(cmd,
                         shell=True,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT,
                         close_fds=True)

    p.wait()
    output = p.stdout.read()

    if len(output) > 1:
        if encoding:
            return output.decode(encoding)
        else:
            return output
    else:
        logger.var('output', output)
        logger.warn('Length of `output` is <=1, returning the process returncode')

        return p.returncode


def listfiles(path: typing.Union[str, pathlib.Path]='.',
              ext=None,
              pattern=None,
              ignore_case=True,
              full_names=False,
              recursive=False,
              include_hidden=True):
    """
    List files in a given directory.

    path {str} absolute path to search for files in
    ext {str} optional file extension or list of extensions to filter resulting files by
    pattern {str} optional filter resulting files by matching regex pattern
    ignore_case {bool} do not consider case in when filtering for `pattern` parameter
    full_names {bool} return absolute filepaths
    recursive {bool} search recursively down the directory tree
    include_hidden {bool} include hidden files in resulting file list
    """
    owd = os.getcwd()
    os.chdir(path)

    if recursive:
        fpaths = []
        for root, dirs, filenames in os.walk('.'):
            for f in filenames:
                fpaths.append(os.path.join(root, f).replace('./', ''))
    else:
        fpaths = [f for f in os.listdir() if os.path.isfile(f)]

    if not include_hidden:
        fpaths = [f for f in fpaths if not os.path.basename(f).startswith('.')]

    if pattern is not None:
        if ignore_case:
            fpaths = [f for f in fpaths if re.search(pattern, f, re.IGNORECASE)]
        else:
            fpaths = [f for f in fpaths if re.search(pattern, f)]

    if ext:
        ext = [x.lower() for x in ensurelist(ext)]
        ext = ['.' + x if not x.startswith('.') else x for x in ext]
        fpaths = [x for x in fpaths if os.path.splitext(x)[1].lower() in ext]

    if full_names:
        path_expand = os.getcwd() if path == '.' else path
        fpaths = [os.path.join(path_expand, f) for f in fpaths]

    os.chdir(owd)
    return fpaths


def listdirs(path: typing.Union[str, pathlib.Path]='.', pattern: str=None, full_names: bool=False, recursive: bool=False):
    """
    List subdirectories in a given directory, optionally filtering by a regex pattern.
    """
    owd = os.getcwd()
    os.chdir(path)

    if recursive:
        dirs = []
        for root, subdirs, filenames in os.walk('.'):
            for subdir in subdirs:
                dirs.append(os.path.join(root, subdir).replace('./', ''))
    else:
        dirs = [name for name in os.listdir('.') if os.path.isdir(os.path.join(path, name)) ]

    if full_names:
        path_expand = os.getcwd() if path == '.' else path
        dirs = [os.path.join(path_expand, dname) for dname in dirs]

    if pattern is not None:
        dirs = [d for d in dirs if re.match(pattern, d)]

    os.chdir(owd)
    return sorted(dirs)


def systime(as_string: bool=True, compact: bool=False):
    """
    Get the current datetime, optionally formatted as a string.
    """
    if as_string:
        return datetime.now().strftime('%Y%m%d_%H%M%S' if compact else '%Y-%m-%d %H:%M:%S')
    else:
        assert not compact, 'Cannot set `compact` if returning a datetime object!'
        return datetime.now()


def sysdate(as_string: bool=True, compact: bool=False):
    """
    Get the current date, optionally formatted as a string.
    """
    if as_string:
        return datetime.now().strftime('%Y%m%d' if compact else '%Y-%m-%d')
    else:
        assert not compact, 'Cannot set `compact` if returning a datetime object!'
        return datetime.now().replace(hour=0, minute=0, second=0)


def human_filesize(nbytes: int):
    """
    Convert number of bytes to human-readable filesize string.
    Source: https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python
    """
    base = 1

    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']:
        n = nbytes / base

        if n < 9.95 and unit != 'B':
            # Less than 10 then keep 1 decimal place
            value = '{:.1f} {}'.format(n, unit)
            return value

        if round(n) < 1000:
            # Less than 4 digits so use this
            value = f'{round(n)} {unit}'
            return value

        base *= 1024

    value = f'{round(n)} {unit}'

    return value


def textfile_len(fpath: typing.Union[str, pathlib.Path]):
    """
    Get number of rows in a text file.
    """
    with open(fpath) as f:
        for i, l in enumerate(f):
            pass

    return i + 1


def dirsize(dpath: typing.Union[str, pathlib.Path]='.'):
    """
    Get size of directory in bytes.
    Source: https://stackoverflow.com/questions/1392413/calculating-a-directorys-size-using-python
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(dpath):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size


def append_filename_suffix(fpath: typing.Union[str, pathlib.Path], suffix: str):
    """
    Add suffix string to filename before extension.
    """
    base, ext = os.path.splitext(fpath)

    if ext == '.icloud':
        ext_icloud = ext
        base, ext = os.path.splitext(base)
        ext += ext_icloud

    return base + suffix + ext


# Python object operations ---------------

def advanced_strip(string: str):
    """
    Strip whitespace off a string and replace all instances of >1 space with a single space.
    """
    return re.sub(r'\s+', ' ', string.strip())


def ensurelist(val: Any):
    """
    Accept a string or list and ensure that it is formatted as a list. If `val` is not a list,
    return [val]. If `val` is already a list, return as is.
    """
    return [val] if not isinstance(val, list) else val


def naturalsort(lst: list):
    """
    Sort a list with numeric elements, numerically.
    Source: https://stackoverflow.com/questions/5967500/how-to-correctly-sort-a-string-with-a-number-inside
    """
    def atoi(text):
        return int(text) if text.isdigit() else text

    def natural_keys(text):
        """
        alist.sort(key=natural_keys) sorts in human order
        http://nedbatchelder.com/blog/200712/human_sorting.html
        (See Toothy's implementation in the comments)
        """
        return [atoi(c) for c in re.split(r'(\d+)', text)]

    return sorted(lst, key=natural_keys)


def listmode(lst: list):
    """
    Get the most frequently occurring value in a list.
    """
    return max(set(lst), key=lst.count)


def cap_nth_char(string: str, n: int):
    """
    Capitalize character in `string` at zero-indexed position `n`.

    Example:
        >>> cap_nth_char(string='string', n=3, replacement='I')
        'strIng'
    """
    return string[:n] + string[n].capitalize() + string[n+1:]


def replace_nth_char(string: str, n: int, replacement: str):
    """
    Replace character in `string` at zero-indexed position `n` with `replacement`.

    Example:
        >>> replace_nth_char(string='string', n=3, replacement='I')
        'strIng'
    """
    return string[:n] + str(replacement) + string[n+1:]


def insert_nth_char(string: str, n: int, char):
    """
    Insert `char` in `string` at zero-indexed position `n`.

    Example:
        >>> insert_nth_char(string='strng', n=3, char='I')
        'strIng'
    """
    return string [:n] + str(char) + string[n:]


def split_at(lst: list, idx: int):
    """
    Split `lst` at a single position or multiple positions denoted by `idx`. Every index value
    denoted in `idx` will be the *first* item of the subsequent sublist. Return a list of lists.

    Example:
        >>> split_at(lst=['a', 'b', 'c'], idx=1)
        [['a'], ['b', 'c']]
        # Element at position 1 is the first item of the second sublist
    """
    idx = ensurelist(idx)
    return [lst[i:j] for i, j in zip([0] + idx, idx + [None])]


def duplicated(lst: list):
    """
    Return list of boolean values indicating whether each item in a list is a duplicate of
    a previous item in the list. Order matters!
    """
    dup_ind = []

    for i, item in enumerate(lst):
        tmplist = lst.copy()
        del tmplist[i]

        if item in tmplist:
            # Test if this is the first occurrence of this item in the list. If so, do not
            # count as duplicate, as the first item in a set of identical items should not
            # be counted as a duplicate

            first_idx = min(
                [i for i, x in enumerate(tmplist) if x == item])

            if i != first_idx:
                dup_ind.append(True)
            else:
                dup_ind.append(False)

        else:
            dup_ind.append(False)

    return dup_ind


def test_value(value: Any, dtype: str, return_coerced_value: bool=False, stop: bool=False):
    """
    Test if a value is an instance of type `dtype`. May accept a value of any kind.

    Parameter `dtype` must be one of ['bool', 'str', 'string', 'int', 'integer',
    'float', 'date', 'datetime', 'path', 'path exists'].

    Parameter `return_coerced_value` will cause this function to return `value` as type
    `dtype` if possible, and will raise an error otherwise.

    Parameter `stop` will cause this function to raise an error if `value` cannot be
    coerced to `dtype` instead of simply logging the error message.
    """
    class Attribute():
        """
        Empty class defined for convenient use.
        """
        pass

    def define_date_regex():
        """
        Define regex strings for all valid date components.
        """
        rgx = Attribute()
        rgx.sep = r'(\.|\/|-|_|\:)'

        rgx.year = r'(?P<year>\d{4})'
        rgx.month = r'(?P<month>\d{2})'
        rgx.day = r'(?P<day>\d{2})'

        rgx.hour = r'(?P<hour>\d{2})'
        rgx.minute = r'(?P<minute>\d{2})'
        rgx.second = r'(?P<second>\d{2})'
        rgx.microsecond = r'(?P<microsecond>\d+)'

        rgx.tz_sign = r'(?P<tz_sign>-|\+)'
        rgx.tz_hour = r'(?P<tz_hour>\d{1,2})'
        rgx.tz_minute = r'(?P<tz_minute>\d{1,2})'

        rgx.date = f'{rgx.year}{rgx.sep}{rgx.month}{rgx.sep}{rgx.day}'
        rgx.datetime = fr'{rgx.date} {rgx.hour}{rgx.sep}{rgx.minute}{rgx.sep}{rgx.second}'
        rgx.datetime_timezone = fr'{rgx.datetime}{rgx.tz_sign}{rgx.tz_hour}(:){rgx.tz_minute}'
        rgx.datetime_microsecond = fr'{rgx.datetime}(\.){rgx.microsecond}'

        return rgx

    def anchor(x):
        """
        Add regex start and end anchors to a string.
        """
        return '^' + x + '$'


    valid_dtypes = ['bool',
                    'str', 'string',
                    'int', 'integer',
                    'float',
                    'date',
                    'datetime',
                    'path',
                    'path exists']
    assert dtype in valid_dtypes, f"Datatype must be one of {', '.join(valid_dtypes)}"

    # Date/datetime regex definitions
    rgx = define_date_regex()

    coerced_value = None

    # Test bool
    if dtype == 'bool':
        if isinstance(value, bool):
            coerced_value = value
        else:
            if str(value).lower() in ['true', 't', 'yes', 'y']:
                coerced_value = True
            elif str(value).lower() in ['false', 'f', 'no', 'n']:
                coerced_value = False

    # Test string
    elif dtype in ['str', 'string']:
        try:
            coerced_value = str(value)
        except Exception as e:
            if stop:
                raise e
            else:
                logger.warn(str(e))

    # Test integer
    elif dtype in ['int', 'integer']:
        if isinstance(value, int):
            coerced_value = value
        elif str(value).isdigit():
            coerced_value = int(value)
        else:
            try:
                coerced_value = int(value)
            except Exception as e:
                if stop:
                    raise e
                else:
                    logger.warn(str(e))

    # Test float
    elif dtype == 'float':
        if isinstance(value, float) or isinstance(value, int):
            coerced_value = float(value)
        elif '.' in str(value):
            try:
                coerced_value = float(value)
            except Exception as e:
                if stop:
                    raise e
                else:
                    logger.warn(str(e))

    # Test date
    elif dtype == 'date':
        m = re.search(anchor(rgx.date), str(value).strip())
        if m:
            dt_components = dict(year=m.group('year'), month=m.group('month'), day=m.group('day'))
            dt_components = {k: int(v) for k, v in dt_components.items()}
            coerced_value = datetime(**dt_components)

    # Test datetime
    elif dtype == 'datetime':
        m_dt = re.search(anchor(rgx.datetime), str(value).strip())
        m_dt_tz = re.search(anchor(rgx.datetime_timezone), str(value).strip())
        m_dt_ms = re.search(anchor(rgx.datetime_microsecond), str(value).strip())

        if m_dt:
            dt_components = dict(year=m_dt.group('year'),
                                 month=m_dt.group('month'),
                                 day=m_dt.group('day'),
                                 hour=m_dt.group('hour'),
                                 minute=m_dt.group('minute'),
                                 second=m_dt.group('second'))
            dt_components = {k: int(v) for k, v in dt_components.items()}
            coerced_value = datetime(**dt_components)

        elif m_dt_tz:
            dt_components = dict(year=m_dt_tz.group('year'),
                                 month=m_dt_tz.group('month'),
                                 day=m_dt_tz.group('day'),
                                 hour=m_dt_tz.group('hour'),
                                 minute=m_dt_tz.group('minute'),
                                 second=m_dt_tz.group('second'))
            dt_components = {k: int(v) for k, v in dt_components.items()}

            second_offset = int(m_dt_tz.group('tz_hour')) * 60 * 60
            second_offset = -second_offset if m_dt_tz.group('tz_sign') == '-' else second_offset

            dt_components['tzinfo'] = tzoffset(None, second_offset)
            coerced_value = datetime(**dt_components)

        elif m_dt_ms:
            dt_components = dict(year=m_dt_ms.group('year'),
                                 month=m_dt_ms.group('month'),
                                 day=m_dt_ms.group('day'),
                                 hour=m_dt_ms.group('hour'),
                                 minute=m_dt_ms.group('minute'),
                                 second=m_dt_ms.group('second'),
                                 microsecond=m_dt_ms.group('microsecond'))
            dt_components = {k: int(v) for k, v in dt_components.items()}
            coerced_value = datetime(**dt_components)

    # Test path
    elif dtype == 'path':
        if '/' in value or value == '.':
            coerced_value = value

    # Test path exists
    elif dtype == 'path exists':
        if os.path.isfile(value) or os.path.isdir(value):
            coerced_value = value

    # Close function
    if coerced_value is None:
        error_str = f"Unable to coerce value '{str(value)}' (dtype: {type(value).__name__}) to {dtype}"
        logger.info(error_str)

        if return_coerced_value:
            raise ValueError(error_str)
        else:
            return False

    else:
        if return_coerced_value:
            return coerced_value
        else:
            return True


def fmt_seconds(time_in_sec: int, units: str='auto', round_digits: int=4):
    """
    Format time in seconds to a custom string. `units` parameter can be
    one of 'auto', 'seconds', 'minutes', 'hours' or 'days'.
    """
    if units == 'auto':
        if time_in_sec < 60:
            time_diff = round(time_in_sec, round_digits)
            time_measure = 'seconds'
        elif time_in_sec >= 60 and time_in_sec < 3600:
            time_diff = round(time_in_sec/60, round_digits)
            time_measure = 'minutes'
        elif time_in_sec >= 3600 and time_in_sec < 86400:
            time_diff = round(time_in_sec/3600, round_digits)
            time_measure = 'hours'
        else:
            time_diff = round(time_in_sec/86400, round_digits)
            time_measure = 'days'

    elif units in ['seconds', 'minutes', 'hours', 'days']:
        time_measure = units
        if units == 'seconds':
            time_diff = round(time_in_sec, round_digits)
        elif units == 'minutes':
            time_diff = round(time_in_sec/60, round_digits)
        elif units == 'hours':
            time_diff = round(time_in_sec/3600, round_digits)
        else:
            # Days
            time_diff = round(time_in_sec/86400, round_digits)

    return dict(zip(['units', 'value'], [time_measure, time_diff]))


def collapse_df_columns(df: pd.DataFrame, sep: str='_'):
    """
    Collapse a multi-level column index in a dataframe.
    """
    df.columns = [sep.join(col).strip() for col in df.columns.values]
    return df


def extract_colorpalette(palette_name: str, n: int=None, mode: str='hex'):
    """
    Convert color palette to color ramp list.

    palette_name {str} name of color palette
    n {int} size of color ramp. If None, automatically return the maximum number of colors in the color palette
    mode {str} type of colors to return, one of ['rgb', 'hex', 'ansi']
    """
    assert mode in ['rgb', 'hex', 'ansi']

    if n is None:
        cmap_mpl = matplotlib.cm.get_cmap(palette_name)
    else:
        cmap_mpl = matplotlib.cm.get_cmap(palette_name, n)

    cmap = dict(rgb=OrderedDict(), hex=OrderedDict(), ansi=OrderedDict())

    for i in range(cmap_mpl.N):
        rgb = cmap_mpl(i)[:3]
        hex = matplotlib.colors.rgb2hex(rgb)
        ansi = colr.color('', fore=hex)
        cmap['rgb'].update({rgb: None})
        cmap['hex'].update({hex: None})
        cmap['ansi'].update({ansi: None})

    target = [x for x, _ in cmap[mode].items()]

    if isinstance(n, int):
        if n > len(target):
            rep = int(np.floor(n / len(target)))
            target = list(itertools.chain.from_iterable(itertools.repeat(x, rep) for x in target))
            target += [target[-1]] * (n - len(target))

    return target


def rename_dict_keys(dct: dict, key_dict: dict):
    """
    Rename dictionary keys using a `key_dict` mapping.
    """
    for k, v in key_dict.items():
        if k in dct.keys():
            dct[v] = dct.pop(k)

    return dct


# Verbosity ---------------

def print_apple_ascii_art(by_line: bool=False, by_char: bool=False, sleep: int=0):
    """
    Print Apple WWDC 2016 ASCII artwork logo.
    """
    ascii_string = """                                  -·\n                              _/=\:<\n                             .#/*let}\n                           //as\@#:~/\n                          try()|:-./\n                         *~let:>@f#\n                         </>#@~*/\n                        (+!:~/+/\n                        /={+|\n          _.:+*as=._           _.]@~let[._\n       .*()/if{@[[-#>\=.__.<>/#{*+/@*/for=*~.\n      /-(#]:.(var/@~as/@</>\]=/<if[/*:/<try@\~\n     [:/@#</>}#for=\>.<:try#>=\*.if(var<<.+_:#(=.\n   #do()=*:.>as//@[]-./[#=+)\(var/@<>[]:-##~/*>\n  =*:/([<.//>*~/]\+/_/([\<://:_*try/<:#if~do-:\n @#/*-:/#do.i@var=\<)]#>/=\>\<for#>|*:try=\"</\n :/./@#[=#@-asl#:/-i@if.>#[.)=*>/let\{\}</):\~\n(@+_let#do/.@#=#>[/]#let=#or@\=<()~if)*<)\)\nfor):/=]@#try:</=*;/((+do_{/!\\"(@-/((:@>).*}\n/@#:@try*@!\\as=\>_@.>#+var>_@=>#+-do)=+@#>(\n{}:/./@#=do]>/@if)=[/[!\<)#)try+*:~/#).=})=\ntry@#_<(=<i>do#.<}@#}\\=~*:/().<))_+@#()+\>\n *:#for@:@>):/#<\=*>@\\var_}#|[/@*-/.<:if#/-\\\n =<)=~\(-for>ii@if*=*+#as\<)*:#for@f#)try+}).\n [for()=.[#in=*:as=\>_@-.>#do/:/([+var)=+@#]]=\n  /@[as:=\+@#]=:/let[(=\<_)</@->#for()=))#>in>)_\n  *)\{}/*<var/(>;<+/:do#/-)<\(:as/>)(})_+=<(for+=\.\n   do=~\@#=\><<-))_|@#(])/)_+@let]:[+#\=@/if[#()[=\n    =<]).if|/.=*@var<@:/(-)=*:/#)=*>@#var(<(]if):*\n    {/+_=@#as}#:/-i@if>in=@#{#in=>()@>](@#<{:})->\n     \.=let_@<)#)_=\<~#_)@}+@if#-[+#\|=@#~try/as\n       var<:))+-ry-#»+_+=)>@#>()<?>var)=~<+.-/\n        +@>#do(as)*+[#]=:/(/#\<)if).+let:@(.#\"\n         {}</().try()##/as<){*-</>}](as*>-/<\n           <()if}*var(<>.-\"_\"~.let>#[.)=*>/\n             {}<as:\"            \"*)}do>\n"""

    if by_line or by_char:
        if by_line and by_char:
            logger.warn('Both `by_line` and `by_char` specified. Prioritizing `by_line`.')

        if by_line:
            lines = ascii_string.split('\n')
            for line in lines:
                print(line)
                if sleep > 0:
                    time.sleep(sleep)

        elif by_char:
            for char in ascii_string:
                print(char, end='', flush=True)
                if sleep > 0:
                    time.sleep(sleep)
    else:
        print(ascii_string)


class Verbose(object):
    """
    Handle verbose printing to console for pydoni-cli commands. Has advantage of accepting
    a 'verbose' parameter, then not printing if that is False, similar to logging behavior.
    """
    def __init__(self, verbose: bool=True, debug: bool=False, timestamp: bool=False):
        self.verbose = verbose
        self.debug_flag = debug
        self.timestamp = timestamp
        self.pbar = None

    def echo(self, *args, **kwargs):
        if self.verbose:
            echo(*args, **kwargs)

    def debug(self, *args, **kwargs):
        if self.debug_flag:
            kwargs['level'] = 'debug'
            echo(*args, **kwargs)

    def info(self, *args, **kwargs):
        if self.verbose:
            kwargs['level'] = 'info'
            echo(*args, **kwargs)

    def warn(self, *args, **kwargs):
        if self.verbose:
            kwargs['level'] = 'warn'
            echo(*args, **kwargs)

    def error(self, *args, **kwargs):
        if self.verbose:
            kwargs['level'] = 'error'
            echo(*args, **kwargs)

    def line_break(self):
        if self.verbose:
            print()

    def section_header(self, string: str, time_in_sec: int=None, round_digits: int=2):
        """
        Print STDOUT verbose section header and optionally print the estimated time
        that the following section of code is expected to take
        """
        header = click.style(string, fg='white', bold=True)

        # If time in seconds is given, augment header to incorporate estimated time
        if isinstance(time_in_sec, int) or isinstance(time_in_sec, float):
            # Get estimated time as dictionary
            est_time = fmt_seconds(time_in_sec=time_in_sec, units='auto', round_digits=round_digits)
            header = advanced_strip(f"""
            {header}
            {click.style('->', fg='white', bold=True)}
            Est. time
            {click.style(str(est_time['value']) + ' ' + est_time['units'], fg='yellow', bold=True)}
            """)

        echo(header)

    def program_complete(self,
                         msg: str='Program complete',
                         emoji_string: str=':rocket:',
                         start_ts: typing.Union[float, datetime.datetime]=None):
        """
        Print 'program complete' message intended to be use at script or program completion.
        """
        if self.verbose:
            emoji_string = ':' + emoji_string.replace(':', '') + ':'
            emoji_string = emojize(emoji_string, use_aliases=True)

            if isinstance(start_ts, datetime.datetime) or isinstance(start_ts, datetime.datetime):
                if isinstance(start_ts, datetime.datetime):
                    end_ts = datetime.datetime.now()
                    diff_in_seconds = (end_ts - start_ts).microseconds / 100000
                elif isinstance(start_ts, datetime.datetime):
                    end_ts = time.time()
                    diff_in_seconds = end_ts - start_ts

                timediff = fmt_seconds(end_ts - start_ts, units='auto', round_digits=2)
                elapsed_time = f"{timediff['value']} {timediff['units']}"
                elapsed_time = 'Elapsed time: ' + elapsed_time + ' '
            else:
                elapsed_time = ''

            msg = f'\n[ {msg} {emoji_string} {elapsed_time}]'
            print(msg)

    def pbar_init(self, *args, **kwargs):
        if self.verbose:
            self.pbar = tqdm(*args, **kwargs)

    def pbar_update(self, n):
        if self.verbose:
            self.pbar.update(n)

    def pbar_write(self, msg: str, refer_debug: bool=False):
        """
        Write to `self.pbar`. If `refer_debug` is True, then only write if `self.debug_flag`
        is also True. Otherwise, simply write if `self.verbose` is True. This functionality
        is useful when writing from the progress bar is desired only in debug mode, but
        not necessarily in verbose mode.
        """
        if refer_debug:
            if self.debug_flag:
                tqdm.write(msg)
        else:
            if self.verbose:
                tqdm.write(msg)

    def pbar_close(self):
        if self.verbose:
            self.pbar.close()

    def pbar_log_inline(self, msg_lst):
        """
        Print list of strings below TQDM progress bar.
        """
        for i, m in enumerate(msg_lst, 1):
            trange(1, desc=str(m), position=i, bar_format='{desc}')


def echo(msg: str,
         indent: int=0,
         timestamp: bool=False,
         level: str='T',
         arrow: str=None,
         **kwargs):
    """
    Update stdout with custom message and many custom parameters including indentation,
    timestamp, warning/error message, text styles, and more!

    msg {str} message to print to console
    indent {int} indentation level of message printed to console
    sleep {int} number of seconds to pause program after printing message
    timestamp {bool} print datetimestamp preceding message
    return_str {bool} return string instead of printing
    arrow {str} color of arrow to display before message
    """
    # Save original message before any editing is done if the message will be used in a
    # macOS notification

    msg = click.style(msg, **kwargs)
    ts = systime(as_string=True) + ' ' if timestamp else ''
    arrow_str = click.style(' ==> ', fg=arrow, bold=True) if arrow else ''

    # Add preceding colored string for specified keyword args
    letter_map = dict(SUCCESS='S',
                      TEXT='T',
                      DEBUG='D',
                      INFO='I',
                      WARN='W',
                      ERROR='E',
                      FATAL='F')

    level = level.upper()
    letter = letter_map[level]
    if letter in ['D', 'I', 'W', 'E']:
        # Classic logging levels
        prefix = f'[{ts}{letter}]'
    else:
        # Custom logging levels
        custom_level_map = dict(SUCCESS=f'{level}: ', TEXT= '', FATAL=f'{level}: ')
        custom_level_str = custom_level_map[level]
        if timestamp:
            prefix = f'[{ts.strip()}]{custom_level_str}'
        else:
            prefix = f'{custom_level_str}'

    color_map = dict(S='green', T='white', D='white', I='white', W='yellow', E='red', F='red')
    prefix_colorized = click.style(prefix, fg=color_map[letter])

    indent_str = '  ' * indent

    msg = str(msg)
    print(f'{prefix_colorized}{indent_str}{arrow_str}{msg}')


def print_columns(lst, ncol: int=2, delay: int=None):
    """
    Print a list as side-by-side columns.
    """
    def chunks(lst, chunk_size):
        """
        Split a list into a list of lists.

        lst {list} list to split

        chunk_size {int} size of chunks

        """
        for i in range(0, len(lst), chunk_size):
            yield lst[i:i + chunk_size]

    lstlst = list(chunks(lst, ncol))
    col_width = max(len(word) for row in lstlst for word in row) + 2

    for row in lstlst:
        print(''.join(word.ljust(col_width) for word in row))

        if delay is not None:
            if delay > 0:
                time.sleep(delay)


def stabilize_postfix(key, max_len: int=20, fillchar: str='•', side: str='right'):
    """
    Create "stabilized" postfix (of consistent length) to be fed into
    a tqdm progress bar. This ensures that the postfix is always of
    a certain length, which causes the tqdm progress bar to be stable
    rather than moving left to right when keys of length smaller
    than `max_len` are encountered.

    key {str} string to set as postfix
    max_len {int} length of postfix
    fillchar {str} character to fill any spaces on the left with
    side {str} which side of postfix substring to keep, one of ['left', 'right']
    """
    if side == 'left':
        postfix = key[0:max_len].ljust(max_len, fillchar)
    elif side == 'right':
        postfix = key[-max_len:].rjust(max_len, fillchar)

    m = re.match(r'^ +', postfix)
    if m:
        leading_spaces = m.group(0)
        postfix = re.sub(r'^ +', fillchar * len(leading_spaces), postfix)

    m = re.match(r' +$', postfix)
    if m:
        trailing_spaces = m.group(0)
        postfix = re.sub(r'^ +', fillchar * len(trailing_spaces), postfix)

    return postfix


# User prompting ---------------

def user_select_from_list(lst: list,
                          indent: int=0,
                          msg: str=None,
                          adjustment: int=0,
                          valid_opt: list=None,
                          allow_range: bool=True,
                          return_idx: bool=False,
                          noprint: bool=False):
    """
    Prompt user to make a selection from a list. Supports comma- and hyphen-separated selection.

    Example:
        A user may select elements from a list as:
        1-3, 5, 10-15, 29  ->  [1,2,3,5,10,11,12,13,14,15,29]

    lst {list} list of items to select from
    indent {int} indentation level of all items of `lst`
    msg {str} custom message to print instead of default
    adjustment {int} numeric adjust for enumerated display list
    valid_opt {list} list of valid options, defaults to `lst`
    allow_range {bool} allow user to make multiple selections using commas and/or hyphens
    return_idx {bool} return index of selections in `lst` instead of `lst` items
    noprint {bool} do not print `lst` to console
    """
    def get_valid_opt(lst, adjustment=1):
        """
        Build a numeric list in the format of:

            [
                0 + adjustment,
                1 + adjustment,
                2 + adjustment,
                ...
                len(lst)-1 + adjustment
            ]
        """
        valid_opt = []

        for i, item in enumerate(lst):
            valid_opt.append(i + adjustment)

        return valid_opt

    def print_lst(lst, indent, adjustment=1):
        """
        Print an enumerated list to console.
        """
        tab = '  ' * indent
        for i, item in enumerate(lst):
            print(f'{tab}({str(i + adjustment)}) {item}')

    def define_msg(msg, allow_range):
        """
        Build a message string to print along with the printed list.
        """
        if msg is None:
            if allow_range is True:
                msg = 'Please make a selection (hyphen-separated range ok)'
            else:
                msg = 'Please make a single selection'

        return msg

    def parse_numeric_input(uin_raw, valid_opt, allow_range, silent=False):
        """
        Parse user numeric input to list. If allow_range is False, then input
        must be a single digit. If not, then user may enter input with hyphen(s)
        and comma(s) to indicate different slices of a list.

        Example:
            From a list of [0, 1, 2, 3, 4, 5] a user might enter
            '0-2,4', which should be translated as [0, 1, 2, 4].
            This function will then return [0, 1, 2, 4].

        uin_raw {str} user raw character input
        allow_range {bool} allow_range parent funtion flag
        silent {bool} suppress error messages and just return False if invalid entry entered
        """
        def error_func(msg):
            """
            Print string on invalid input, but do not raise an error.
            """
            echo(msg, error=True)

        # Test that input is valid mix of digits, hyphens and commas only
        if not re.match(r'^(\d|-|,)+$', uin_raw):
            if not silent:
                echo('Input must consist of digits, hyphens and/or commas only', error=True)

            return False

        if allow_range:
            uin_raw = uin_raw.split(',')
            out = []

            for x in uin_raw:
                if '-' in x:

                    start = x.split('-')[0]
                    if start.strip().isdigit():
                        start = int(start)
                    else:
                        if not silent:
                            echo(f"'Start' component '{start}' of hyphen-separated range unable to be parsed", error=True)

                        return False

                    stop = x.split('-')[1]
                    if stop.strip().isdigit():
                        stop = int(stop) + 1
                    else:
                        if not silent:
                            echo(f"'Stop' component '{stop}' of hyphen-separated range unable to be parsed", error=True)

                        return False

                    if start >= stop:
                        if not silent:
                            echo(f"Invalid range '{x}'. 'Start' must be >= 'stop'", error=True)

                        return False

                    out.append(list(range(start, stop)))

                elif x.strip().isdigit():
                    out.append([int(x)])

                else:
                    if not silent:
                        echo(f"Component '{str(x)}' could not in valid format", error=True)

                    return False

            out = list(set([item for sublist in out for item in sublist]))

            oos = []
            for x in out:
                if x not in valid_opt:
                    oos.append(x)

            if len(oos):
                if not silent:
                    error_func(f"Value{'s' if len(oos) > 1 else ''} {str(oos)} out of valid range {str(valid_opt)}")

                return False

            return out

        else:
            if uin_raw.strip().isdigit():
                return [int(uin_raw)]
            else:
                return False

    if not noprint:
        print_lst(lst, indent, adjustment)

    valid_opt = get_valid_opt(lst, adjustment) if not valid_opt else valid_opt
    msg = define_msg(msg, allow_range)

    sel = False
    while sel is False:
        uin_raw = get_input(msg)
        sel = parse_numeric_input(uin_raw, valid_opt, allow_range)

    if return_idx:
        return sel[0] if len(sel) == 1 else sel
    else:
        out = [x for i, x in enumerate(lst) if i + adjustment in sel]
        return out[0] if len(out) == 1 else out


def user_select_from_list_inq(lst: list, msg: str='Select an option'):
    """
    Use PyInquirer module to prompt user to select an item or items from a list.
    """
    style = inq.style_from_dict({
        inq.Token.QuestionMark: '#E91E63 bold',
        inq.Token.Selected: '#673AB7 bold',
        inq.Token.Instruction: '',
        inq.Token.Answer: '#2196f3 bold',
        inq.Token.Question: '',
    })

    question = [{
        'type': 'list',
        'name': 'option',
        'message': msg,
        'choices': lst,
    }]

    selection = inq.prompt(question)['option']

    return selection


def get_input(msg: str='Enter input', mode: str='str', indicate_mode: bool=False):
    """
    Get user input, optionally of specified format.

    msg {str} message to print to console
    mode {str} apply filter to user input, one of ['bool', 'date', 'int', 'float',
               'str', 'file', 'filev', 'dir', 'dirv']. 'filev' and 'dirv'
               options are {exists}'file'/'dir' with an added layer of validation, to
    indicate_mode {bool} print type of anticipated datatype with message
    """
    assert mode in ['str', 'bool', 'date', 'int', 'float', 'file', 'filev', 'dir', 'dirv']

    add_colon = lambda x: x + ': '
    add_clarification = lambda x, clar: x + ' ' + clar

    # Add suffix based on `mode`
    msg = re.sub(r': *$', '', msg).strip()
    if mode == 'bool':
        msg = add_clarification(msg, '(y/n)')
    elif mode == 'date':
        msg = add_clarification(msg, '(YYYY-MM-DD)')
    if indicate_mode:
        msg = add_clarification(msg, '{%s}' % mode)
    msg = add_colon(msg)

    uin_raw = input(msg)

    if mode == 'bool':
        while not test_value(uin_raw, 'bool'):
            uin_raw = input("Must enter 'y' or 'n': ")
        if uin_raw.lower() in ['y', 'yes']:
            return True
        else:
            return False
    elif mode == 'date':
        while not test_value(uin_raw, 'date') and uin_raw != '':
            uin_raw = input("Must enter valid date in format 'YYYY-MM-DD': ")
    elif mode == 'int':
        while not test_value(uin_raw, 'int'):
            uin_raw = input('Must enter integer value: ')
        uin_raw = int(uin_raw)
    elif mode == 'float':
        while not test_value(uin_raw, 'float'):
            uin_raw = input('Must enter float value: ')
    elif mode in ['file', 'filev', 'dir', 'dirv']:
        uin_raw = os.path.expanduser(uin_raw.strip())
        if mode == 'filev':
            while not os.path.isfile(uin_raw):
                uin_raw = input('Must enter existing file: ')
        elif mode == 'dirv':
            while not os.path.isdir(uin_raw):
                uin_raw = input('Must enter existing directory: ')

    return uin_raw


def get_input_inq(msg: str='Enter input', mode: str='str', indicate_mode: bool=False):
    """
    Get user input for single line using PyInquirer module.

    msg {str} message to print to console
    mode {str} apply filter to user input, one of ['bool', 'date', 'int', 'float',
               'str', 'file', 'filev', 'dir', 'dirv']. 'filev' and 'dirv' options
               are 'file {str}/'dir' with an added layer of validation, to ensure the file/dir exists
    indicate_mode {bool} print type of anticipated datatype with message
    """
    assert mode in ['str', 'bool', 'date', 'int', 'float', 'file', 'filev', 'dir', 'dirv']

    def define_validator(mode):
        """
        Define 'InqValidator' class based on 'mode'.

            mode {str}'mode' parameter passed into parent

        """

        testfunc = lambda value: test_value(value, mode)

        class InqValidator(inq.Validator):
            def validate(self, document):
                if not testfunc(document.text):
                    raise inq.ValidationError(
                        message="Please enter a valid value of type '%s'" % mode,
                        cursor_position=len(document.text))

        return InqValidator

    add_colon = lambda x: x + ': '
    add_clarification = lambda x, clar: x + ' ' + clar

    # Add suffix based on `mode`
    msg = re.sub(r': *$', '', msg).strip()
    if mode == 'bool':
        msg = add_clarification(msg, '(y/n)')
    elif mode == 'date':
        msg = add_clarification(msg, '(YYYY-MM-DD)')
    if indicate_mode:
        msg = add_clarification(msg, '{%s}' % mode)

    msg = add_colon(msg)

    question = {
        'type': 'input',
        'name': 'TMP',
        'message': msg
    }

    if mode in ['bool', 'date', 'int', 'float', 'file', 'filev', 'dir', 'dirv']:
        validator = define_validator(mode)
        question['validate'] = validator

    question = [question]
    answer = inq.prompt(question)['TMP']

    if mode == 'int':
        answer = int(answer)
    elif mode == 'float':
        answer = float(answer)
    elif mode == 'bool':
        if answer.lower() in ['y', 'yes', 'true', 't']:
            answer = True
        elif answer.lower() in ['n', 'no', 'false', 'f']:
            answer = False
    elif mode in ['file', 'filev', 'dir', 'dirv']:
        answer = os.path.expanduser(answer)

    return answer


def continuous_prompt(msg: str, mode='str', indicate_mode: bool=False, use_inq: bool=False):
    """
    Continuously prompt the user for input until '' is entered.

    msg {str} message to print to console
    mode {str} apply filter to user input, one of ['bool', 'date', 'int', 'float',
               'str', 'file', 'filev', 'dir', 'dirv']. 'filev' and 'dirv'
               options are {exists}'file'/'dir' with an added layer of validation, to
    indicate_mode {bool} print type of anticipated datatype with message
    use_inq {bool} use `get_input_inq()` instead of `get_input()`
    """
    uin = 'TMP'
    all_input = []

    while uin > '':
        if use_inq:
            uin = get_input_inq(msg=msg, mode=mode, indicate_mode=indicate_mode)
        else:
            uin = get_input(msg=msg, mode=mode, indicate_mode=indicate_mode)

        if uin > '':
            all_input.append(uin)

    return all_input

# Database operations ---------------

class Postgres(object):
    """
    Interact with PostgreSQL database through Python.
    """
    def __init__(self, pg_user: str=None, pg_dbname: str=None):
        self.dbuser = pg_user
        self.dbname = pg_dbname
        self.dbcon = self.connect()

        self.null_equivalents = ['nan', 'n/a', 'null', 'none', '']
        self.null_equivalents = self.null_equivalents + [x.upper() for x in self.null_equivalents]

    def read_pgpass(self):
        """
        Read ~/.pgpass file if it exists and extract Postgres credentials. Return tuple
        in format: `hostname, port, pg_dbname, pg_user, pg_pass`
        """
        pgpass_file = os.path.expanduser('~/.pgpass')
        if os.path.isfile(pgpass_file):
            with open(pgpass_file, 'r') as f:
                pgpass_contents = f.read().split(':')

            # Ensure proper ~/.pgpass format, should be a tuple of length 5
            assert len(pgpass_contents) == 5, \
                'Invalid ~/.pgpass contents format. Should be `hostname:port:pg_dbname:pg_user:pg_pass`'

            return pgpass_contents

    def connect(self):
        """
        Connect to Postgres database and return the database connection.
        """
        if self.dbuser is None and self.dbname is None:
            # Attempt to parse ~/.pgpass file
            logger.warn('No credentials supplied, attempting to parse ~/.pgpass file')
            pgpass_contents = self.read_pgpass()
            if pgpass_contents is not None:
                hostname, port, pg_dbname, pg_user, pg_pass = pgpass_contents

                if pg_dbname > '' and pg_user > '':
                    self.dbuser = pg_user
                    self.dbname = pg_dbname
            else:
                raise Exception(pydoni.advanced_strip("""
                Could not connect to Postgres database! Check the Postgres credentials you
                supplied and/or your ~/.pgpass file if it exists."""))

        con_str = f'postgresql://{self.dbuser}@localhost:5432/{self.dbname}'
        return sqlalchemy.create_engine(con_str)

    def execute(self, sql: str, logfile: typing.Union[str, pathlib.Path]=None, log_ts: bool=False, progress: bool=False):
        """
        Execute a SQL string or a list of SQL statements.
        """
        write_log = False if logfile is None else True
        if write_log:
            logger.info(f'Writing SQL query log to file "{logfile}"')

        sql = ensurelist(sql)

        with self.dbcon.begin() as con:
            if progress:
                pbar = tqdm(total=len(sql), unit='query')

            for stmt in sql:
                con.execute(sqlalchemy.text(stmt))

                if write_log:
                    with open(logfile, 'a') as f:
                        entry = stmt + '\n'

                        if log_ts:
                            entry = systime(as_string=True) + ' ' + entry

                        f.write(entry)

                if progress:
                    pbar.update(1)

        if progress:
            pbar.close()

    def read_sql(self, sql: str, simplify: bool=True):
        """
        Execute SQL and read results using Pandas, optionally simplify result to a Series if
        the result is a single-column dataframe.
        """
        res = pd.read_sql(sql, con=self.dbcon)

        if res.shape[1] == 1:
            if simplify:
                logger.info(f'Simplifying result data to pd.Series, length: {str(len(res))}')
                res = res.iloc[:, 0]

        return res

    def get_table_name(self, schema_name: str=None, table_name: str=None):
        """
        Concatenate a schema and table names. Require that `table_name` is supplied,
        but `schema_name` may be blank (i.e. in the case of querying pg_stat, or another
        builtin table that does not have an explicit corresponding schema.)
        """
        assert table_name is not None, 'Must supply `table_name`'

        if schema_name is None:
            return table_name
        else:
            return schema_name + '.' + table_name

    def validate_dtype(self, schema_name: str, table_name: str, col: str, val: Any):
        """
        Query database for datatype of value and validate that the Python value to
        insert to that column is compatible with the SQL datatype.
        """
        if table_name.startswith('pg_'):
            # Builtin table housed in `pg_catalog` schema, but no schema required to query from it
            schema_name = 'pg_catalog'

        table_schema_and_name = self.get_table_name(schema_name, table_name)
        full_col = table_schema_and_name + '.' + col

        infoschema = self.infoschema(infoschema_table='columns')[['table_schema', 'table_name', 'column_name', 'data_type', 'is_nullable']]
        infoschema = infoschema.loc[
            (infoschema['table_schema']==schema_name)
            & (infoschema['table_name']==table_name)
            & (infoschema['column_name']==col)
        ]

        assert len(infoschema), f'Nonexistent column {full_col}'
        infoschema = infoschema.squeeze().to_dict()

        if val == 'NULL' or val is None:
            if bool(infoschema['is_nullable']) is True:
                return True
            else:
                logger.error(f"Value 'NULL' (dtype: {val.__class__.__name__}) not allowed for column {full_col}")
                return False

        # Check that input value datatype matches queried table column datatype
        dtype = self.col_dtypes(schema_name, table_name)[col]
        dtype_map = {
            'bigint': 'int',
            'int8': 'int',
            'bigserial': 'int',
            'serial8': 'int',
            'integer': 'int',
            'int': 'int',
            'int4': 'int',
            'smallint': 'int',
            'int2': 'int',
            'double precision': 'float',
            'float': 'float',
            'float4': 'float',
            'float8': 'float',
            'numeric': 'float',
            'decimal': 'float',
            'character': 'str',
            'char': 'str',
            'character varying': 'str',
            'varchar': 'str',
            'text': 'str',
            'date': 'str',
            'timestamp': 'str',
            'timestamp with time zone': 'str',
            'timestamp without time zone': 'str',
            'name': 'str',
            'boolean': 'bool',
            'bool': 'bool',
        }

        # Get python equivalent of SQL column datatype according to dtype_map above
        python_dtype = [v for k, v in dtype_map.items() if dtype in k]

        if not len(python_dtype):
            known_python_datatypes = list(set([v for k, v in dtype_map.items()]))
            logger.error(advanced_strip(f"""
            Unable to match SQL column '{full_col}' datatype {dtype} to any known Python
            datatypes {known_python_datatypes}"""))
            return False
        else:
            python_dtype = python_dtype[0]

        true_python_dtype = type(val).__name__

        # Prepare message to be used in event of incompatible datatypes
        msg = f"""Incompatible datatypes! SQL column {full_col} has type
        `{dtype}`, and Python value `{str(val)}` is of type `{val.__class__.__name__}`."""

        # Begin validation
        if true_python_dtype in ['date', 'datetime']:
            if 'date' in dtype or 'timestamp' in dtype:
                return True
            else:
                return False

        elif python_dtype == 'bool':
            if isinstance(val, bool):
                return True
            else:
                if isinstance(val, str):
                    if val.lower() in ['t', 'true', 'f', 'false']:
                        return True

        elif python_dtype == 'int':
            if isinstance(val, int):
                return True
            else:
                if isinstance(val, str):
                    try:
                        int(val)
                        return True
                    except:
                        pass

        elif python_dtype == 'float':
            if isinstance(val, float):
                return True
            else:
                if val == 'inf':
                    pass
                try:
                    float(val)
                    return True
                except:
                    pass

        elif python_dtype == 'str':
            if isinstance(val, str):
                return True
        else:
            return True

        # If this function hasn't returned True by now, then datatype validation must have failed
        logger.error(msg)
        return False

    def infoschema(self, infoschema_table: str):
        """
        Query from information_schema. Vanilla call to this function executes:

            select * from information_schema.{columns_or_tables};

        Can also set `infoschema_table` to "tables", or any other subdivision of Postgres'
        information schema.
        """
        sql = f'select *\nfrom information_schema.{infoschema_table}'
        df = self.read_sql(sql, simplify=False)
        logger.info(f'Retrieved information_schema.{infoschema_table}')

        # Format known column datatypes
        bool_cols = ['is_nullable']
        for bcol in bool_cols:
            if bcol in df.columns:
                df[bcol] = df[bcol].map(lambda x: dict(YES=True, NO=False)[x])

        return df

    def build_update(self,
                     schema_name,
                     table_name,
                     pkey_name,
                     pkey_value,
                     columns,
                     values,
                     validate=True,
                     newlines=False):
        """
        Construct a SQL UPDATE statement.

        By default, this method will:

            - Attempt to coerce a date value to proper format if the input value is detect_dtype
              as a date but possibly in the improper format. Ex: '2019:02:08' -> '2019-02-08'
            - Quote all values passed in as strings. This will include string values that
              are coercible to numerics. Ex: '5', '7.5'.
            - Do not quote all values passed in as integer or boolean values.
            - Primary key value is quoted if passed in as a string. Otherwise, not quoted.

        schema {str} name of schema
        table {str} SQL table name
        pkey_name {str} name of primary key in table
        pkey_value {str} value of primary key for value to update
        columns {list} columns to consider in UPDATE statement
        values {list} values to consider in UPDATE statement
        validate {bool} validate that each value may be inserted to destination column
        newlines {true} add newlines to query string to make more human-readable
        """
        columns = ensurelist(columns)
        values = ensurelist(values)
        if len(columns) != len(values):
            raise Exception("Parameters `columns` and `values` must be of equal length")

        pkey_value = self.__single_quote__(pkey_value)
        lst = []

        for col, val in zip(columns, values):
            if validate:
                test = self.validate_dtype(schema_name, table_name, col, val)
                if not test:
                    dtype = type(val).__name__
                    raise Exception(f'Dtype mismatch. Value: {val}, dtype: {dtype}, column: {col}')

            if str(val).lower() in self.null_equivalents:
                val = 'NULL'
            elif test_value(val, 'bool') or test_value(val, 'int') or test_value(val, 'float'):
                pass
            else:
                # Assume string
                val = self.__single_quote__(val)

            if newlines:
                lst.append(f'\n    "{col}"={str(val)}')
            else:
                lst.append(f'"{col}"={str(val)}')

        sql = ["UPDATE {}", "SET {}", "WHERE {} = {}"]
        if newlines:
            lst[0] = lst[0].strip()
            sql = '\n'.join(sql)
        else:
            sql = ' '.join(sql)

        table_schema_and_name = self.get_table_name(schema_name, table_name)
        return sql.format(table_schema_and_name,
                          ', '.join(lst),
                          '"' + pkey_name + '"',
                          pkey_value)

    def build_insert(self, schema_name: str, table_name: str, columns: list, values: list, validate: bool=False, newlines: bool=False):
        """
        Construct SQL INSERT statement.
        By default, this method will:

            - Attempt to coerce a date value to proper format if the input value is
              detect_dtype as a date but possibly in the improper format.
              Ex: '2019:02:08' -> '2019-02-08'
            - Quote all values passed in as strings. This will include string values
              that are coercible to numerics. Ex: '5', '7.5'.
            - Do not quote all values passed in as integer or boolean values.
            - Primary key value is quoted if passed in as a string. Otherwise, not quoted.

        schema {str} name of schema
        table {str} SQL table name
        columns {list} columns to consider in UPDATE statement
        values {list} values to consider in UPDATE statement
        validate {bool} validate that each value may be inserted to destination column
        newlines {true} add newlines to query string to make more human-readable
        :return: SQL UPDATE statement
        :rtype: str
        """
        columns = ensurelist(columns)
        values = ensurelist(values)
        if len(columns) != len(values):
            raise Exception("Parameters `columns` and `values` must be of equal length")

        lst = []
        for col, val in zip(columns, values):
            if validate:
                test = self.validate_dtype(schema_name, table_name, col, val)
                if not test:
                    dtype = type(val).__name__
                    raise Exception(advanced_strip(f"""Value '{val}' (dtype: {dtype})
                    is incompatible with column '{col}' """))

            if str(val).lower() in self.null_equivalents:
                val = 'null'

            elif test_value(val, 'bool') or test_value(val, 'int') or test_value(val, 'float'):
                pass
            else:
                # Assume string, handle quotes
                val = self.__single_quote__(val)

            lst.append(val)

        values_final = ', '.join(str(x) for x in lst)
        values_final = values_final.replace("'null'", 'null')
        columns = ', '.join(['"' + x + '"' for x in columns])

        table_schema_and_name = self.get_table_name(schema_name, table_name)
        sql = ['insert into {table_schema_and_name} ({columns})', 'values ({values_final})']
        sql = '\n'.join(sql) if newlines else ' '.join(sql)

        return sql.format(**locals())

    def build_delete(self, schema_name: str, table_name: str, pkey_name: str, pkey_value:Any, newlines:bool=False):
        """
        Construct SQL DELETE FROM statement.
        """
        pkey_value = self.__single_quote__(pkey_value)
        table_schema_and_name = self.get_table_name(schema_name, table_name)
        sql = ['delete from {}', 'where {} = {}']
        sql = '\n'.join(sql) if newlines else ' '.join(sql)

        return sql.format(table_schema_and_name, pkey_name, pkey_value)

    def col_names(self, schema_name: str, table_name: str) -> list:
        """
        Get column names of table as a list.
        """
        df_cols = self.infoschema(infoschema_table='columns')[['table_schema', 'table_name', 'column_name']]

        df_cols = df_cols.loc[(df_cols['table_schema'] == schema_name)
                              & (df_cols['table_name'] == table_name)]

        cols = df_cols['column_name'].tolist()
        return cols

    def col_dtypes(self, schema_name: str, table_name: str) -> list:
        """
        Get column datatypes of table as a dictionary.
        """
        infoschema = self.infoschema(infoschema_table='columns')
        infoschema = infoschema.loc[
            (infoschema['table_schema']==schema_name)
            & (infoschema['table_name']==table_name)
        ]
        return infoschema.set_index('column_name')['data_type'].to_dict()

    def read_table(self, schema_name: str, table_name: str) -> list:
        """
        Read an entire SQL table as a dataframe.
        """
        df = self.read_sql(f'select * from "{schema_name}"."{table_name}"')
        logger.info(f"Read dataframe {schema_name}.{table_name}, shape: {df.shape}")
        return df

    def dump(self, backup_dir: typing.Union[str, pathlib.Path]):
        """
        Wrap `pg_dump` and save an entire database contents to a directory.
        """
        backup_dir = os.path.expanduser(backup_dir)
        logger.info(f'Dumping database {self.dbname} to "{backup_dir}"')

        bin = find_binary('pg_dump', abort=True)
        outfile = f'{backup_dir}/{self.dbname}.sql'
        cmd = f'{bin} --user {self.dbuser} {self.dbname} > "{outfile}"'

        out = syscmd(cmd)
        if not isinstance(out, int):
            out = out.decode('utf-8')
            if 'FATAL' in out:
                raise Exception(out.strip())

        return outfile

    def dump_tables(self, backup_dir: typing.Union[str, pathlib.Path], sep: str=',', coerce_csv: bool=False):
        """
        Dump each table in database to a textfile with specified separator.

        Source: https://stackoverflow.com/questions/17463299/export-database-into-csv-file?answertab=oldest#tab-top
        """
        db_to_csv = """
        CREATE OR REPLACE FUNCTION db_to_csv(path TEXT) RETURNS void AS $$
        DECLARE
           tables RECORD;
           statement TEXT;
        BEGIN
        FOR tables IN
           SELECT (table_schema || '.' || table_name) AS schema_table
           FROM information_schema.tables t
               INNER JOIN information_schema.schemata s ON s.schema_name = t.table_schema
           WHERE t.table_schema NOT IN ('pg_catalog', 'information_schema')
               AND t.table_type NOT IN ('VIEW')
           ORDER BY schema_table
        LOOP
           statement := 'COPY ' || tables.schema_table || ' TO ''' || path || '/' || tables.schema_table || '.tmpcsv' ||''' DELIMITER ''{sep}'' CSV HEADER';
           EXECUTE statement;
        END LOOP;
        RETURN;
        END;
        $$ LANGUAGE plpgsql;""".format(**locals())
        self.execute(db_to_csv)

        # Execute function, dumping each table to a textfile.
        # Function is used as follows: SELECT db_to_csv('/path/to/dump/destination');
        logger.info(f'Dumping database {self.dbname} to "{backup_dir}" as tables stored as textfiles')
        self.execute(f"select db_to_csv('{backup_dir}')")

        # If coerce_csv is True, read in each file outputted, then write as a quoted CSV.
        # Replace 'sep' if different from ',' and quote each text field.
        if coerce_csv:
            if sep != ',':
                owd = os.getcwd()
                os.chdir(backup_dir)

                # Get tables that were dumped and build filenames
                get_dumped_tables = """
                select (table_schema || '.' || table_name) as schema_table
                from information_schema.tables t
                join information_schema.schemata s
                  on s.schema_name = t.table_schema
                where t.table_schema not in ('pg_catalog', 'information_schema')
                  and t.table_type not in ('view')
                order by schema_table"""
                dumped_tables = self.read_sql(get_dumped_tables).squeeze()

                if isinstance(dumped_tables, pd.Series):
                    dumped_tables = dumped_tables.tolist()
                elif isinstance(dumped_tables, str):
                    dumped_tables = [dumped_tables]

                dumped_tables = [x + '.csv' for x in dumped_tables]

                # Read in each table and overwrite file with comma sep and quoted text values
                for csvfile in dumped_tables:
                    pd.read_csv(csvfile, sep=sep).to_csv(
                        csvfile, quoting=csv.QUOTE_NONNUMERIC, index=False)

                os.chdir(owd)
            else:
                logger.warn('`coerce_csv` is True but desired `sep` is not a comma!')

        # Get tables that were just dumped and return their filenames
        dumped_files_tmpcsv = listfiles(path=backup_dir, ext='tmpcsv', full_names=True)
        dumped_files = []
        for tmpcsvfile in dumped_files_tmpcsv:
            newfilename = os.path.splitext(tmpcsvfile)[0] + '.csv'
            os.rename(tmpcsvfile, newfilename)
            dumped_files.append(newfilename)

        return dumped_files

    def create_schema(self, table_schema: str):
        """
        Create a Postgres schema.
        """
        self.execute(f'create schema {table_schema}')

    def create_table(self, table_schema: str, table_name: str, columnspec: list):
        """
        Create a Postgres table given a schema name, table name and column specification. The
        specification must be in format:

            [
                (col1_name, col1_dtype),
                (col2_name, col2_dtype),
                ...
            ]
        """
        tab_ws = '    '

        columnspec_str = tab_ws + tab_ws.join([col + ' ' + dtype + ',\n' for col, dtype in columnspec]).rstrip('\n,')

        create_table_sql_lst = [
            f'create table {table_schema}.{table_name} (',
            columnspec_str,
            ')',
        ]

        create_table_sql = '\n'.join(create_table_sql_lst)
        self.execute(create_table_sql)

        return True

    def create_table_if_not_exists(self, table_schema: str, table_name: str, columnspec: list):
        """
        Call `self.create_table` if table does not exist.
        """
        if not self.table_exists(table_schema, table_name):
            self.create_table(table_schema, table_name, columnspec)
            return True
        else:
            return False

    def drop_schema(self, table_schema: str, cascade: bool=True):
        """
        Drop a Postgres schema.
        """
        cascade_str = ' cascade' if cascade else ''
        self.execute(f'drop schema {table_schema}{cascade_str}')

    def drop_and_recreate_schema(self, table_schema: str):
        """
        Drop then re-create a Postgres schema
        """
        self.drop_schema(table_schema)
        self.create_schema(table_schema)

    def drop_table(self, table_schema: str, table_name: str):
        """
        Drop a Postgres table.
        """
        self.execute(f'drop table "{table_schema}"."{table_name}"')

    def wipe_table(self, table_schema: str, table_name: str):
        """
        Delete all records in a table.
        """
        if self.table_exists(table_schema, table_name):
            self.execute(f'delete from {table_schema}.{table_name} where 1 = 1')

    def drop_table_if_exists(self, table_schema: str, table_name: str):
        """
        Drop a Postgres table if it exists.
        """
        self.execute(f'drop table if exists "{table_schema}"."{table_name}"')

    def drop_view(self, view_schema: str, view_name: str):
        """
        Drop a Postgres view.
        """
        self.execute(f'drop view "{view_schema}"."{view_name}"')

    def drop_view_if_exists(self, view_schema: str, view_name: str):
        """
        Drop a Postgres view if it exists.
        """
        self.execute(f'drop view if exists "{view_schema}"."{view_name}"')

    def table_exists(self, table_schema: str=None, table_name: str=None):
        """
        Return a boolean indicating whether a table is existent in a Postgres database.
        """
        assert table_name is not None
        tables = self.list_tables(table_schema)
        return table_name in tables['table_name'].tolist()

    def view_exists(self, view_schema: str=None, view_name: str=None):
        """
        Return a boolean indicating whether a view is existent in a Postgres database.
        """
        assert view_name is not None
        views = self.list_views(view_schema)
        return view_name in views['view_name'].tolist()

    def trigger_exists(self, trigger_schema: str=None, trigger_name: str=None):
        """
        Return a boolean indicating whether a trigger is existent in a Postgres database.
        """
        assert trigger_name is not None
        triggers = self.list_triggers(trigger_schema)
        return trigger_name in triggers['trigger_name'].tolist()

    def list_tables(self, table_schema: str=None):
        """
        List tables present in the database connection.
        """
        additional_cond = f"and table_schema = '{table_schema}'" if isinstance(table_schema, str) else ''
        sql = f"""
        select table_schema, "table_name"
        from information_schema.tables
        where table_type = 'BASE TABLE'
          and table_schema <> 'pg_catalog'
          {additional_cond}
        """
        return self.read_sql(sql)

    def list_views(self, view_schema: str=None):
        """
        List views present in the database connection.
        """
        additional_cond = f"and table_schema = '{view_schema}'" if isinstance(view_schema, str) else ''
        sql = f"""
        select
            table_schema as view_schema
            , "table_name" as view_name
        from
            information_schema.views
        where
            table_schema not in ('information_schema', 'pg_catalog')
            {additional_cond}
        order by
            table_schema,
            view_name
        """
        return self.read_sql(sql)

    def list_triggers(self, trigger_schema: str=None):
        """
        List triggers present in the database connection.
        """
        additional_cond = f"and trigger_schema = '{trigger_schema}'" if isinstance(trigger_schema, str) else ''
        sql = f"""
        select
            event_object_schema as table_schema
            , event_object_table as "table_name"
            , trigger_schema
            , trigger_name
            , string_agg(event_manipulation, ',') as "event"
            , action_timing as activation
            , action_condition as "condition"
            , action_statement as definition
        from
            information_schema.triggers
        where
            trigger_schema <> 'pg_catalog'
            {additional_cond}
        group by
            1, 2, 3, 4, 6, 7, 8
        order by
            table_schema
            , "table_name"
        """
        return self.read_sql(sql)

    def __single_quote__(self, val: Any):
        """
        Escape single quotes and put single quotes around value if string value.
        """
        if type(val) not in [bool, int, float]:
            val = str(val).replace("'", "''")
            val = "'" + val + "'"

        return val

# Backend module operations ---------------

def __pydonicli_register__(var_dict):
    """
    Register variable as a part of the 'pydoni' module to be logged to the CLI's backend.
    """
    for key, value in var_dict.items():
        setattr(pydoni, 'pydonicli_' + key, value)


def __pydonicli_declare_args__(var_dict):
    """
    Limit a dictionary, usually `locals()` to exclude modules and functions and thus contain
    only key:value pairs of variables.
    """
    vars_only = {}

    for k, v in var_dict.items():
        dtype = v.__class__.__name__
        if dtype not in ['module', 'function']:
            vars_only[k] = v

    return vars_only
