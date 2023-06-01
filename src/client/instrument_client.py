from typing import List, Union

from ..rest import ApiException
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

    def get_by(self, instumentStr: Union[str, int]) -> InstrumentResponseDto:
        try:
            return self.__api_instance.api_instrument_instrument_str_get(instumentStr)
        except ApiException:
            return None

    def delete_by(self, instumentStr: Union[str, int]):
        self.__api_instance.api_instrument_instrument_str_delete(instumentStr)