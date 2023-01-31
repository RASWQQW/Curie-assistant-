import datetime
import json


class LogManager(object):
    """
    Totally validating of date process
    """

    def __init__(self):
        pass

    def step1ForSaving(self: object) -> None:
        print(self)
        with open('./historyData.json', 'r') as f:
            _array = json.load(f)

        if (datetime.date.today() - datetime.date(_array['date'][0], _array['date'][1], _array['date'][2])).days > 1:
            today = datetime.datetime.now()
            dict = {'date': (today.year, today.month, today.day)}
            with open('./historyData.json', 'w') as f:
                json.dump(dict, f, indent=4, separators=(',', ':'))