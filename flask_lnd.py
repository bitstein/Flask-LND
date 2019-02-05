from flask import current_app

from lnd_grpc import lnd_grpc


class LNDNode(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('LND_DIR', '.lnd')
        app.config.setdefault('LND_NETWORK', 'mainnet')
        app.config.setdefault('LND_GRPC_HOST', 'localhost')
        app.config.setdefault('LND_GRPC_PORT', '10009')
        self.rpc = lnd_grpc.Client(
            lnd_dir=app.config['LND_DIR'],
            network=app.config['LND_NETWORK'],
            grpc_host=app.config['LND_GRPC_HOST'],
            grpc_port=app.config['LND_GRPC_PORT'],
        )
