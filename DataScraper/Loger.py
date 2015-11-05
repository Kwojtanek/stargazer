__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'
import os
import json


class LogData(object):
    """
    Class logs according to flag json formatted data provided by **kwargs
    """
    LOGS_DIRS = 'logs/'
    logs = {
        1: 'data.log',
        2: 'photo.log',
        3: 'error.log',
        4: 'test.log'

    }

    def __init__(self, flag, **kwargs):
        self.flag = flag
        self.kwargs = dict(kwargs)

    def print_log(self):
        return self.kwargs

    def save(self):
        """
        Saves log to appropriate file
        :return:
        """
        path = os.path.join(self.LOGS_DIRS, self.logs[self.flag])
        if not os.path.isfile(path):
            with open(path, 'w+') as f:
                json.dump([], f)
                f.close()
        with open(path) as f:
            data = json.load(f)
            f.close()
        with open(path, 'w') as f:
            data.append(self.kwargs)
            json.dump(data, f)
            f.close()
