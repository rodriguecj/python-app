from flask import Flask, jsonify
import socket
import datetime

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return jsonify({
        'message' : 'Hello World - details',
        'hostname': socket.gethostname(),
        'time'    : datetime.datetime.now()
    })

@app.route('/api/v1/healthz')
def health():
    return jsonify({
        'message' : 'Hello World - healthz',
        'status'  : 'up', 
        'hostname': socket.gethostname(),
        'time'    : datetime.datetime.now()
    }), 200

# main driver function
if __name__ == '__main__':
    app.run(host="0.0.0.0")