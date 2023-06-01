from src import Configuration, InstrumentClient, NewInstrumentRequestDto
from src.models.instrument_response_dto import InstrumentResponseDto
import logging
import unittest


class Post_instrument_TestCase(unittest.TestCase):

    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    def test_WHEN_request_create_THEN_ok(self):
        # Array
        Configuration.DEFAULT_HOST = "srv"
        client = InstrumentClient()
        request_dto = NewInstrumentRequestDto(
            f"Instrument10", f"InstPost10", 1, price_decimal_len=4, volume_decimal_len=2)
        # Act
        asserted_response = client.post_instrument(request_dto)

        # Assert
        self.logger.info(asserted_response)
        self.assertIsInstance(asserted_response, InstrumentResponseDto)

        # tearDown
        client.delete_by(asserted_response.id)
