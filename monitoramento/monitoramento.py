"""Não ta pronto."""

from httpx import Client, RequestError, ConnectTimeout


def resquest_ok(url: str) -> bool:
    try:
        with Client(follow_redirects=True) as client:
            response = client.get(url=url)
            if response.status_code == 200:
                return True
    except ConnectTimeout:
        ...
        """TODO: tratar a exception"""
    except RequestError:
        ...
        """TODO: tratar a exception"""


if __name__ == "__main__":
    if resquest_ok(url="https://globo.com"):
        print("OK")
