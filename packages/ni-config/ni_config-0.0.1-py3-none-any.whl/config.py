# coding: utf-8

import os
import yaml
import json
import logging
from jsonschema import validate, ValidationError


class config(object):

    def __init__(self, name):
        self._name = name
        self._filenames = {
            'desc': name + '.desc',
            'cfg': name + '.cfg'
        }
        self._value = config.load(self._filenames['cfg'])
        desc = config.load(self._filenames['desc'])
        self._desc = desc['schema']
        self._default = desc['default']
        if self._value is None:
            self.set_default()
        else:
            if self.validate():
                pass
            else:
                raise AssertionError(
                    'According to description file "' + self._filenames['desc'] + '", the content of config file "' +
                    self._filenames['cfg'] + '" is invalid.')

    def validate(self):
        try:
            validate(instance=self._value, schema=self._desc)
            return True
        except ValidationError:
            return False

    @staticmethod
    def load(ori_filename):
        obj_json = None
        filename = os.path.join(os.getcwd(), ori_filename)
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                obj_json = yaml.safe_load(f)
                logging.info('Succeeded reading file "' + filename + '".')
        else:
            logging.warning(str(filename) + ' is not found.')
        return obj_json

    def dump(self):
        if self.validate():
            filename = os.path.join(os.getcwd(), self._filenames['cfg'])
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self._value, f, indent=4)
        else:
            raise AssertionError('Value of "' + self._name + '" is invalid.')

    def __getitem__(self, item):
        if item in self._value:
            return self._value[item]
        else:
            raise KeyError('Key "' + item + '" is not found in config object "' + self._name + '".')

    def __setitem__(self, key, value):
        if key in self._value:
            t = type(self._default[key])
            if isinstance(value, t):
                old_value = self._value.copy()
                self._value[key] = value
                if self.validate():
                    pass
                else:
                    self._value = old_value
                    raise ValueError('Value for setting is invalid.')
            else:
                raise ValueError('Value for setting should be ' + str(t) + '.')
        else:
            raise KeyError('Key "' + key + '" is not found in config object "' + self._name + '".')

    def __repr__(self):
        return self._value.__repr__()

    def is_default(self):
        return self._value == self._default

    def set_default(self):
        self._value = self._default.copy()
