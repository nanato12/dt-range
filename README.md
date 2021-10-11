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

### weekrange

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

## GitHub Actions

- **pychecker**

  python code check (black, flake8, isort, mypy)
  - [Repository](https://github.com/nanato12/pychecker)
  - [Marketplace](https://github.com/marketplace/actions/pychecker)
