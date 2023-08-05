import gtransport
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


def get_retry_strategy(
    retries=0, status_forcelist=None, method_whitelist=None, backoff_factor=0.3
):
    if method_whitelist is None:
        method_whitelist = ["HEAD", "GET", "OPTIONS"]
    if status_forcelist is None:
        status_forcelist = [429, 500, 502, 503, 504]

    return Retry(
        total=retries,
        read=retries,
        connect=retries,
        status_forcelist=status_forcelist,
        method_whitelist=method_whitelist,
        backoff_factor=backoff_factor,
    )


def get_http_adapter(max_retries, pool_connections=10, pool_maxsize=200):
    return HTTPAdapter(
        max_retries=max_retries or get_retry_strategy(),
        pool_connections=pool_connections,
        pool_maxsize=pool_maxsize,
    )


def get_request_session(
    url=None,
    session=None,
    max_retries=0,
    adapter=None,
    pool_connections=10,
    pool_maxsize=200,
):
    """
    Wrapper function to create a session

    :param url: session for URL
    :param session: pass existing session or new session is created
    :param max_retries: int or urllib3 retry object
    :param adapter: request adapter, if not passed default http adapter is created
    :param pool_connections: int
    :param pool_maxsize: int

    :return: session object
    """
    session = session or gtransport.Session()
    max_retries = max_retries or get_retry_strategy(retries=0)

    adapter = adapter or get_http_adapter(
        max_retries=max_retries,
        pool_connections=pool_connections,
        pool_maxsize=pool_maxsize,
    )

    session.mount("http://", adapter)
    session.mount("https://", adapter)

    if url:
        session.mount(url, adapter)

    return session
