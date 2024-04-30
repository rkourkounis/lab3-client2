import typing
import base64
import ssl
import requests


def oidc_get_request(url: str, auth_string: str, rootCA: str) -> typing.Tuple[int, str]:
    """
    Takes in parameters and makes a GET web call to "url" with appropriate headers for Bearer auth.
    @param url: the URL to attempt to authenticate to
    @param auth_string: A JWT
    @param rootCA: File location of the root ca
    @return: A python tuple of (status code, text output of the web call)
    """
    output = requests.get(url,  headers={"Authorization": "Bearer " + auth_string}, verify=rootCA)
    return output.status_code, output.text



def generate_auth_string(username: str, password: str, rootCA: str) -> str:
    """
    DO NOT CHANGE THIS METHOD. I DID THIS BIT FOR YOU.
    Takes in a Username and Password and asks Keycloak to generate an access token. This handles authentication
    @param username: String representing a username
    @param password: String representing a password
    @param rootCA: String with the file location of the rootCA
    @return: returns a JWT access token that can be used for auth
    """
    form_data = {
        'client_id': "keycloak",
        'grant_type': "password",
        'scope': "openid",
        'username': 'user',
        'password': 'user'
    }
    response = requests.post('https://localhost:8443/realms/cyb600/protocol/openid-connect/token', verify=rootCA, data=form_data)
    if response.status_code == 200:
        return response.json()['access_token']
    raise IOError("Unable to authenticate")

# HINT: DO NOT CHANGE ANYTHING UNDER THIS LINE
if __name__ == '__main__':
    print("Enter Username")
    username = input()
    print("Enter Password")
    password = input()

    print("Location of root CA certificate [default: /home/vboxuser/lab3-client/rootCA.crt]")
    rootCA = input()
    rootCA = rootCA if rootCA else "/../../../rootCA.crt"

    print(oidc_get_request("https://localhost:8082/keycloak", generate_auth_string(username, password, rootCA), rootCA))
