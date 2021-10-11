from datetime import datetime

from dt_range import hourrange


class TestHourRange:
    """時間単位ジェネレータのテスト"""

    def test_it(self) -> None:
        """通常"""

        start = datetime(2000, 1, 1, 1)
        end = datetime(2000, 1, 1, 6)

        generator_object = hourrange(start, end)
        assert next(generator_object) == start
        assert next(generator_object) == datetime(2000, 1, 1, 2)
        assert next(generator_object) == datetime(2000, 1, 1, 3)
        assert next(generator_object) == datetime(2000, 1, 1, 4)
        assert next(generator_object) == datetime(2000, 1, 1, 5)
        assert next(generator_object) == end

    def test_orver_day(self) -> None:
        """日をまたぐ"""

        start = datetime(2000, 1, 1, 21)
        end = datetime(2000, 1, 2, 3)

        generator_object = hourrange(start, end)
        assert next(generator_object) == start
        assert next(generator_object) == datetime(2000, 1, 1, 22)
        assert next(generator_object) == datetime(2000, 1, 1, 23)
        assert next(generator_object) == datetime(2000, 1, 2, 0)
        assert next(generator_object) == datetime(2000, 1, 2, 1)
        assert next(generator_object) == datetime(2000, 1, 2, 2)
        assert next(generator_object) == end

    def test_orver_month(self) -> None:
        """月をまたぐ"""

        start = datetime(2000, 1, 31, 21)
        end = datetime(2000, 2, 1, 3)

        generator_object = hourrange(start, end)
        assert next(generator_object) == start
        assert next(generator_object) == datetime(2000, 1, 31, 22)
        assert next(generator_object) == datetime(2000, 1, 31, 23)
        assert next(generator_object) == datetime(2000, 2, 1, 0)
        assert next(generator_object) == datetime(2000, 2, 1, 1)
        assert next(generator_object) == datetime(2000, 2, 1, 2)
        assert next(generator_object) == end

    def test_orver_year(self) -> None:
        """年をまたぐ"""

        start = datetime(2000, 12, 31, 21)
        end = datetime(2001, 1, 1, 3)

        generator_object = hourrange(start, end)
        assert next(generator_object) == start
        assert next(generator_object) == datetime(2000, 12, 31, 22)
        assert next(generator_object) == datetime(2000, 12, 31, 23)
        assert next(generator_object) == datetime(2001, 1, 1, 0)
        assert next(generator_object) == datetime(2001, 1, 1, 1)
        assert next(generator_object) == datetime(2001, 1, 1, 2)
        assert next(generator_object) == end
