"""
    Module with classes to encapsulate abstract objects and helper methods over those objects
"""

# -- helper
import abc
import json
import logging
import re
import signal
from threading import Thread, Event
from time import sleep

from stringcolor import cs
from tqdm import tqdm

from videotools import COLOR_RED, COLOR_YELLOW, COLOR_GRAY, COLOR_LIGHT_BLUE
from videotools.utils import DateTimeHelper

PATTERN_DATE_FORMAT = re.compile(r'((?P<year>\d{4})\-(?P<month>\d{2})\-(?P<day>\d{2}))')

_logger = logging.getLogger("model")


class ColoredException(Exception):
    """
    Base exception used to create other exceptions with message, and debug args options
    """

    def __init__(self, msg, **kwargs):
        self.msg = msg
        self.debug_args = kwargs

    def __str__(self):
        _msg = cs(self.msg, COLOR_RED)
        _msg += '\n' * 2
        if self.debug_args and isinstance(self.debug_args, dict):
            _msg += cs('args:', COLOR_YELLOW)
            _msg += '\n'
            for _k, _v in self.debug_args.items():
                _msg += f'\t{cs(_k, COLOR_GRAY):>} -> {cs(_v, COLOR_LIGHT_BLUE):<}\n'
        return _msg


class MissingArgumentException(ColoredException):
    """
    Exception launched when a method needs a missing param
    """


class MissingTokenException(ColoredException):
    """
    Exception launched when a method needs an existing token, and none is found
    """


class WrongFileTypeException(ColoredException):
    """
    Exception launched when supplied file has not correct type
    """


class UnknownStatNameException(ColoredException):
    """
    Exception launched when supplied stat name does not exists in StatsDict
    """

    def __init__(self, name):
        super().__init__('Supplied stat name does not exists', name=name)


# -- logic

# -- model classes to handle data easier


class DictionaryField:
    """
    Encapsulates any object field with nested elements
    """

    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            if isinstance(value, dict):
                value = DictionaryField(**value)
            setattr(self, name, value)

    def serialize(self, *skip_fields, as_json=False):
        """
        Serialize current object as a dictionary, or json
        :param skip_fields: A list of fieldnames separated by colon to be skipped from serialized output
        :param as_json: Serialize object as json representation
        :return: A valid serialized object as a dictionary
        """
        skip_fields = list(skip_fields) or []
        skip_fields.append('logger')

        serialized_dict = dict()
        for k, v in self.__dict__.items():
            if k in skip_fields:
                continue
            if isinstance(v, DictionaryField):
                serialized_dict[k] = v.serialize(*skip_fields)
            elif isinstance(v, list):
                list_dict = []
                for elem in v:
                    # if a list element is serializable, serialize it
                    if isinstance(elem, DictionaryField):
                        list_dict.append(elem.serialize(*skip_fields))
                    else:
                        list_dict.append(elem)
                serialized_dict[k] = list_dict
            else:
                serialized_dict[k] = v
        if as_json:
            return json.dumps(serialized_dict)
        return serialized_dict


def get_obj_attr(object, item, missing_value=None, join_with=None, transform=None):
    """
    Returns the value of an object's attribute, checking if it exists. It can provide a predefined default value,
    in case it's an array can be joined with supplied char, and can be even transformed with supplied lambda function
    :param object: The object to look for the attribute
    :param item: The name of the field to retrieve
    :param missing_value: Default value in case it doesn't exists
    :param join_with: If the field value is an array, join the items with supplied char
    :param transform: Apply supplied transformation to the field, or to each member of the field if it's
    an array. The supplied function, must consider the type of data that the field value should contain, that is,
    we can not apply an upper() to an integer, for example.
    :return: The value of the field, or the default value if it doesn't exists and, optionally, transformed with
    supplied function or if it's an array, a single value with it's items joined
    """
    # traverse fields if several are provided joined by a dot
    fields = item.split('.')
    item = fields[-1]

    for _child in fields[:-1]:
        if hasattr(object, _child):
            object = getattr(object, _child)
        else:
            return missing_value

    if not hasattr(object, item):
        return missing_value

    value = getattr(object, item)

    if not isinstance(value, list):
        if transform:
            return transform(value)
        else:
            return value
    else:
        if transform and join_with:
            assert isinstance(join_with, str), f'{join_with} must be a string'
            return join_with.join([transform(x) for x in value])
        elif transform:
            return list(map(transform, value))
        elif join_with:
            return join_with.join(value)
        else:
            return value


