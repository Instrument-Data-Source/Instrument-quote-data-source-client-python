from src.swagger_client import Configuration, NewInstrumentRequestDto
from src.client.instrument_client import InstrumentClient
import logging
import unittest

from src.swagger_client.rest import ApiException
from src.default_config import set_default_host

class Delete_TestCase(unittest.TestCase):

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
    self.expected_dto1 = self.client.post_instrument(self.using_dto1)
    self.expected_dto2 = self.client.post_instrument(self.using_dto2)

  def tearDown(self):
    for dto in self.client.get_all():
      self.client.delete_by(dto.id)

  def test_WHEN_create_instrument_and_delete_by_id_THEN_deleted(self):
    # Array

    # Act
    self.client.delete_by(self.expected_dto1.id)

    # Assert
    self.assertIsNone(self.client.get_by(self.expected_dto1.id))

  def test_WHEN_create_instrument_and_delete_by_code_THEN_deleted(self):
    # Array
    # Act
    self.client.delete_by(self.expected_dto1.code)

    # Assert
    self.assertIsNone(self.client.get_by(self.expected_dto1.id))

  def test_WHEN_try_delete_wrong_instrumnt_THEN_exception(self):
      # Array

      # Act

      # Assert
      with self.assertRaises(ApiException):
        self.client.delete_by("InstDel9999")

      with self.assertRaises(ApiException):
        self.client.delete_by(9999)
