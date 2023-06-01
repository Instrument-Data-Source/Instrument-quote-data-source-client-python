from src import Configuration, InstrumentClient, NewInstrumentRequestDto
import logging
import unittest

from src.rest import ApiException


class Delete_TestCase(unittest.TestCase):

  logger = logging.getLogger(__name__)
  logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                      datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

  def __init__(self, methodName: str = "runTest") -> None:
    Configuration.DEFAULT_HOST = "srv"
    self.client = InstrumentClient()
    super().__init__(methodName)

  def test_WHEN_create_instrument_and_delete_by_id_THEN_deleted(self):
    # Array
    request_dto = NewInstrumentRequestDto(
        f"InstrumentInstDel16", f"InstDel1", 1, price_decimal_len=4, volume_decimal_len=2)
    new_inst = self.client.post_instrument(request_dto)

    # Act
    self.client.delete_by(new_inst.id)

    # Assert
    asserted_value = self.client.get_by(new_inst.id)
    self.assertIsNone(asserted_value)

  def test_WHEN_create_instrument_and_delete_by_code_THEN_deleted(self):
    # Array
    request_dto = NewInstrumentRequestDto(
        f"InstrumentInstDel16", f"InstDel2", 1, price_decimal_len=4, volume_decimal_len=2)
    new_inst = self.client.post_instrument(request_dto)

    # Act
    self.client.delete_by("InstDel2")

    # Assert
    asserted_value = self.client.get_by(new_inst.id)
    self.assertIsNone(asserted_value)

  def test_WHEN_create_instrument_and_delete_by_code_THEN_deleted(self):
    # Array
    request_dto = NewInstrumentRequestDto(
        f"InstrumentInstDel16", f"InstDel2", 1, price_decimal_len=4, volume_decimal_len=2)
    new_inst = self.client.post_instrument(request_dto)

    # Act
    self.client.delete_by("InstDel2")

    # Assert
    asserted_value = self.client.get_by(new_inst.id)
    self.assertIsNone(asserted_value)

  def test_WHEN_try_delete_wrong_instrumnt_THEN_exception(self):
      # Array

      # Act

      # Assert
      with self.assertRaises(ApiException):
        self.client.delete_by("InstDel9999")

      with self.assertRaises(ApiException):
        self.client.delete_by(9999)
