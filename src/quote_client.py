from typing import List, Union
from .swagger_client.rest import ApiException
from .swagger_client.configuration import Configuration
from .swagger_client import ChartApi, ApiClient, CandleDto
from .default_config import get_default_config
from .tools.date_mapper import map_to_dto_dt, map_to_variable
from datetime import date


class QuoteClient:
    def __init__(self, configuration: Configuration = None) -> None:
        if configuration is None:
            configuration = get_default_config()
        self.__api_instance = ChartApi(ApiClient(configuration))
        pass

    def get_for(self, instrumentIdOrCode: str, timeframeIdOrCode: str, from_date: date, untill_date: date) -> List[CandleDto]:
        response: List[CandleDto] = self.__api_instance.api_chart_instrument_str_timeframe_str_get(
            instrumentIdOrCode, timeframeIdOrCode,
            _from=map_to_dto_dt(from_date), untill=map_to_dto_dt(untill_date))
        ret = [CandleDto(**r.to_dict()) for r in response]
        for row in ret:
            row.date_time = map_to_variable(row.date_time)
        return ret
