import typing
import requests

def ssl_get_request(url: str, cert: str, key: str, rootCA: str) -> typing.Tuple[int, str]:
    """
    Takes in file paths for key/cert and rootCA and offers that cert for client Authentication
    @param url: he URL to attempt to authenticate to
    @param cert: Public Key to use for authentication
    @param key: Private Key to use for authentication
    @param rootCA: CA that signed the server
    @return: A python tuple of (status code, text output of the web call)
    """
    output = requests.get(url, cert=(cert,key), verify=rootCA)
    return output.status_code, output.text

# HINT: DO NOT CHANGE ANYTHING UNDER THIS LINE
if __name__ == '__main__':
    print("Location of user certificate [default: ../../user.crt]")
    cert = input()
    cert = cert if cert else "../../user.crt"

    print("Location of user certificate [default: ../../user.key]")
    key = input()
    key = key if key else "../../user.key"


    print("Location of root CA certificate [default: ../../rootCA.crt]")
    rootCA = input()
    rootCA = rootCA if rootCA else "../../rootCA.crt"

    print(ssl_get_request("https://localhost:8081/ssl", cert, key, rootCA))
