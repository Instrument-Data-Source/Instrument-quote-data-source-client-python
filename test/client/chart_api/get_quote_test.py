from src.client import ChartClient, InstrumentClient, UploadedCandlesDto, CandleDto, ChartClient, QuoteClient,NewInstrumentRequestDto
import logging
import unittest
from src.default_config import set_default_host
from datetime import datetime, timezone, date
from src.tools.date_mapper import set_utc_check


class Get_Quote_TestCase(unittest.TestCase):

    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    def __init__(self, methodName: str = "runTest") -> None:
        set_default_host("srv")
        self.client = QuoteClient()
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

        self.usedCandles = [
            CandleDto(datetime(2020, 1, 1), 100, 150, 90, 130, 100),
            CandleDto(datetime(2020, 1, 2), 110.1, 160, 80, 140, 110.33),]
        self.usedDto = UploadedCandlesDto(
            datetime(2020, 1, 1), datetime(2020, 2, 1), self.usedCandles)
        set_utc_check(False)
        ChartClient().post_chart(
            self.expected_inst1.id, "D1", self.usedDto)

    def tearDown(self):
        for dto in self.instrument_client.get_all():
            self.instrument_client.delete_by(dto.id)

    def test_WHEN_request_quotes_THEN_get_correct(self):
        # Array

        # Act
        assertedResponse = self.client.get_for(
            self.expected_inst1.code, "D1", date(2020, 1, 1), date(2020, 2, 1))

        # Assert

        self.assertEqual(2, len(assertedResponse))

        assertedCandle = assertedResponse[0]
        self.assertEqual(datetime(2020, 1, 1).astimezone(
            timezone.utc), assertedCandle.date_time)
        self.assertEqual(100, assertedCandle.open)
        self.assertEqual(150, assertedCandle.high)
        self.assertEqual(90, assertedCandle.low)
        self.assertEqual(130, assertedCandle.close)
        self.assertEqual(100, assertedCandle.volume)

        assertedCandle = assertedResponse[1]
        self.assertEqual(datetime(2020, 1, 2).astimezone(
            timezone.utc), assertedCandle.date_time)
        self.assertEqual(110.1, assertedCandle.open)
        self.assertEqual(160, assertedCandle.high)
        self.assertEqual(80, assertedCandle.low)
        self.assertEqual(140, assertedCandle.close)
        self.assertEqual(110.33, assertedCandle.volume)
