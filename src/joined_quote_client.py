from typing import List, Union
from .swagger_client.rest import ApiException
from .swagger_client.configuration import Configuration
from .swagger_client import ChartApi, ApiClient, JoinedCandleDto
from .default_config import get_default_config
from .tools.date_mapper import map_to_dto_dt, map_to_variable
from datetime import date


class JoinedQuoteClient:
    def __init__(self, configuration: Configuration = None) -> None:
        if configuration is None:
            configuration = get_default_config()
        self.__api_instance = ChartApi(ApiClient(configuration))
        pass

    def get_joined_for(self, instrumentIdOrCode: str, timeframeIdOrCode: str, targetTimeFrameIdOrCode: str, from_date: date, untill_date: date) -> List[JoinedCandleDto]:
