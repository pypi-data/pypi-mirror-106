"""
A basic webserver, used to close Reddit OAuth flow.

@author: Alessandro -oggei- Ogier <alessandro.ogier@gmail.com>
"""
import http.server
import socketserver

from py3status_reddit import PORT

HTML = """
<html><body>
<h1>py3status-reddit: you can now close this window</h1>
</body></html>
"""


class OAuthCallbackHandler(http.server.BaseHTTPRequestHandler):
    """
    The oauth callback handler
    """

    queue = None

    def do_GET(self):  # pylint: disable=invalid-name
        """
        send a minimal response, then the path back to queue
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", len(HTML))
        self.end_headers()

        self.wfile.write(HTML.encode("utf-8"))
        self.queue.put(self.path)


def webserver(queue):
    """
    main loop

    :param queue: a multiprocessing.Queue used for communication
    """

    OAuthCallbackHandler.queue = queue

    with socketserver.TCPServer(("", PORT), OAuthCallbackHandler) as httpd:
        httpd.serve_forever()
