import unittest
import logging
from src.default_config import set_default_host
from src import TimeFrameClient, TimeFrameResponseDto


class TimeFrameClient_GetAll_TestCase(unittest.TestCase):

    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    def test_WHEN_request_tf_list_THEN_get_it(self):
        # Array
        set_default_host("srv")

        api_instance = TimeFrameClient()

        # Act
        asserted_response = api_instance.get_all()

        # Assert
        asserted_tf_code = [resp.code for resp in asserted_response]
        self.logger.info("Asserted response")
        self.logger.info(asserted_response)

        self.assertGreater(len(asserted_response), 0)
        self.assertIn("M", asserted_tf_code)
        self.assertIn("m1", asserted_tf_code)


class TimeFrameClient_GetByCode_TestCase(unittest.TestCase):

    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    def test_WHEN_request_with_correct_code_THEN_get_it(self):
        # Array
        set_default_host("srv")

        api_instance = TimeFrameClient()

        # Act
        asserted_response = api_instance.get("m1")

        # Assert
        self.logger.info("Asserted response")
        self.logger.info(asserted_response)

        self.assertEqual("m1", asserted_response.code)
        self.assertEqual(10, asserted_response.id)
        self.assertEqual(60, asserted_response.seconds)

    def test_WHEN_request_with_incorrect_code_THEN_get_it(self):
        # Array
        set_default_host("srv")

        api_instance = TimeFrameClient()

        # Act

        # Assert
        self.assertIsNone(api_instance.get("m111"))


class TimeFrameClient_GetById_TestCase(unittest.TestCase):

    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    def test_WHEN_request_with_correct_id_THEN_get_it(self):
        # Array
        set_default_host("srv")

        api_instance = TimeFrameClient()

        # Act
        asserted_response = api_instance.get(10)

        # Assert
        self.logger.info("Asserted response")
        self.logger.info(asserted_response)

        self.assertEqual("m1", asserted_response.code)
        self.assertEqual(10, asserted_response.id)
        self.assertEqual(60, asserted_response.seconds)

    def test_WHEN_request_with_incorrect_id_THEN_get_it(self):
        # Array
        set_default_host("srv")

        api_instance = TimeFrameClient()

        # Act

        # Assert
        self.assertIsNone(api_instance.get(-1))
