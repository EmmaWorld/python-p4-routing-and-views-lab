#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return'<h1>Python Operations with Flask Routing and Views</h1>' 

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    result=""
    for i in range(parameter):
        result+= str(i) + "\n"
    return result

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    dict_map = {
        '+': num1 + num2,
        '-': num1 - num2,
        'div': num1 / num2,
        '*': num1 * num2,
        '%': num1 % num2,
    }
    if operation in dict_map:
        result = dict_map[operation]
        return str(result)
    else:
        return "Invalid operation"


if __name__ == '__main__':
    app.run(port=5555, debug=True)
    
    
# math/1/*/2
