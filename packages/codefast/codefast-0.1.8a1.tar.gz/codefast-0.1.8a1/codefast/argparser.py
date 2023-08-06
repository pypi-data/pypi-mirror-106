from collections import defaultdict
import sys

PLACEHOLDER = 'PLACEHOLDER'


class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def get_arg(arg: str) -> str:
    return arg.strip('-')


def is_arg(arg: str) -> bool:
    return arg.startswith('-')


class ArgParser:
    def __init__(self):
        self._arg_counter = 0
        self._alias = defaultdict(set)
        self._help = {}

    def input(self, *args, **kwargs):
        return self.add_argument(*args, **kwargs)

    def add_argument(self,
                     abbr: str = "",
                     full_arg: str = "",
                     default_value: str = "",
                     sub_args: list = [],
                     description: str = ""):
        """ Add arguments to object.
        :abbr: str, abbreviated argument, e.g., -dw could be an abbraviation of --download
        :full_arg: str, complete argument name, e.g., --download
        :default_value:, str, default value of argument
        :description: str, description of what the argument will invoke
        :sub_args:, dict, possible sub arguments.
        """
        self._arg_counter += 1
        full, abbr = get_arg(full_arg), get_arg(abbr)
        if not full:
            full = abbr
        if not abbr:
            abbr = full
        self._alias[abbr].add(full)
        self._alias[full].add(abbr)

        self._help[full] = {
            'description': description,
            'abbr': abbr,
            'full': full,
            'sub_args': sub_args
        }
        # self.__data[full] = Fro
        _dict = dotdict()
        _dict['_pid'] = dotdict({'_pid': -1})
        for i, sa in enumerate(sub_args):
            for _arg in sa:
                _arg = get_arg(_arg)
                _dict['_pid'][_arg] = i
                _dict[get_arg(_arg)] = {}

        setattr(self, full, _dict)
        setattr(self, abbr, _dict)

    def parse_args(self) -> None:
        self.parse()

    def parse(self) -> None:
        # sys.argv += ['-LONG_FAKE_ARGUMENT', 'LONG_FAKE_VALUE']
        self.input(abbr='-LONG_FAKE_ARGUMENT')
        args, main = sys.argv[1:], 'LONG_FAKE_ARGUMENT'
        if args:
            main, pre_arg = get_arg(args[0]), None
            self.__dict__[main]['value'] = PLACEHOLDER

            def _transmit_value(arg_name:str, value):
                for _alias in list(self.__dict__[main]['_pid']):
                    cur_pic = self.__dict__[main]['_pid'][arg_name]
                    if self.__dict__[main]['_pid'][_alias] == cur_pic:
                        self.__dict__[main][_alias] = value

            for i, _arg in enumerate(args[1:]):
                if i == 0 and not is_arg(_arg):  # Input value for main arg
                    self.__dict__[main]['value'] = _arg
                elif is_arg(_arg):  # Input value for sub arg
                    sub_arg = get_arg(_arg)
                    value = dotdict({'value': ''})
                    _transmit_value(sub_arg, value)
                    pre_arg = sub_arg

                else:
                    _transmit_value(pre_arg, _arg)

        for _key in list(self.__dict__):
            if not _key.startswith('_'):
                if _key != main and _key not in self._alias[main]:
                    self.__dict__[_key] = False

    def help(self) -> None:
        ''' display help message '''
        for _, value in self._help.items():
            if value['description']:
                str_left = f"-{value['abbr']} (-{value['full']}) ["

                for i, subs in enumerate(value['sub_args']):
                    sub_str = ','.join('-' + get_arg(s) for s in subs)
                    if i < len(value['sub_args']) - 1: sub_str += ' | '
                    str_left += sub_str

                str_left += ']'
                str_left = str_left.replace(
                    '[]', '')  # strip [] when sub_arg list is empty

                desc = value['description']
                lst = desc.split('\n')
                for i, ln in enumerate(lst):
                    print('{:<60} {:<10}'.format(str_left if i == 0 else '',
                                                 lst[i]))


if __name__ == '__main__':
    dd = ArgumentParser()
    dd.add_argument(abbr='-oss',
                    sub_args=[['u', 'upload'], ['del', 'delete'],
                              ['dw', 'download', 'd']],
                    description='Aliyun OSS manager.')
    dd.add_argument(abbr='-dw',
                    full_arg='--download',
                    sub_args=[['proxy', 'p'], ['r', 'rename', 'o']])

    dd.parse(['-oss', '-d', 'https://google.com/a.txt'])
    # pprint.pprint(dd.__dict__)

    if dd.oss:
        if dd.oss.download:
            print(dd.oss.download)

        if dd.oss.delete:
            print('oss delete')

    dd.help()
    pprint.pprint(dd.__dict__)
