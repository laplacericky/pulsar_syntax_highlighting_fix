import argparse,sys
import datetime
from zoneinfo import ZoneInfo
from scipy.stats import norm

HK_timezone = ZoneInfo('Asia/Hong_Kong')

class s_time:
    def __init__(self, record = None, date = None, exact_time = None):
        if record is not None:
            self.date = record['date']
            self.exact_time = record['exact_time']
        else:
            assert date is not None and exact_time is not None
            self.date = date
            self.exact_time = exact_time
    def __lt__(self, other):
        if self.date == other.date:
            return self.exact_time < other.exact_time
        else:
            return self.date < other.date

    def todatetime(self):
        match self.exact_time:
            case 0|1:
                return datetime.datetime(self.date.year, self.date.month, self.date.day, 12)
            case 2|3:
                tmr = self.date + datetime.timedelta(days=1)
                return datetime.datetime(tmr.year, tmr.month, tmr.day, tzinfo = HK_timezone)

def func(x):
    pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int ,default = 5)
    args = parser.parse_args()
    hello = f'{123}\n'

    boo = True
    map(func, [1,2,3])

    CONSTANT_LIKE = 3
    bb = CONSTANT_LIKE
    ll = []
    dd = {}
    a = 3
    a,b = 3,4
    c = int(3)
    e = dict()
    f = set()
    args.n = 3

    match a:
        case 3:
            print(3)
        case 4:
            pass
        case _:
            pass

if __name__ == '__main__':
    assert sys.version_info[0] >= 3 and sys.version_info[1] >= 11
    main()
