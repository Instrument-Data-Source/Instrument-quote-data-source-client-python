from ..configuration import Configuration
from .. import TimeFrameApi, ApiClient,  TimeFrameResponseDto
from typing import List


class TimeFrameClient:
    def __init__(self, configuration: Configuration = None) -> None:
        self.__api_instance = TimeFrameApi(ApiClient(configuration))
        pass

    def get_all(self) -> List[TimeFrameResponseDto]:
        return self.__api_instance.api_time_frame_get()
