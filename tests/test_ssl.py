import unittest

from cyb_600_lab3.ssl_request import ssl_get_request


class TestSSL(unittest.TestCase):
    def test_authentication(self):
        output = ssl_get_request("https://localhost:8081/ssl", "/home/vboxuser/lab3-client/user.crt", "/home/vboxuser/lab3-client/user.key", "/home/vboxuser/lab3-client/rootCA.crt")
        self.assertEqual(output[0], 200)
        self.assertEqual(output[1],
                         "This endpoint is protected with 2 Way SSL. You will only be able to access it if you have the appropriate certificate given to it.")


if __name__ == '__main__':
    unittest.main()
