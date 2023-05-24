import unittest
import logging
import src


class TimeFrameApi_GetAll_TestCase(unittest.TestCase):

  logger = logging.getLogger(__name__)
  logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                      datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

  def test_WHEN_request_tf_list_THEN_get_it(self):
    # Array
    configuration = src.Configuration()
    configuration.host = "srv"

    api_instance = src.TimeFrameApi(src.ApiClient(configuration))

    # Act
    asserted_response = api_instance.get_all_time_frame()

    # Assert
    asserted_tf_code = [resp.code for resp in asserted_response]
    self.logger.info("Asserted response")
    self.logger.info(asserted_response)

    self.assertGreater(len(asserted_response), 0)
    self.assertIn("M", asserted_tf_code)
    self.assertIn("m1", asserted_tf_code)
