"""Top-level package for """

__author__ = """Andoni Sooklaris"""
__email__ = 'andoni.sooklaris@gmail.com'
__version__ = '0.1.3'


import click
import colr
import itertools
import logging
import matplotlib
import matplotlib.cm
import numpy as np
import os
import pydonitest
import PyInquirer as inq
import pylab
import re
import subprocess
import threading
import time
from collections import OrderedDict
from datetime import datetime
from dateutil.parser import parse
from dateutil.tz import tzoffset

# from pydonitest import vb


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


def logger_setup(name=__name__, level=logging.DEBUG, equal_width=False):
    """
    Standardize logger setup across pydonitest package.
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


def advanced_strip(string):
    """
    Strip whitespace off a string and replace all instances of >1 space with a single space.
    """
    return re.sub(r'\s+', ' ', string.strip())


def syscmd(cmd, encoding=''):
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


def listfiles(path='.',
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


def listdirs(path='.', pattern=None, full_names=False, recursive=False):
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


def ensurelist(val):
    """
    Accept a string or list and ensure that it is formatted as a list. If `val` is not a list,
    return [val]. If `val` is already a list, return as is.
    """
    return [val] if not isinstance(val, list) else val


def print_apple_ascii_art(by_line=False, by_char=False, sleep=0):
    """
    Print Apple WWDC 2016 ASCII artwork logo.
    """
    ascii_string = """                                  -·\n                              _/=\:<\n                             .#/*let}\n                           //as\@#:~/\n                          try()|:-./\n                         *~let:>@f#\n                         </>#@~*/\n                        (+!:~/+/\n                        /={+|\n          _.:+*as=._           _.]@~let[._\n       .*()/if{@[[-#>\=.__.<>/#{*+/@*/for=*~.\n      /-(#]:.(var/@~as/@</>\]=/<if[/*:/<try@\~\n     [:/@#</>}#for=\>.<:try#>=\*.if(var<<.+_:#(=.\n   #do()=*:.>as//@[]-./[#=+)\(var/@<>[]:-##~/*>\n  =*:/([<.//>*~/]\+/_/([\<://:_*try/<:#if~do-:\n @#/*-:/#do.i@var=\<)]#>/=\>\<for#>|*:try=\"</\n :/./@#[=#@-asl#:/-i@if.>#[.)=*>/let\{\}</):\~\n(@+_let#do/.@#=#>[/]#let=#or@\=<()~if)*<)\)\nfor):/=]@#try:</=*;/((+do_{/!\\"(@-/((:@>).*}\n/@#:@try*@!\\as=\>_@.>#+var>_@=>#+-do)=+@#>(\n{}:/./@#=do]>/@if)=[/[!\<)#)try+*:~/#).=})=\ntry@#_<(=<i>do#.<}@#}\\=~*:/().<))_+@#()+\>\n *:#for@:@>):/#<\=*>@\\var_}#|[/@*-/.<:if#/-\\\n =<)=~\(-for>ii@if*=*+#as\<)*:#for@f#)try+}).\n [for()=.[#in=*:as=\>_@-.>#do/:/([+var)=+@#]]=\n  /@[as:=\+@#]=:/let[(=\<_)</@->#for()=))#>in>)_\n  *)\{}/*<var/(>;<+/:do#/-)<\(:as/>)(})_+=<(for+=\.\n   do=~\@#=\><<-))_|@#(])/)_+@let]:[+#\=@/if[#()[=\n    =<]).if|/.=*@var<@:/(-)=*:/#)=*>@#var(<(]if):*\n    {/+_=@#as}#:/-i@if>in=@#{#in=>()@>](@#<{:})->\n     \.=let_@<)#)_=\<~#_)@}+@if#-[+#\|=@#~try/as\n       var<:))+-ry-#»+_+=)>@#>()<?>var)=~<+.-/\n        +@>#do(as)*+[#]=:/(/#\<)if).+let:@(.#\"\n         {}</().try()##/as<){*-</>}](as*>-/<\n           <()if}*var(<>.-\"_\"~.let>#[.)=*>/\n             {}<as:\"            \"*)}do>\n"""

    if by_line or by_char:
        if by_line and by_char:
            logger.warning('Both `by_line` and `by_char` specified. Prioritizing `by_line`.')

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


def systime(as_string=True, compact=False):
    """
    Get the current datetime, optionally formatted as a string.
    """
    if as_string:
        return datetime.now().strftime('%Y%m%d_%H%M%S' if compact else '%Y-%m-%d %H:%M:%S')
    else:
        assert not compact, 'Cannot set `compact` if returning a datetime object!'
        return datetime.now()


def sysdate(as_string=True, compact=False):
    """
    Get the current date, optionally formatted as a string.
    """
    if as_string:
        return datetime.now().strftime('%Y%m%d' if compact else '%Y-%m-%d')
    else:
        assert not compact, 'Cannot set `compact` if returning a datetime object!'
        return datetime.now().replace(hour=0, minute=0, second=0)


def naturalsort(lst):
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