# -- progress bars

class SchedulerThread(Thread):
    """
    Simple thread implementation to perform async operations
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, **kwargs):
        """
        :param sleep_sec: Time to sleep the thread
        :param daemon: Thread is gonna be a daemon
        """
        Thread.__init__(self)
        self.daemon = kwargs.get('daemon', True)
        self.sleep_sec = kwargs.get('sleep_sec', 1)

        # event to handle exit gracefully
        self.quit_event = Event()

        _logger.debug('registering quit signals...')
        signal.signal(signal.SIGINT, self._quit)
        signal.signal(signal.SIGTERM, self._quit)

    def _quit(self, signum, frame):
        _logger.debug(f'Signal __{signum}__ in frame __{frame}__ received. Quitting...')
        self.quit_event.set()
        raise InterruptedError()

    def run(self):
        _logger.debug('Starting scheduler...')
        while not self.quit_event.isSet():
            _logger.debug(f'Executing scheduler...')
            self._run()
            try:
                sleep(self.sleep_sec)
            except InterruptedError:
                _logger.debug('Quit signal intercepted, exiting scheduler...')
                if not self.quit_event.is_set():
                    self.quit_event.set()

    @abc.abstractmethod
    def _run(self):
        """
        Logic to be executed in thread
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def quit(self):
        """
        Logic to be executed for quitting thread execution
        """
        raise NotImplementedError()


class ProgressBarScheduler(SchedulerThread):
    """
    Thread to schedule progress bar operations
    """

    def __init__(self, description, **kwargs):
        """
        :param description: Text shown in progress bar description
        :param kwargs: Extra arguments
            sleep_sec: Time to sleep the thread (inherited)
            total: Total amount shown in progress bar
            color: Color of progress bar
            ratio: Update count for progress bar, instead of simple sleep_sec
            fake: Do not perform any progress operation
        """
        super().__init__(**kwargs)
        self.description = description

        # for those cases where no progress is gonna be shown
        self.fake = kwargs.get('fake', False)

        if not self.fake:
            self.sleep_sec = kwargs.get('sleep_sec', 1)
            self.total = kwargs.get('total', 100)
            self.color = kwargs.get('color', 'blue')
            self.ratio = kwargs.get('ratio', 1)
            self.pbar = tqdm(total=self.total, desc=self.description, position=0, colour=self.color)
            self.update_count = self.sleep_sec * self.ratio
            self.total_count = 0

    def run(self):
        if not self.fake:
            super().run()
        return

    def _run(self):
        if not self.fake:
            _logger.debug('executing progressbar _run....')
            self.total_count += self.update_count
            self.pbar.update(self.update_count)

    def quit(self):
        if not self.fake:
            _logger.debug('quitting progressbar _run....')
            self.pbar.update(self.total - self.total_count)
            self.pbar.close()
            self.quit_event.set()


class ProgressBar(tqdm):
    def __init__(self, **kwargs):
        """
       :param kwargs: Extra arguments
           fake: Do not perform any progress operation
       """
        self.fake = kwargs.pop('fake', False)
        if not self.fake:
            super().__init__(**kwargs)

    def update(self, n=1):
        if not self.fake:
            super().update(n)

    def close(self):
        if not self.fake:
            super().close()

# -- stats

