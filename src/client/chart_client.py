from typing import List, Union
from ..swagger_client.rest import ApiException
from ..swagger_client.configuration import Configuration
from ..swagger_client import ChartApi, ApiClient, UploadedCandlesDto, CandleDto, ChartDto
from ..default_config import get_default_config
from ..tools.date_mapper import map_to_dto_dt, map_to_variable


class ChartClient:
    def __init__(self, configuration: Configuration = None) -> None:
        if configuration is None:
            configuration = get_default_config()
        self.__api_instance = ChartApi(ApiClient(configuration))
        pass

    def post_chart(self, instrumentIdOrCode: str, timeframeIdOrCode: str, request_dto: UploadedCandlesDto) -> int:
        body = UploadedCandlesDto(**request_dto.to_dict())
        body.from_date = map_to_dto_dt(request_dto.from_date)
        body.untill_date = map_to_dto_dt(request_dto.untill_date)
        body.candles = [self.__mapCandle(c) for c in request_dto.candles]
        return self.__api_instance.api_chart_instrument_str_timeframe_str_post(
            instrumentIdOrCode, timeframeIdOrCode, body=body)

    def get_all(self) -> List[ChartDto]:
        response: List[ChartDto] = self.__api_instance.api_chart_get()
        ret = [ChartDto(**r.to_dict()) for r in response]
        for row in ret:
            row.from_date = map_to_variable(row.from_date)
            row.untill_date = map_to_variable(row.untill_date)
        return ret

    def get_for(self, instrumentIdOrCode: str) -> List[ChartDto]:
        response: List[ChartDto] = self.__api_instance.api_chart_instrument_str_get(
            instrumentIdOrCode)
        ret = [ChartDto(**r.to_dict()) for r in response]
        for row in ret:
            row.from_date = map_to_variable(row.from_date)
            row.untill_date = map_to_variable(row.untill_date)
        return ret

    def __mapCandle(self, candle: CandleDto) -> CandleDto:
        ret_c = CandleDto(**candle.to_dict())
        ret_c.date_time = map_to_dto_dt(candle.date_time)
        return ret_c
