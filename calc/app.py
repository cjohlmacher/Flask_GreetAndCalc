from flask import Flask, request
from operations import *

app = Flask(__name__)

operation_functions = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}

@app.route('/add')
def eval_add():
    a,b = request.args.get("a",None), request.args.get("b",None)
    if not a or not b:
        return "Requries two values: a and b"
    return f"{add(int(a),int(b))}"

@app.route('/sub')
def eval_subtract():
    a,b = request.args.get("a",None), request.args.get("b",None)
    if not a or not b:
        return "Requries two values: a and b"
    return f"{sub(int(a),int(b))}"

@app.route('/mult')
def eval_multiply():
    a,b = request.args.get("a",None), request.args.get("b",None)
    if not a or not b:
        return "Requries two values: a and b"
    return f"{mult(int(a),int(b))}"

@app.route('/div')
def eval_divide():
    a,b = request.args.get("a",None), request.args.get("b",None)
    if not a or not b:
        return "Requries two values: a and b"
    return f"{div(int(a),int(b))}"

@app.route('/math/<operation>')
def calculate(operation):
    """Calculates based off a given operation and returns result as string"""
    a,b = request.args.get("a",None), request.args.get("b",None)
    if not a or not b:
        return "Requries two values: a and b"
    operation_function = operation_functions.get(operation,None)
    return f"{operation_functions[operation](int(a),int(b))}" if operation_function else "Invalid operation"