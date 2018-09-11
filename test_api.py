import unittest
import api

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = api.app.test_client()

    def test_index(self):
        return_value = self.app.get('/')
        assert b'Hi, Daniel!' in return_value.data

if __name__ == '__main__':
    unittest.main()