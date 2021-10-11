from datetime import datetime, timedelta
from math import ceil
from typing import Generator, Optional

__ARGS = {
    "weeks",
    "days",
    "hours",
    "minutes",
    "seconds",
    "milliseconds",
    "microseconds",
}


def dtrange(
    start: datetime,
    end: datetime,
    td: Optional[timedelta] = None,
    **kwargs: int,
) -> Generator[datetime, None, None]:
    if not (set(kwargs.keys()) <= __ARGS):
        raise Exception(f"Invalid argments: {set(kwargs.keys()) - __ARGS}")

    td = td or timedelta(**kwargs)

    tmp = start
    yield tmp

    for _ in range(ceil((end - start) / td)):
        tmp = tmp + td
        if tmp <= end:
            yield tmp


def weekrange(
    start: datetime, end: datetime, weeks: int = 1
) -> Generator[datetime, None, None]:
    return dtrange(start, end, weeks=weeks)


def daterange(
    start: datetime, end: datetime, days: int = 1
) -> Generator[datetime, None, None]:
    return dtrange(start, end, days=days)


def hourrange(
    start: datetime, end: datetime, hours: int = 1
) -> Generator[datetime, None, None]:
    return dtrange(start, end, hours=hours)


def minuterange(
    start: datetime, end: datetime, minutes: int = 1
) -> Generator[datetime, None, None]:
    return dtrange(start, end, minutes=minutes)


def secondrange(
    start: datetime, end: datetime, seconds: int = 1
) -> Generator[datetime, None, None]:
    return dtrange(start, end, seconds=seconds)


def millisecondrange(
    start: datetime, end: datetime, milliseconds: int = 1
) -> Generator[datetime, None, None]:
    return dtrange(start, end, milliseconds=milliseconds)


def microsecondrange(
    start: datetime, end: datetime, microseconds: int = 1
) -> Generator[datetime, None, None]:
    return dtrange(start, end, microseconds=microseconds)


def timedeltarange(
    start: datetime, end: datetime, td: timedelta
) -> Generator[datetime, None, None]:
    return dtrange(start, end, td=td)
