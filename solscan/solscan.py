""" API wrapper for Solscan.  """
from requests import request
from ratelimit import ratelimit
from tenacity import retry, stop_after_attempt, wait_fixed


cache = {'meta': {}}


@retry(stop=stop_after_attempt(3), wait=wait_fixed(5))  # retries on error.
@ratelimit(duration=1/4, sleep=True)  # limits calls to 4 per second.
def fetch(path: str, param: dict = None) -> dict:
    return request('GET', f'https://public-api.solscan.io/{path}', params=param).json()


def get_token_meta(token: str) -> dict:
    """ Get token metadata.

    Args:
        address (str, optional): The address to get the token balance for. Defaults to None.

    Returns:
        dict: The token metadata.
    """
    if token in cache['meta']:
        return cache['meta'][token]
    result = fetch('token/meta', {'tokenAddress': token})
    cache['meta'][token] = result
    return result


def get_last_block(limit: int = 10) -> dict:
    """ Get the last block.
    
    Args:
        limit (int, optional): The limit to get the last block. Defaults to 10.

    Returns:
        dict: The last block.
    """
    return fetch('block/last', {'limit': limit})


def get_block_transactions(limit: int = 10, offset: int = 0, block: int = None) -> dict:
    """ Get the block transactions.

    Args:
        limit (int, optional): The limit to get the block transactions. Defaults to 10.
        offset (int, optional): The offset to get the block transactions. Defaults to 0.
        block (int, optional): The block to get the block transactions for. Defaults to None.

    Returns:
        dict: The block transactions.
    """
    return fetch('block/transactions', {'limit': limit, 'offset': offset, 'block': block})