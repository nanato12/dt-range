from datetime import datetime, timedelta
from typing import Generator


def daterange(
    start: datetime, end: datetime
) -> Generator[datetime, None, None]:
    for day in range((end - start).days + 1):
        yield start + timedelta(day)
