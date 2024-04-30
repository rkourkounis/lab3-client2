import base64
import typing
import requests
import ssl


def basic_get_request(url: str, auth_string: str, rootCA: str) -> typing.Tuple[int, str]:
    """
    Basic Authentication
    Takes in parameters and makes a GET web call to "url" with appropriate headers for Basic auth.
    @param url: the URL to attempt to authenticate to
    @param auth_string: A base64 encoded string to be used for authentication
    @param rootCA: File location of the root ca
    @return: A python tuple of (status code, text output of the web call)
    """
    output = requests.get(url,  headers={"Authorization": "basic " + auth_string}, verify=rootCA)
    return output.status_code, output.text


def generate_auth_string(username: str, password: str) -> str:
    """
    Takes in a username and password and outputs a base64 string of "username:password"
    @param username: String representing a username
    @param password: String representing a password
    @return: A string of the base64 auth string.
    """

    auth_string = username + ":" + password
    return base64.b64encode(auth_string.encode('ascii')).decode('ascii')
   

# HINT: DO NOT CHANGE ANYTHING UNDER THIS LINE
if __name__ == '__main__':
    print("Enter Username")
    username = input()
    print("Enter Password")
    password = input()

    print("Location of root CA certificate [default: ../../rootCA.crt]")
    rootCA = input()
    rootCA = rootCA if rootCA else "../../rootCA.crt"

    print(basic_get_request("https://localhost:8080/basic", generate_auth_string(username, password), rootCA))
