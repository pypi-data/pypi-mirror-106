"""
py3status-reddit: a py3status module showing reddit unread messages.

@author: Alessandro -oggei- Ogier <alessandro.ogier@gmail.com>
"""


import multiprocessing
import urllib
from uuid import uuid4

import praw
from praw.util.token_manager import FileTokenManager
from xdg import xdg_config_home

from py3status_reddit import CLIENT_ID, PORT
from py3status_reddit.webserver import webserver


class TokenManager(FileTokenManager):
    """
    Simple token manager which extend praw's one
    with sensible permissions and paths, plus a couple
    convenience methods.
    """

    def __init__(self):
        config_home = xdg_config_home() / "py3status-reddit"
        config_home.mkdir(parents=True, exist_ok=True)
        config_home.chmod(0o0700)
        filename = config_home / "refresh_token"
        filename.touch(0o0600, exist_ok=True)
        filename.chmod(0o0600)
        super().__init__(filename)

    @property
    def present(self):
        """
        Check for token existence ie. non-empty file.
        """
        with open(self._filename) as token_file:
            return bool(token_file.read().strip())

    def write(self, token):
        """
        Write current token to file.

        :param token: the token to write
        """
        with open(self._filename, "w") as token_file:
            token_file.write(token)


class Py3status:
    """
    Main module implementation
    """

    # parameters
    format = "reddit: {count}"
    cache_timeout = 60

    # internal
    _token = None
    _reddit = None
    _count = None

    def post_config_hook(self):
        """
        This is the class constructor which will be executed once.
        """

        self._token = TokenManager()

        self._reddit = praw.Reddit(
            client_id=CLIENT_ID,
            user_agent="py3status-reddit",
            client_secret=None,
            redirect_uri=f"http://localhost:{PORT}",
            token_manager=self._token,
        )

    def reddit(self):
        """
        module loop
        """

        if not self._token.present:
            message = "click here to authenticate with reddit OAuth"
            self._count = -1
        else:
            message = self.format
            self._count = len(list(self._reddit.inbox.unread()))

        return {
            "full_text": self.py3.safe_format(  # pylint: disable=no-member
                message, {"count": self._count}
            ),
            "cached_until": self.py3.time_in(  # pylint: disable=no-member
                self.cache_timeout
            ),
            "urgent": False,
        }

    def on_click(self, _event):
        """
        click handler

        :param _event: py3status' event
        """

        if not self._token.present:
            queue = multiprocessing.Queue()

            server = multiprocessing.Process(
                target=webserver, args=(queue,), daemon=True
            )

            server.start()
            state = uuid4()

            url = self._reddit.auth.url(["privatemessages"], state, "permanent")
            self.py3.command_run(f"xdg-open {url}")  # pylint: disable=no-member

            out = queue.get()
            # self.py3.log("queue got: %s" % out)
            server.kill()
            server.join()

            query = urllib.parse.parse_qs(urllib.parse.urlparse(out).query)
            # self.py3.log("aieie %s" % query)

            if query["state"] == [str(state)]:
                refresh_token = self._reddit.auth.authorize(query["code"][0])
                self._token.write(refresh_token)

        elif self._count > 0:
            self.py3.command_run(  # pylint: disable=no-member
                "xdg-open https://www.reddit.com/message/unread"
            )


# Run module in test mode.
if __name__ == "__main__":
    from py3status.module_test import module_test

    module_test(Py3status)
