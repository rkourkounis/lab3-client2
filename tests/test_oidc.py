import unittest
import ssl
import requests 

from cyb_600_lab3.oidc_request import generate_auth_string, oidc_get_request


class TestBasic(unittest.TestCase):
    def test_auth_string(self):
        username = "user"
        password = "user"
        try:
            output = generate_auth_string(username, password, "/home/vboxuser/lab3-client/rootCA.crt")
        except Exception as e:
            assert False, "Error was thrown"
        self.assertIsNotNone(output, "Output is None")

    def test_authentication(self):
        username = "user"
        password = "user"
        output = oidc_get_request("https://localhost:8082/keycloak", generate_auth_string(username, password, "/home/vboxuser/lab3-client/rootCA.crt"), "/home/vboxuser/lab3-client/rootCA.crt")
        self.assertEqual(output[0], 200)
        self.assertEqual(output[1], "This endpoint is protected with Keycloak and uses OIDC authentication. It needs a token passed in.")

if __name__ == '__main__':
    unittest.main()
