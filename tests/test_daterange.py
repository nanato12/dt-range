from datetime import datetime

from dt_range import daterange


class TestDateRange:
    def test_it(self) -> None:
        """通常"""

        start = datetime(2000, 1, 1)
        end = datetime(2000, 1, 5)

        generator_object = daterange(start, end)
        assert next(generator_object) == start
        assert next(generator_object) == datetime(2000, 1, 2)
        assert next(generator_object) == datetime(2000, 1, 3)
        assert next(generator_object) == datetime(2000, 1, 4)
        assert next(generator_object) == end

    def test_orver_month(self) -> None:
        """月をまたぐ"""

        start = datetime(2000, 1, 28)
        end = datetime(2000, 2, 3)

        generator_object = daterange(start, end)
        assert next(generator_object) == start
        assert next(generator_object) == datetime(2000, 1, 29)
        assert next(generator_object) == datetime(2000, 1, 30)
        assert next(generator_object) == datetime(2000, 1, 31)
        assert next(generator_object) == datetime(2000, 2, 1)
        assert next(generator_object) == datetime(2000, 2, 2)
        assert next(generator_object) == end

    def test_orver_year(self) -> None:
        """年をまたぐ"""

        start = datetime(2000, 12, 28)
        end = datetime(2001, 1, 3)

        generator_object = daterange(start, end)
        assert next(generator_object) == start
        assert next(generator_object) == datetime(2000, 12, 29)
        assert next(generator_object) == datetime(2000, 12, 30)
        assert next(generator_object) == datetime(2000, 12, 31)
        assert next(generator_object) == datetime(2001, 1, 1)
        assert next(generator_object) == datetime(2001, 1, 2)
        assert next(generator_object) == end
