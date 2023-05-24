from datetime import datetime
import unittest
import logging
from src import Configuration, InstrumentApi, NewInstrumentRequestDto
from src.models.instrument_response_dto import InstrumentResponseDto


class InstrumentApi_CreateInstrument_TestCase(unittest.TestCase):

  logger = logging.getLogger(__name__)
  logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                      datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

  def test_WHEN_request_create_THEN_ok(self):
    # Array
    Configuration.DEFAULT_HOST = "srv"
    client = InstrumentApi()
    request_dto = NewInstrumentRequestDto(
        f"Instrument1", f"Inst1", "Currency", price_decimal_len=4, volume_decimal_len=2)
    # Act
    asserted_response = client.post_instrument(body=request_dto)

    # Assert
    self.logger.info(asserted_response)
    self.assertIsInstance(asserted_response, InstrumentResponseDto)
