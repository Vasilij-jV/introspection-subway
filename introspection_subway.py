# -*- config: utf8 -*-

from pprint import pprint
import inspect
from random import randint


class Subway:

    def __init__(self, days):
        self.days = days
        self.turnstiles = 5
        self._maximum = 100000

    def statistics_on_turnstiles(self):
        # Словарь со значениями количества прохождений людей через один турникет
        statistics_of_one_turnstile = {}
        # Цикл, генерирующий случайное число прохождений через турникет за один день
        for _ in range(1, self.days):
            for number_turnstile in range(1, 6):
                count_of_people = randint(500, 3500)
                number_turnstile_str = str(number_turnstile)
                # Суммирование прохождений через один турникет за несколько дней
                if statistics_of_one_turnstile.get(number_turnstile_str):
                    statistics_of_one_turnstile[number_turnstile_str] += count_of_people
                else:
                    statistics_of_one_turnstile[number_turnstile_str] = count_of_people
        # Выявление максимального количества прохождений через один турникет за несколько дней
        max_people = max(statistics_of_one_turnstile, key=statistics_of_one_turnstile.get)
        if statistics_of_one_turnstile[max_people] > self._maximum:
            print(
                f'Через турникет номер {max_people} прошло {statistics_of_one_turnstile[max_people]} людей. Это '
                f'превышает максимальное количество использований турникета. Турникету номер {max_people} необходимо '
                f'провести '
                f'техническое обслуживание.')
        return statistics_of_one_turnstile


subway = Subway(47)
print(subway.statistics_on_turnstiles())

introspection_obj = {}


def introspection_info(obj):
    if inspect.isfunction(obj) or inspect.isclass(obj) or inspect.ismodule(obj):
        introspection_obj['name'] = obj.__name__
        introspection_obj['type'] = type(obj)
    else:
        introspection_obj['type'] = type(obj)
    introspection_obj['attributes'] = dir(obj)
    regular_methods = [method for method in dir(obj) if
                       callable(getattr(obj, method)) and not method.startswith("__")]
    introspection_obj['methods'] = regular_methods
    introspection_obj['module'] = inspect.getmodule(obj)
    introspection_obj['callable'] = callable(obj.statistics_on_turnstiles)


introspection_info(subway)
pprint(introspection_obj)
