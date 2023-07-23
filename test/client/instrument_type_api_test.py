import unittest
import logging
from src.default_config import set_default_host
from src.client import InstrumentTypeClient, InstrumentTypeResponseDto



class InstrumentTypeClient_GetAll_TestCase(unittest.TestCase):

    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    def test_WHEN_request_tf_list_THEN_get_it(self):
        # Array
        set_default_host("srv")

        api_instance = InstrumentTypeClient()

        # Act
        asserted_response = api_instance.get_all()

        # Assert
        asserted_tf_code = [resp.name for resp in asserted_response]
        self.logger.info("Asserted response")
        self.logger.info(asserted_response)

        self.assertGreater(len(asserted_response), 0)
        self.assertIn("Stock", asserted_tf_code)
        self.assertIn("Currency", asserted_tf_code)


class InstrumentTypeClient_GetByCode_TestCase(unittest.TestCase):

    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    def test_WHEN_request_with_correct_code_THEN_get_it(self):
        # Array
        set_default_host("srv")

        api_instance = InstrumentTypeClient()

        # Act
        asserted_response = api_instance.get("Stock")

        # Assert
        self.logger.info("Asserted response")
        self.logger.info(asserted_response)

        self.assertEqual("Stock", asserted_response.name)
        self.assertEqual(2, asserted_response.id)

    def test_WHEN_request_with_incorrect_code_THEN_get_it(self):
        # Array
        set_default_host("srv")

        api_instance = InstrumentTypeClient()

        # Act

        # Assert
        self.assertIsNone(api_instance.get("m111"))


class InstrumentTypeClient_GetById_TestCase(unittest.TestCase):

    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    def test_WHEN_request_with_correct_id_THEN_get_it(self):
        # Array
        set_default_host("srv")

        api_instance = InstrumentTypeClient()

        # Act
        asserted_response = api_instance.get(2)

        # Assert
        self.logger.info("Asserted response")
        self.logger.info(asserted_response)

        self.assertEqual("Stock", asserted_response.name)
        self.assertEqual(2, asserted_response.id)

    def test_WHEN_request_with_incorrect_id_THEN_get_it(self):
        # Array
        set_default_host("srv")

        api_instance = InstrumentTypeClient()

        # Act
        self.assertIsNone(api_instance.get(-1))

        # Assert
        self.assertIsNone(api_instance.get(-1))
