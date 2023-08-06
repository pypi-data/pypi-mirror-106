import paramiko
import os
import logging
import functools
from concurrent.futures import ThreadPoolExecutor

logger = logging.getLogger(__name__)


class LinuxShell:
    """
    执行linux shell命令
    """

    def __init__(self, hostname: str, port: int, username: str, password: str):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password

    def create_remote_connection(self) -> bool:
        try:
            # 实例化SSHClient
            self.client = paramiko.SSHClient()
            # 自动添加策略，保存服务器的主机名和密钥信息
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(hostname=self.hostname, port=self.port, username=self.username, password=self.password)
            return True
        except Exception as e:
            logger.error(e, exc_info=True)
            return False

    def remote_exec(self, cmd):
        stdin, stdout, stderr = self.client.exec_command(cmd)
        return '\n'.join(stdout.readlines())

    @staticmethod
    def local_exec(cmd):
        try:
            result = os.popen(cmd)
            return '\n'.join(result.readlines())
        except Exception as e:
            logger.error(e, exc_info=True)
            return False


def perform(func, data, func_args=None, asynch=False, workers=None, progress=False, desc='Loading...'):
    """
    Wrapper arround executable and the data list object.
    Will execute the callable on each object of the list.
    Parameters:

    - `func`: callable stateless function. func is going to be called like `func(item, **func_args)` on all items in data.
    - `data`: if stays None, will perform the action on all rows, else it will perfom the action on the data list.
    - `func_args`: dict that will be passed by default to func in all calls.
    - `asynch`: execute the task asynchronously
    - `workers`: mandatory if asynch is true.
    - `progress`: to show progress bar with ETA (if tqdm installed).
    - `desc`: Message to print if progress=True
    Returns a list of returned results
    """
    if not callable(func):
        raise ValueError('func must be callable')
    # Setting the arguments on the function
    func = functools.partial(func, **(func_args if func_args is not None else {}))
    # The data returned by function
    returned = list()
    elements = data
    try:
        import tqdm
    except ImportError:
        progress = False
    tqdm_args = dict()
    # The message will appear on loading bar if progress is True
    if progress is True:
        tqdm_args = dict(desc=desc, total=len(elements))
    # Runs the callable on list on executor or by iterating
    if asynch:
        if isinstance(workers, int):
            if progress:
                returned = list(tqdm.tqdm(ThreadPoolExecutor(max_workers=workers).map(func, elements), **tqdm_args))
            else:
                returned = list(ThreadPoolExecutor(max_workers=workers).map(func, elements))
        else:
            raise AttributeError('When asynch == True : You must specify a integer value for workers')
    else:
        if progress:
            elements = tqdm.tqdm(elements, **tqdm_args)
        for index_or_item in elements:
            returned.append(func(index_or_item))
    return returned
