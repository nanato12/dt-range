# dt-range

Generators for datetime.

## Usage

You can use `pip` to install this package.

```shell
$ pip install dt-range
```

If you use it, import `dt_range`.

Note the slight difference from this package name.

```python
from dt_range import weekrange ,daterange ,hourrange ,minuterange ,secondrange ,millisecondrange ,microsecondrange ,timedeltarange
```

## Examples

Here is an example of usage using `START` and `END`.

### weekrange

`weekrange` can be used to get the date for each week.

```python
from datetime import datetime

from dt_range import weekrange

START = datetime(2021, 1, 1)
END = datetime(2021, 1, 31)

for dt in weekrange(START, END):
    print(dt)
# 2021-01-01 00:00:00
# 2021-01-08 00:00:00
# 2021-01-15 00:00:00
# 2021-01-22 00:00:00
# 2021-01-29 00:00:00

for dt in weekrange(START, END, weeks=2):
    print(dt)
# 2021-01-01 00:00:00
# 2021-01-15 00:00:00
# 2021-01-29 00:00:00
```

### daterange

`daterange` can be used to get the date for each day.

```python
from datetime import datetime

from dt_range import daterange

START = datetime(2021, 1, 1)
END = datetime(2021, 1, 31)

for dt in daterange(START, END):
    print(dt)
# 2021-01-01 00:00:00
# 2021-01-02 00:00:00
# 2021-01-03 00:00:00
# ...
# 2021-01-29 00:00:00
# 2021-01-30 00:00:00
# 2021-01-31 00:00:00


for dt in daterange(START, END, days=4):
    print(dt)
# 2021-01-01 00:00:00
# 2021-01-05 00:00:00
# 2021-01-09 00:00:00
# 2021-01-13 00:00:00
# 2021-01-17 00:00:00
# 2021-01-21 00:00:00
# 2021-01-25 00:00:00
# 2021-01-29 00:00:00
```

### hourrange

`hourrange` can get the `datetime` for each hour.

`datetime` will be 0:00 if you don't specify the `hour` argument, so you may need to specify 23:00 in some cases.

```python
from datetime import datetime

from dt_range import hourrange

START = datetime(2021, 1, 1)
END = datetime(2021, 1, 1, 23)


for dt in hourrange(START, END):
    print(dt)
# 2021-01-01 00:00:00
# 2021-01-01 01:00:00
# 2021-01-01 02:00:00
# 2021-01-01 03:00:00
# ...
# 2021-01-01 21:00:00
# 2021-01-01 22:00:00
# 2021-01-01 23:00:00

for dt in hourrange(START, END, hours=4):
    print(dt)
# 2021-01-01 00:00:00
# 2021-01-01 04:00:00
# 2021-01-01 08:00:00
# 2021-01-01 12:00:00
# 2021-01-01 16:00:00
# 2021-01-01 20:00:00
```

### Other

You can also use `minuterange`, `secondrange`, etc. in the same way.

If you want to break it into smaller time segments, use `timedeltarange`.

```python
from datetime import datetime, timedelta

from dt_range import timedeltarange

START = datetime(2021, 1, 1)
END = datetime(2021, 1, 31)


for dt in timedeltarange(
    START,
    END,
    timedelta(days=5, hours=4, minutes=3, seconds=2, microseconds=1),
):
    print(dt)
# 2021-01-01 00:00:00
# 2021-01-06 04:03:02.000001
# 2021-01-11 08:06:04.000002
# 2021-01-16 12:09:06.000003
# 2021-01-21 16:12:08.000004
# 2021-01-26 20:15:10.000005
```

## GitHub Actions

- **pychecker**

  python code check (black, flake8, isort, mypy)
  - [Repository](https://github.com/nanato12/pychecker)
  - [Marketplace](https://github.com/marketplace/actions/pychecker)