def user_select_from_list(lst,
                          indent=0,
                          msg=None,
                          adjustment=0,
                          valid_opt=None,
                          allow_range=True,
                          return_idx=False,
                          noprint=False):
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
            vb.echo(msg, error=True)

        # Test that input is valid mix of digits, hyphens and commas only
        if not re.match(r'^(\d|-|,)+$', uin_raw):
            if not silent:
                vb.echo('Input must consist of digits, hyphens and/or commas only', error=True)

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
                            vb.echo(f"'Start' component '{start}' of hyphen-separated range unable to be parsed", error=True)

                        return False

                    stop = x.split('-')[1]
                    if stop.strip().isdigit():
                        stop = int(stop) + 1
                    else:
                        if not silent:
                            vb.echo(f"'Stop' component '{stop}' of hyphen-separated range unable to be parsed", error=True)

                        return False

                    if start >= stop:
                        if not silent:
                            vb.echo(f"Invalid range '{x}'. 'Start' must be >= 'stop'", error=True)

                        return False

                    out.append(list(range(start, stop)))

                elif x.strip().isdigit():
                    out.append([int(x)])

                else:
                    if not silent:
                        vb.echo(f"Component '{str(x)}' could not in valid format", error=True)

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


def user_select_from_list_inq(lst, msg='Select an option'):
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


def fmt_seconds(time_in_sec, units='auto', round_digits=4):
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


def listmode(lst):
    """
    Get the most frequently occurring value in a list.
    """
    return max(set(lst), key=lst.count)


def cap_nth_char(string, n):
    """
    Capitalize character in `string` at zero-indexed position `n`.

    Example:
        >>> cap_nth_char(string='string', n=3, replacement='I')
        'strIng'
    """
    return string[:n] + string[n].capitalize() + string[n+1:]


def replace_nth_char(string, n, replacement):
    """
    Replace character in `string` at zero-indexed position `n` with `replacement`.

    Example:
        >>> replace_nth_char(string='string', n=3, replacement='I')
        'strIng'
    """
    return string[:n] + str(replacement) + string[n+1:]


def insert_nth_char(string, n, char):
    """
    Insert `char` in `string` at zero-indexed position `n`.

    Example:
        >>> insert_nth_char(string='strng', n=3, char='I')
        'strIng'
    """
    return string [:n] + str(char) + string[n:]


def human_filesize(nbytes):
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


def split_at(lst, idx):
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


def duplicated(lst):
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


def test_value(value, dtype, return_coerced_value=False, assertion=False):
    """
    Test if a value is an instance of type `dtype`. May accept a value of any kind.

    Parameter `dtype` must be one of ['bool', 'str', 'string', 'int', 'integer',
    'float', 'date', 'datetime', 'path', 'path exists'].

    Parameter `return_coerced_value` will cause this function to return `value` as type
    `dtype` if possible, and will raise an error otherwise.

    Parameter `assertion` will cause this function to raise an error if `value` cannot be
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
            if assertion: raise e
            else: logger.info(str(e))

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
                if assertion: raise e
                else: logger.info(str(e))

    # Test float
    elif dtype == 'float':
        if isinstance(value, float) or isinstance(value, int):
            coerced_value = float(value)
        elif '.' in str(value):
            try:
                coerced_value = float(value)
            except Exception as e:
                if assertion: raise e
                else: logger.info(str(e))

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


def get_input(msg='Enter input', mode='str', indicate_mode=False):
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


def get_input_inq(msg='Enter input', mode='str', indicate_mode=False):
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

        testfunc = lambda value: test(value, mode)

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


def continuous_prompt(msg, mode='str', indicate_mode=False, use_inq=False):
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


def extract_colorpalette(palette_name, n=None, mode='hex'):
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
    if n > len(target):
        rep = int(np.floor(n / len(target)))
        target = list(itertools.chain.from_iterable(itertools.repeat(x, rep) for x in target))
        target += [target[-1]] * (n - len(target))

    return target


def rename_dict_keys(d, key_dict):
    """
    Rename dictionary keys using a `key_dict` mapping.
    """
    for k, v in key_dict.items():
        if k in d.keys():
            d[v] = d.pop(k)

    return d


def append_filename_suffix(filename, suffix):
    """
    Add suffix string to filename before extension.

    filename {exists} Name of file to append suffix to.
    suffix {str} Suffix string to append to filename.
    """
    base, ext = os.path.splitext(filename)

    if ext == '.icloud':
        ext_icloud = ext
        base, ext = os.path.splitext(base)
        ext += ext_icloud

    return base + suffix + ext


def textfile_len(fname):
    """
    Get number of rows in a text file.
    """
    with open(fname) as f:
        for i, l in enumerate(f):
            pass

    return i + 1


def dirsize(start_path='.'):
    """
    Get size of directory in bytes.
    Source: https://stackoverflow.com/questions/1392413/calculating-a-directorys-size-using-python
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size


def collapse_df_columns(df, sep='_'):
    """
    Collapse a multi-level column index in a dataframe.
    """
    df.columns = [sep.join(col).strip() for col in df.columns.values]
    return df


def pydonicli_register(var_dict):
    """
    Register variable as a part of the 'pydoni' module to be logged to the CLI's backend.
    """
    for key, value in var_dict.items():
        setattr(pydonitest, 'pydonicli_' + key, value)


def pydonicli_declare_args(var_dict):
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
