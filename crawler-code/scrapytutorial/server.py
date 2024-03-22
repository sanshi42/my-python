"""使用Flask定义一个轻量级的服务器"""
from flask import Flask, jsonify, request
from loguru import logger

app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def receive():
    post_data = request.get_json()
    event = post_data.get('event')
    data = post_data.get('data')
    logger.info(f'received event {event}, data {data}')
    return jsonify(status='success')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)