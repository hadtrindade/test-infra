from typing import Union
from httpx import Client, ConnectTimeout, ConnectError


def resquest_ok(url: str) -> Union[None, str]:
    """Verifica se o site alvo está ok.

    Args:
        url (str): endereço do site alvo.

    Returns:
        Union[None, str]: em caso de sucesso retorna None,
        caso contrário Str.
    """
    try:
        with Client(follow_redirects=True) as client:
            response = client.get(url=url)
            if response.status_code == 200:
                return
    except ConnectTimeout as e:
        return e
    except ConnectError as e:
        return e
    except Exception as e:
        return e


if __name__ == "__main__":
    if not resquest_ok(url="https://evolux.net.br/"):
        print("OK")
