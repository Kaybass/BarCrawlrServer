import os

from BarCrawlrServer import bcserver


if __name__ == '__main__':
    with bcserver.server.app_context():
        bcserver.server.run(debug=True)