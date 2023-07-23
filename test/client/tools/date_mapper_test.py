import unittest
import logging
from datetime import datetime, timezone, date
from src.tools.date_mapper import map_to_dto_dt, TimeZoneException, set_utc_check


class DateMapper_MapToDto_TestCase(unittest.TestCase):

    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    def setUp(self) -> None:
        set_utc_check(True)
        return super().setUp()

    def test_WHEN_give_date_THEN_get_correct_dto_date(self):
        # Array
        usingDate = datetime(2020, 1, 1).astimezone(timezone.utc)
        expectedDate = "2020-01-01T00:00:00.000Z"
        # Act
        assertedDate = map_to_dto_dt(usingDate)
        # Assert
        self.assertEqual(expectedDate, assertedDate)

    def test_WHEN_give_datetime_THEN_get_correct_dto_date(self):
        # Array
        usingDate = datetime(2020, 1, 1, 6, 4, 22).astimezone(timezone.utc)
        expectedDate = "2020-01-01T06:04:22.000Z"
        # Act
        assertedDate = map_to_dto_dt(usingDate)
        # Assert
        self.assertEqual(expectedDate, assertedDate)

    def test_WHEN_datetime_is_not_utc_THEN_exception(self):
        # Array
        usingDate = datetime(2020, 1, 1, 6, 4, 22)
        # Act

        # Assert
        with self.assertRaises(TimeZoneException):
            map_to_dto_dt(usingDate)

    def test_WHEN_datetime_is_not_utc_but_check_is_off_THEN_ok(self):
        # Array
        usingDate = datetime(2020, 1, 1, 6, 4, 22)
        expectedDate = "2020-01-01T06:04:22.000Z"
        # Act
        set_utc_check(False)
        assertedDate = map_to_dto_dt(usingDate)
        # Assert
        self.assertEqual(expectedDate, assertedDate)

    def test_WHEN_date_is_not_utc_THEN_ok(self):
        # Array
        usingDate = date(2020, 1, 1)
        expectedDate = "2020-01-01T00:00:00.000Z"
        # Act
        assertedDate = map_to_dto_dt(usingDate)
        # Assert
        self.assertEqual(expectedDate, assertedDate)
