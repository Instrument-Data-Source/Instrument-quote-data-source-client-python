from src.swagger_client import Configuration, NewInstrumentRequestDto
from src.client import ChartClient, InstrumentClient, UploadedCandlesDto, CandleDto
import logging
import unittest
from src.default_config import set_default_host
from datetime import datetime, timezone
from src.tools.date_mapper import set_utc_check


class Post_Chart_TestCase(unittest.TestCase):

    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    def __init__(self, methodName: str = "runTest") -> None:
        set_default_host("srv")
        self.client = ChartClient()
        self.using_inst1 = NewInstrumentRequestDto(
            f"Instrument13", f"InstGA1", 1, price_decimal_len=4, volume_decimal_len=2)
        self.using_inst2 = NewInstrumentRequestDto(
            f"Instrument14", f"InstGA2", 2, price_decimal_len=5, volume_decimal_len=3)

        super().__init__(methodName)

    def setUp(self):
        self.instrument_client = InstrumentClient()
        for dto in self.instrument_client.get_all():
            self.instrument_client.delete_by(dto.id)
        self.expected_inst1 = self.instrument_client.post_instrument(
            self.using_inst1)
        self.expected_inst2 = self.instrument_client.post_instrument(
            self.using_inst2)

    def tearDown(self):
        for dto in self.instrument_client.get_all():
            self.instrument_client.delete_by(dto.id)

    def test_WHEN_pest_new_chart_THEN_added(self):
        # Array
        usedCandles = [CandleDto(datetime(2020, 1, 1), 100, 150, 90, 130, 100)]
        usedDto = UploadedCandlesDto(
            datetime(2020, 1, 1), datetime(2020, 3, 1), usedCandles)
        set_utc_check(False)
        # Act
        assertedResponse = self.client.post_chart(
            self.expected_inst1.id, "D1", usedDto)

        # Assert
        self.assertEqual(1, assertedResponse)