class StatMeassure:
    COLUMNS_LENGTH = {'name': 40, 'other': 20}

    PRINT_SEPARATOR = '-' * 100
    PRINT_HEADER = '{:^{width}}'.format(' ' * COLUMNS_LENGTH['name'], width=COLUMNS_LENGTH['name']) + \
                   '{:^{width}}{:^{width}}{:^{width}}'.format('Total', 'Success', 'Failure',
                                                              width=COLUMNS_LENGTH['other'])

    __statkeys__ = ('name', 'total', 'success', 'failure')

    def __init__(self, name, **kwargs):
        self.name = name
        self.total = kwargs.get('total', 0)
        self.success = kwargs.get('success', 0)
        self.failure = kwargs.get('failure', 0)

    @staticmethod
    def _check_stats(**kwargs):
        assert len(set(kwargs.keys()).difference(StatMeassure.__statkeys__)) == 0, \
            cs(f'Supplied dictionary must contain required keys {StatMeassure.__statkeys__}', COLOR_RED)

    @staticmethod
    def of(**kwargs):
        """
        Creates an instance of meassurement from supplied dictionary. Only stats with integer values are valid, stats
        with percent values can not be used
        """
        StatMeassure._check_stats(**kwargs)
        _name = kwargs.pop('name')
        return StatMeassure(_name, **kwargs)

    def successUp(self, amount=1):
        self.success += amount

    def failureUp(self, amount=1):
        self.failure += amount

    def totalUp(self, amount=1):
        self.total += amount

    def stats(self, **kwargs):
        """
        Return number of total, success and failure as a dictionary
        :param kwargs: Any extra arguments
             json: Return a json dump
         percent: If True, return stats as percentage
         :return: A dictionary with stats or a json string ir param is given
        """
        _rst = self.__dict__
        if kwargs.get('json'):
            _rst = json.dumps(_rst)
        return _rst

    def percent(self, **kwargs):
        """
        Provides a dictionary with given values as percent
        :param kwargs: Any extra arguments
            json: Return a json dump
        :return: A dictionary with stats as percentages, or a json string ir param is given
        """
        _stats = self.stats()
        _rst = {'name': _stats['name'],
                'total': _stats['total'],
                'success': f'{(_stats["success"] / _stats["total"]) * 100:.1f}%',
                'failure': f'{(_stats["failure"] / _stats["total"]) * 100:.1f}%'}
        if kwargs.get('json'):
            _rst = json.dumps(_rst)
        return _rst

    def print(self, **kwargs):
        """
        Prints a formatted output of current stats
        :param kwargs: Any extra arguments
            percent: Print output as percent
        """
        _stats = self.stats()
        if kwargs.get('percent'):
            _stats = self.percent()

        _line = '{:^{width}}'.format(self.name, width=self.COLUMNS_LENGTH['name'])
        _line += '{:^{width}}{:^{width}}{:^{width}}'.format(_stats['total'], _stats['success'], _stats['failure'],
                                                            width=self.COLUMNS_LENGTH['other'])
        print(_line)


