from flask import Flask, request
from . import operations as ops

calc_app = Flask(__name__)


@calc_app.route('/add')
def add_route():
    """Add a and b parameters."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(ops.add(a, b))


@calc_app.route('/sub')
def sub_route():
    """Subtract a and b parameters."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(ops.sub(a, b))


@calc_app.route('/mult')
def mult_route():
    """Multiply a and b parameters."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(ops.mult(a, b))


@calc_app.route('/div')
def div_route():
    """Divide a and b parameters."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(ops.div(a, b))


@calc_app.route('/math/<operation>')
def math_route(operation):
    """Perform math operation on a and b parameters."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    match operation:
        case 'add':
            return str(ops.add(a, b))
        case 'sub':
            return str(ops.sub(a, b))
        case 'mult':
            return str(ops.mult(a, b))
        case 'div':
            return str(ops.div(a, b))
        case _:
            return 'Invalid operation'
