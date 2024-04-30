import unittest

from cyb_600_lab3.basic_request import generate_auth_string, basic_get_request


class TestBasic(unittest.TestCase):
    def test_auth_string(self):
        username = "username"
        password = "password"
        output = generate_auth_string(username, password)
        self.assertEqual(output, "dXNlcm5hbWU6cGFzc3dvcmQ=")  # add assertion here

    def test_authentication(self):
        output = basic_get_request("https://localhost:8080/basic", "dXNlcjp1c2Vy", "/home/vboxuser/lab3-client/rootCA.crt")
        self.assertEqual(output[0], 200)
        self.assertEqual(output[1], "This endpoint is protected with Basic authentication. It needs a User:pass passed in.")

if __name__ == '__main__':
    unittest.main()
