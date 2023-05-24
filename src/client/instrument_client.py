from typing import List
from ..configuration import Configuration
from .. import InstrumentApi, ApiClient, NewInstrumentRequestDto, InstrumentResponseDto


class InstrumentClient:
    def __init__(self, configuration: Configuration = None) -> None:
        self.__api_instance = InstrumentApi(ApiClient(configuration))
        pass

    def post_instrument(self, request_dto: NewInstrumentRequestDto) -> InstrumentResponseDto:
        return self.__api_instance.api_instrument_post(body=request_dto)

    def get_all(self) -> List[InstrumentResponseDto]:
        return self.__api_instance.api_instrument_get()
