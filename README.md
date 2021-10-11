# dt-range

python datetime generator

## Usage

```shell
$ pip install dt-range
```

```python
from dt_range import dtrange ,weekrange ,daterange ,hourrange ,minuterange ,secondrange ,millisecondrange ,microsecondrange ,timedeltarange
```

## Examples

Here is an example of usage using `START` and `END`.

```python
from datetime import datetime

START = datetime(2021, 1, 1)
END = datetime(2021, 1, 31)
```

### weekrange

`weekrange` can be used to get the date for each week.

```python
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

## GitHub Actions

- **pychecker**

  python code check (black, flake8, isort, mypy)
  - [Repository](https://github.com/nanato12/pychecker)
  - [Marketplace](https://github.com/marketplace/actions/pychecker)
