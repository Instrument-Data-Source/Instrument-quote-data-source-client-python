from datetime import datetime
import unittest
import logging
from src import Configuration, InstrumentClient, NewInstrumentRequestDto
from src.models.instrument_response_dto import InstrumentResponseDto


class InstrumentApi_post_instrument_TestCase(unittest.TestCase):

  logger = logging.getLogger(__name__)
  logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                      datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

  def test_WHEN_request_create_THEN_ok(self):
    # Array
    Configuration.DEFAULT_HOST = "srv"
    client = InstrumentClient()
    request_dto = NewInstrumentRequestDto(
        f"Instrument10", f"Inst10", "Currency", price_decimal_len=4, volume_decimal_len=2)
    # Act
    asserted_response = client.post_instrument(request_dto)

    # Assert
    self.logger.info(asserted_response)
    self.assertIsInstance(asserted_response, InstrumentResponseDto)


class InstrumentApi_get_all_instrument_TestCase(unittest.TestCase):

  logger = logging.getLogger(__name__)
  logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                      datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

  def __init__(self, methodName: str = "runTest") -> None:
    Configuration.DEFAULT_HOST = "srv"

    super().__init__(methodName)

  def test_WHEN_request_THEN_get_data(self):
    # Array
    client = InstrumentClient()
    request_dto = NewInstrumentRequestDto(
        f"Instrument13", f"Inst13", "Currency", price_decimal_len=4, volume_decimal_len=2)
    client.post_instrument(request_dto)
    # Act
    asserted_dtos = client.get_all()

    # Assert
    self.assertGreater(len(asserted_dtos), 0)
    for dto in asserted_dtos:
      self.assertIsInstance(dto, InstrumentResponseDto)

  def test_WHEN_request_by_code_THEN_get_data(self):
    # Array
    client = InstrumentClient()
    request_dto = NewInstrumentRequestDto(
        f"Instrument16", f"Inst16", "Currency", price_decimal_len=4, volume_decimal_len=2)
    new_inst = client.post_instrument(request_dto)

    # by Code
    # Act
    asserted_dto = client.get_by("Inst16")

    # Assert
    self.assertIsInstance(asserted_dto, InstrumentResponseDto)
    self.assertEqual(asserted_dto, new_inst)

    # by Id
    # Act
    asserted_dto = client.get_by(asserted_dto.id)

    # Assert
    self.assertIsInstance(asserted_dto, InstrumentResponseDto)
    self.assertEqual(asserted_dto, new_inst)
