from flask import current_app

from lnd_grpc import lnd_grpc
from lnd_grpc.utilities import get_lnd_dir


class LNDNode(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('LND_DIR', get_lnd_dir())
        app.config.setdefault('LND_NETWORK', 'mainnet')
        # Do not use localhost as it is significantly slower on Windows
        app.config.setdefault('LND_GRPC_HOST', '127.0.0.1')
        app.config.setdefault('LND_GRPC_PORT', '10009')
        self.rpc = lnd_grpc.Client(
            lnd_dir=app.config['LND_DIR'],
            network=app.config['LND_NETWORK'],
            grpc_host=app.config['LND_GRPC_HOST'],
            grpc_port=app.config['LND_GRPC_PORT'],
        )
