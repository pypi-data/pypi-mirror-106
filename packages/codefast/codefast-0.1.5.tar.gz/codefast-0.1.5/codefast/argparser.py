import sys
import collections
from typing import List

PLACEHOLDER = "PLACEHOLDER"
help_message = {}


class ArgParser:
    """A simple argument parser"""
    def __init__(self):
        self.__dict__ = collections.defaultdict(Attribute)
        self.arg_counter = 0

    def input(self,
              abbr: str = "",
              full_arg: str = "",
              default_value: str = "",
              sub_args: List = [],
              description: str = ""):
        # alias of add argument
        self.add_argument(abbr,
                          full_arg,
                          default_value=default_value,
                          sub_args=sub_args,
                          description=description)

    def add_argument(self,
                     abbr: str = "",
                     full_arg: str = "",
                     default_value: str = "",
                     sub_args: List = [],
                     description: str = ""):
        """ Add arguments to object.
        :abbr: str, abbreviated argument, e.g., -dw could be an abbraviation of --download
        :full_arg: str, complete argument name, e.g., --download
        :default_value:, str, default value of argument
        :description: str, description of what the argument will invoke
        :sub_args:, dict, possible sub arguments.
        """
        assert full_arg != "", "Full argument name is required."
        self.arg_counter += 1
        full = full_arg.strip('-')
        abbr = abbr.strip('-') if abbr else full
        help_message[full] = {
            'description': description,
            'abbr': abbr,
            'full': full,
            'sub_args': sub_args
        }

        attribute_holder = _AttributeHolder(default_value)
        setattr(self, full, attribute_holder)
        setattr(self, abbr, attribute_holder)

        for sub_arg_list in sub_args:
            assert isinstance(sub_arg_list, list), "Sub args are list of list"

            _attribute = Attribute()
            for item in sorted(sub_arg_list, key=len):
                setattr(_AttributeHolder, item.strip('-'), _attribute)

    def parse_args(self) -> None:
        """ Parse arguments from sys.argv. Two types of arguments:
        1. main argument, once decided, values of all other main argument is set to None
        2. sub argument.
        """
        main_arg, sub_arg = None, None
        for item in sys.argv[1:]:
            if item.startswith('-'):
                sub_arg = item.strip('-')
                if not main_arg:
                    main_arg = sub_arg
                    if not self.__dict__[sub_arg].value:
                        self.__dict__[
                            sub_arg].value = PLACEHOLDER  # Assign default value.
                else:
                    _AttributeHolder.__dict__[sub_arg].value = PLACEHOLDER
            else:
                if main_arg == sub_arg:
                    self.__dict__[main_arg].value = item
                else:
                    _AttributeHolder.__dict__[sub_arg].value = item

        # When no argument is passed in, forge a main argument.
        if not main_arg:
            main_arg = PLACEHOLDER
            setattr(self, main_arg, None)

        for _other in list(self.__dict__):  # set value of other arg to None
            if getattr(self, _other) != getattr(self, main_arg):
                copy_attr: str = '__' + _other
                setattr(self, copy_attr, getattr(self, _other))
                setattr(self, _other, None)

    def help(self) -> None:
        ''' display help message '''
        for _, value in help_message.items():
            if value['description']:
                str_left = f"-{value['abbr']} (-{value['full']}) ["

                for i, subs in enumerate(value['sub_args']):
                    sub_str = ','.join('-' + s for s in subs)
                    if i < len(value['sub_args']) - 1: sub_str += ' | '
                    str_left += sub_str
                
                str_left += ']'
                str_left = str_left.replace('[]', '')  # strip [] when sub_arg list is empty
                
                desc = value['description']
                lst = desc.split('\n')
                for i, ln in enumerate(lst):
                    print('{:<50} {:<10}'.format(str_left if i == 0 else '', lst[i]))


class Attribute:
    """Final node of argparse to get value directly with dot notation."""
    def __init__(self, value: str = ""):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value: str) -> None:
        self.value = value


class _AttributeHolder(object):
    def __init__(self, value: str = ""):
        self.value = value
