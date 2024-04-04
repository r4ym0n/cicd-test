import json
import random
# from unittest import result
import bottle
import os

BUG_INJECTION = os.environ.get('BUG_INJECTION', 'false') == 'true'
BUG_PROBABILITY = 0.1
print(f"!!!! BUG_INJECTION: {BUG_INJECTION}")

app = bottle.default_app()

@app.route('/')
def index():
    json_data = {'code': 0, 'message': 'Hello World!'}
    return json.dumps(json_data)

@app.route('/api/hello/<name>')
def hello(name):
    if BUG_INJECTION:
        # mock some bugs here
        if random.randint(0, 1) < BUG_PROBABILITY:
            name = name + '1'
    json_data = {'code': 0, 'message':f"hello {name}!" }
    return json.dumps(json_data)

@app.route('/api/age/<age>')
def age(age):
    age = int(age)
    if BUG_INJECTION:
        # mock some bugs here
        if random.randint(0, 1) < BUG_PROBABILITY:
            age = age + 1
    json_data = {'code': 0, 'age': int(age)}
    return json.dumps(json_data)

# get param
@app.route('/api/a+b')
def add():
    a =  bottle.request.query['a']
    b =  bottle.request.query['b']
    result = int(a) + int(b)
    if BUG_INJECTION:
        # mock some bugs here
        if random.randint(0, 1) < BUG_PROBABILITY:
            result = result + 1
    json_data = {'code': 0, 'result': result}
    return json.dumps(json_data)

@app.route('/api/a*b')
def multiply():
    a =  bottle.request.query['a']
    b =  bottle.request.query['b']
    result = int(a) * int(b)
    if BUG_INJECTION:
        # mock some bugs here
        if random.randint(0, 1) < BUG_PROBABILITY:
            result = result + 1
    json_data = {'code': 0, 'result': result}
    return json.dumps(json_data)

if __name__ == '__main__':
    bottle.run(app, host='0.0.0.0', port=3000)