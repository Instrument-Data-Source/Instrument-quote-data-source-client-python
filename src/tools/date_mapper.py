from typing import Union
from datetime import datetime, timezone, date

UTC_CHECK_IS_ON = False


def set_utc_check(isOn: bool):
    global UTC_CHECK_IS_ON
    UTC_CHECK_IS_ON = isOn


def map_to_dto_dt(dt: Union[date, datetime]) -> str:
    global UTC_CHECK_IS_ON
    if isinstance(dt, datetime) and dt.tzinfo != timezone.utc and UTC_CHECK_IS_ON:
        raise TimeZoneException(dt)
    return dt.strftime('%Y-%m-%dT%H:%M:%S.000Z')


def map_to_variable(dt: datetime) -> datetime:
    return dt.astimezone(timezone.utc)


class TimeZoneException(Exception):
    def __init__(self, dt: datetime):
        super().__init__(
            f"Datetime {dt} isn't in UTC timezone. Use .astimezone(timezone.utc) to verify that datetime in UTC format or use set_utc_check(False) to disable check")
