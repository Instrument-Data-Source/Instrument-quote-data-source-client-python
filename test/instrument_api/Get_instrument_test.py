
from src.instrument_client import InstrumentClient, NewInstrumentRequestDto, InstrumentResponseDto
import logging
import unittest
from src.default_config import set_default_host


class Get_instrument_TestCase(unittest.TestCase):

  logger = logging.getLogger(__name__)
  logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                      datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

  def __init__(self, methodName: str = "runTest") -> None:
    set_default_host("srv")
    self.client = InstrumentClient()
    self.using_dto1 = NewInstrumentRequestDto(
        f"Instrument13", f"InstGA1", 1, price_decimal_len=4, volume_decimal_len=2)
    self.using_dto2 = NewInstrumentRequestDto(
        f"Instrument14", f"InstGA2", 2, price_decimal_len=5, volume_decimal_len=3)

    super().__init__(methodName)

  def setUp(self):
    for dto in self.client.get_all():
      self.client.delete_by(dto.id)
    self.client.post_instrument(self.using_dto1)
    self.client.post_instrument(self.using_dto2)

  def test_WHEN_request_all_THEN_get_data(self):
    # Array

    # Act
    asserted_dtos = self.client.get_all()

    # Assert
    self.assertEqual(2, len(asserted_dtos))
    for dto in asserted_dtos:
      self.assertIsInstance(dto, InstrumentResponseDto)
      if (dto.code == self.using_dto1.code):
        self.assertEqual(dto.name, self.using_dto1.name)
      else:
        self.assertEqual(dto.name, self.using_dto2.name)

  def test_WHEN_request_by_code_or_id_THEN_get_data(self):
    # Array

    # by Code
    # Act
    asserted_dto = self.client.get_by(self.using_dto1.code)

    # Assert
    self.assertIsInstance(asserted_dto, InstrumentResponseDto)
    self.assertEqual(asserted_dto.code, self.using_dto1.code)
    self.assertEqual(asserted_dto.name, self.using_dto1.name)
    self.assertEqual(asserted_dto.volume_decimal_len,
                     self.using_dto1.volume_decimal_len)
    self.assertEqual(asserted_dto.price_decimal_len,
                     self.using_dto1.price_decimal_len)

    using_id = asserted_dto.id
    # by Id
    # Act
    asserted_dto = self.client.get_by(using_id)

    # Assert
    self.assertIsInstance(asserted_dto, InstrumentResponseDto)
    self.assertEqual(asserted_dto.code, self.using_dto1.code)
    self.assertEqual(asserted_dto.name, self.using_dto1.name)
    self.assertEqual(asserted_dto.volume_decimal_len,
                     self.using_dto1.volume_decimal_len)
    self.assertEqual(asserted_dto.price_decimal_len,
                     self.using_dto1.price_decimal_len)
    self.assertEqual(asserted_dto.id, using_id)

  def test_WHEN_request_by_wrong_code_or_id_THEN_get_data(self):
    self.assertIsNone(self.client.get_by(-1))
    self.assertIsNone(self.client.get_by("asdasd"))

  def tearDown(self):
    self.client.delete_by(self.using_dto1.code)
    self.client.delete_by(self.using_dto2.code)