class Stats:
    """
    Class that wraps logic to perform basic calculations of % success events over total actions.
    Name of actions are defined dynamically, so no event or action names (aka: keys) are known
    in advance
    """

    def __init__(self):
        self.__substats__ = dict()

    @staticmethod
    def of(serialized):
        """
        Creates an instance of stats from supplied serialized object, either as a dict, or as a json dump
        :param serialized: A dictionary or a json dump
        """
        if isinstance(serialized, str):
            serialized = json.loads(serialized)

        assert isinstance(serialized, dict), cs('Serialized param must be a dictionary or a json dump')

        _stats = Stats()
        for _name, _st in serialized.items():
            _st.update({'name': _name})
            _stats.__substats__[_name] = StatMeassure.of(**_st)
        return _stats

    def add(self, meassure):
        """
        Adss a prebuilt meassure to this instance
        """
        assert isinstance(meassure, StatMeassure), cs('Supplied meassure must be an instance of StatMeassure')
        self.__substats__[meassure.name] = meassure
        return meassure

    def successUp(self, name, **kwargs):
        """
        Increases the number of success events
        :param name: Increases success events of given substat name
        :param kwargs: Any extra arguments
            amount: Amount to increase failure stat
           nototal: Skip total increase
        """
        amount = kwargs.get('amount', 1)
        nototal = kwargs.get('nototal', False)

        assert name, cs('Name of stat serie is required', COLOR_RED)

        if name not in self.__substats__.keys():
            self.__substats__[name] = StatMeassure(name)

        self.__substats__[name].successUp(amount)
        if nototal:
            return
        self.__substats__[name].totalUp(amount)

    def failureUp(self, name, **kwargs):
        """
        Increases the number of failure events
        :param name: Increases failure events of given substat name
        :param kwargs: Any extra arguments
             amount: Amount to increase failure stat
            nototal: Skip total increase
        """
        amount = kwargs.get('amount', 1)
        nototal = kwargs.get('nototal', False)

        assert name, cs('Name of stat serie is required', COLOR_RED)

        if name not in self.__substats__.keys():
            self.__substats__[name] = StatMeassure(name)

        self.__substats__[name].failureUp(amount)
        if nototal:
            return
        self.__substats__[name].totalUp(amount)

    def totalUp(self, name, **kwargs):
        """
        Increases the total number of events
        :param name: Increases total count of given substat name
        :param kwargs: Extra arguments
            amount: Amount to increase failure stat
        """
        assert name, cs('Name of stat serie is required', COLOR_RED)

        amount = kwargs.get('amount', 1)

        if name not in self.__substats__.keys():
            self.__substats__[name] = StatMeassure(name)
        self.__substats__[name].totalUp(amount)

    def stats(self, name, **kwargs):
        """
        Return number of total, success and failure as a dictionary
        :param name: Provide stats of given substat name
        :param kwargs: Any extra arguments
              json: Return stats as json dump
        """
        assert name, cs('Name of stat serie is required', COLOR_RED)

        # given stat name does not exits. So no input value was given
        if name and name not in self.__substats__.keys():
            raise UnknownStatNameException(name)
        return self.__substats__[name].stats(**kwargs)

    def percent(self, name, **kwargs):
        """
        Return number of total, success and failure as a dictionary expessed in %
        :param name: Provide stats of given substat name
        :param kwargs: Any extra arguments
              json: Return stats as json dump
        """
        # given stat name does not exits. So no input value was given
        if name and name not in self.__substats__.keys():
            raise UnknownStatNameException(name)
        return self.__substats__[name].percent(**kwargs)

    def delete(self, name):
        """
        Delete stats of given name
        :param name: Stats of given name are deleted
        """
        assert name, cs('Name of stat serie is required', COLOR_RED)

        if name and name not in self.__substats__.keys():
            raise UnknownStatNameException(name)

        del self.__substats__[name]

    def print(self):
        """
        Prints a formatted output for included stats
        """
        print(StatMeassure.PRINT_SEPARATOR)
        print(StatMeassure.PRINT_HEADER)
        print(StatMeassure.PRINT_SEPARATOR)

        for _meassure in self.__substats__.values():
            _meassure.print(percent=True)

        print(StatMeassure.PRINT_SEPARATOR)

    def update(self, stats):
        """
        Updated current stats with another instance of Stats
        """
        assert isinstance(stats, Stats), cs('stats must be an instance of Stats')
        for _name, _st_meassure in stats.__substats__.items():
            self.successUp(_name, amount=_st_meassure.success)
            self.failureUp(_name, amount=_st_meassure.failure)

    # reformat
    def as_dict(self):
        """
        Provides a dictionary with all stats
        :return: All stats as a dictionary
        """
        _dict = {}
        for _name, _st_meassure in self.__substats__.items():
            _dict[_name] = _st_meassure.stats()
        return _dict

    def as_json(self):
        """
        Return stats as json dump
        """
        return json.dumps(self.as_dict(), indent=4)

    def save(self, **kwargs):
        """
        Saves stats as json
        :param kwargs: Extra args
            filename: Final target final name for stats
        """
        _filename = kwargs.get('filename', f'stats_{DateTimeHelper.short_date()}.json')
        _logger.info('saving stats as %s', _filename)
        with open(_filename, 'w') as _f:
            _f.write(self.as_json())
            _f.flush()

