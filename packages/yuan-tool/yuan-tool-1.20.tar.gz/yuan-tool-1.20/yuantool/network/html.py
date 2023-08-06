import socket
import requests
import logging

logger = logging.getLogger(__name__)


def _get_html(url):
    # change_user_agent()
    html = requests.get(url)
    if html.status_code == 200:
        res = html.text
    else:
        res = False
    return res


def _post_data(url, data):
    # change_user_agent()
    try:
        res = requests.post(url, data=str(data).encode('utf-8'))
        if res.status_code != 200:
            res = False
    except Exception as e:
        if 'Failed to establish a new connection:' in str(e):
            logger.warning(e)
            logger.warning(e)
        else:
            logger.warning(e, exc_info=True)
        res = False
    return res
