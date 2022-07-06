# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask (__name__)


@app.route('/math/<operation>')
def get_math(operation):
    t1 = int(request.args.get("a"))
    t2 = int(request.args.get("b"))
    if (operation == 'add'):
        res = add(t1, t2)
        return str(res)
    elif (operation == 'sub'):
        return str(sub(t1,t2))
    elif (operation == 'mult'):
        return str(mult(t1,t2))
    elif (operation == 'div'):
        return str(div(t1,t2))
    else:
        return "Invalid Operation"