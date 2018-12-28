from collections import OrderedDict,Counter

from operator import itemgetter


class OrderedCounter(Counter, OrderedDict):
    pass


[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]
