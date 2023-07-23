from ..swagger_client.configuration import Configuration
from ..swagger_client import InstrumentTypeApi, ApiClient,  InstrumentTypeResponseDto
from ..swagger_client.rest import ApiException
from typing import List
from ..default_config import get_default_config


class InstrumentTypeClient:
    def __init__(self, configuration: Configuration = None) -> None:
        if configuration is None:
            configuration = get_default_config()
        self.__api_instance = InstrumentTypeApi(ApiClient(configuration))
        pass

    def get(self, instrumentIdOrCode) -> InstrumentTypeResponseDto:
        try:
            return self.__api_instance.api_instrument_type_instrument_type_str_get(instrumentIdOrCode)
        except ApiException:
            return None

    def get_all(self) -> List[InstrumentTypeResponseDto]:
        return self.__api_instance.api_instrument_type_get()
