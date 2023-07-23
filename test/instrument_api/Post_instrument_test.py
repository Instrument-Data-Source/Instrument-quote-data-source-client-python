from src.default_config import set_default_host
from src import InstrumentClient,NewInstrumentRequestDto ,InstrumentResponseDto
import logging
import unittest


class Post_instrument_TestCase(unittest.TestCase):

    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    def test_WHEN_request_create_THEN_ok(self):
        # Array
        set_default_host("srv")
        client = InstrumentClient()
        request_dto = NewInstrumentRequestDto(
            f"Instrument10", f"InstPost10", 1, price_decimal_len=4, volume_decimal_len=2)
        # Act
        asserted_response = client.post_instrument(request_dto)

        # Assert
        self.logger.info(asserted_response)
        self.assertIsInstance(asserted_response, InstrumentResponseDto)
        self.assertEqual(asserted_response.code, request_dto.code)
        self.assertEqual(asserted_response.name, request_dto.name)

        # tearDown
        client.delete_by(asserted_response.id)
