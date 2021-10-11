"""
    Copyright 2021 nanato12
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
        http://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

__description__ = "Generators for datetime."
__copyright__ = "Copyright 2021 nanato12"
__version__ = "1.0"
__license__ = "Apache License 2.0"
__author__ = "nanato12"
__author_email__ = "admin@nanato12.info"
__url__ = "https://github.com/nanato12/dt-range"


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


def __dtrange(
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
    return __dtrange(start, end, weeks=weeks)


def daterange(
    start: datetime, end: datetime, days: int = 1
) -> Generator[datetime, None, None]:
    return __dtrange(start, end, days=days)


def hourrange(
    start: datetime, end: datetime, hours: int = 1
) -> Generator[datetime, None, None]:
    return __dtrange(start, end, hours=hours)


def minuterange(
    start: datetime, end: datetime, minutes: int = 1
) -> Generator[datetime, None, None]:
    return __dtrange(start, end, minutes=minutes)


def secondrange(
    start: datetime, end: datetime, seconds: int = 1
) -> Generator[datetime, None, None]:
    return __dtrange(start, end, seconds=seconds)


def millisecondrange(
    start: datetime, end: datetime, milliseconds: int = 1
) -> Generator[datetime, None, None]:
    return __dtrange(start, end, milliseconds=milliseconds)


def microsecondrange(
    start: datetime, end: datetime, microseconds: int = 1
) -> Generator[datetime, None, None]:
    return __dtrange(start, end, microseconds=microseconds)


def timedeltarange(
    start: datetime, end: datetime, td: timedelta
) -> Generator[datetime, None, None]:
    return __dtrange(start, end, td=td)
