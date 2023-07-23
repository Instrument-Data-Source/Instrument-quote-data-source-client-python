import unittest
import logging
from src.default_config import get_default_config, set_default_host



class Configuration_TestCase(unittest.TestCase):

  logger = logging.getLogger(__name__)
  logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                      datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

  def test_WHEN_set_up_default_host_THEN_when_no_config_than_of(self):
    # Array
    expectedHost = "123"

    # Act
    set_default_host(expectedHost)
    assertedConfig = get_default_config()

    # Assert
    self.assertEqual(expectedHost, assertedConfig.host,
                     "Default config doesn't changed")
