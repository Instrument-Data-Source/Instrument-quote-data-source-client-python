import unittest
import logging
from src.configuration import Configuration
from src.api import TimeFrameApi


class Configuration_TestCase(unittest.TestCase):

  logger = logging.getLogger(__name__)
  logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                      datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

  def test_WHEN_set_up_default_host_THEN_when_no_config_than_of(self):
    # Array
    Configuration.DEFAULT_HOST = "srv"

    # Act
    api_instance = TimeFrameApi()
    asserted_response = api_instance.get_all_time_frame()

    # Assert
    asserted_tf_code = [resp.code for resp in asserted_response]
    self.logger.info("Asserted response")
    self.logger.info(asserted_response)

    self.assertGreater(len(asserted_response), 0)
    self.assertIn("M", asserted_tf_code)
    self.assertIn("m1", asserted_tf_code)
