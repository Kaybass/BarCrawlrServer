from flask import Flask, jsonify, current_app

from BarCrawlrServer import bcserver


if __name__ == '__main__':
    with bcserver.server.app_context():
        bcserver.server.run(debug=True)