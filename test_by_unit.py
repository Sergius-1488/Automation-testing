import unittest
from selenium import webdriver


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.driver = webdriver.Chrome()
        self.driver.get('google.com')

if __name__ == "__main__":
    unittest.main()
