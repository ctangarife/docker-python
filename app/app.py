#coding: utf-8

from flask import Flask, json
app = Flask(__name__)

@app.route("/")
def summary():
    data = make_summary()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
        # return {'a': 1, 'b': 2}
    )
    return response

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
