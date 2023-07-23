from .swagger_client.configuration import Configuration
from .swagger_client import TimeFrameApi, ApiClient,  TimeFrameResponseDto
from .swagger_client.rest import ApiException
from typing import List
from .default_config import get_default_config


class TimeFrameClient:
    def __init__(self, configuration: Configuration = None) -> None:
        if configuration is None:
            configuration = get_default_config()
        self.__api_instance = TimeFrameApi(ApiClient(configuration))
        pass

    def get(self, tfIdOrCode) -> TimeFrameResponseDto:
        try:
            return self.__api_instance.api_time_frame_timeframe_str_get(tfIdOrCode)
        except ApiException:
            return None

    def get_all(self) -> List[TimeFrameResponseDto]:
        return self.__api_instance.api_time_frame_get()
