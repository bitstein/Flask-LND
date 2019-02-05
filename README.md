# Flask-LND

Flask-LND initializes an LND gRPC interface using Will Clark's [lnd-grpc](https://github.com/willcl-ark/lnd_grpc) package.

## Installation

```
$ pip install flask-lnd
```

## Usage

```
import flask
from flask_lnd import LNDNode

app = flask.Flask(__name__)

lnd = LNDNode()
lnd.init_app(app)


@app.route('/')
def index():
    return str(lnd.rpc.get_info())
```
