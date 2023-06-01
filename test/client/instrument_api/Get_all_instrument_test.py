from src import Configuration, InstrumentClient, NewInstrumentRequestDto
from src.models.instrument_response_dto import InstrumentResponseDto
import logging
import unittest


class Get_all_instrument_TestCase(unittest.TestCase):

  logger = logging.getLogger(__name__)
  logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                      datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

  def __init__(self, methodName: str = "runTest") -> None:
    Configuration.DEFAULT_HOST = "srv"
    self.client = InstrumentClient()
    self.using_dto = NewInstrumentRequestDto(
        f"Instrument13", f"InstGA1", 1, price_decimal_len=4, volume_decimal_len=2)

    super().__init__(methodName)

  def setUp(self):
    self.client.post_instrument(self.using_dto)

  def test_WHEN_request_THEN_get_data(self):
    # Array

    # Act
    asserted_dtos = self.client.get_all()

    # Assert
    self.assertGreater(len(asserted_dtos), 0)
    for dto in asserted_dtos:
      self.assertIsInstance(dto, InstrumentResponseDto)

  def test_WHEN_request_by_code_THEN_get_data(self):
    # Array

    # by Code
    # Act
    asserted_dto = self.client.get_by(self.using_dto.code)

    # Assert
    self.assertIsInstance(asserted_dto, InstrumentResponseDto)
    self.assertEqual(asserted_dto.code, self.using_dto.code)
    self.assertEqual(asserted_dto.name, self.using_dto.name)
    self.assertEqual(asserted_dto.volume_decimal_len,
                     self.using_dto.volume_decimal_len)
    self.assertEqual(asserted_dto.price_decimal_len,
                     self.using_dto.price_decimal_len)

    using_id = asserted_dto.id
    # by Id
    # Act
    asserted_dto = self.client.get_by(using_id)

    # Assert
    self.assertIsInstance(asserted_dto, InstrumentResponseDto)
    self.assertEqual(asserted_dto.code, self.using_dto.code)
    self.assertEqual(asserted_dto.name, self.using_dto.name)
    self.assertEqual(asserted_dto.volume_decimal_len,
                     self.using_dto.volume_decimal_len)
    self.assertEqual(asserted_dto.price_decimal_len,
                     self.using_dto.price_decimal_len)
    self.assertEqual(asserted_dto.id, using_id)

  def tearDown(self):
    self.client.delete_by(self.using_dto.code)
