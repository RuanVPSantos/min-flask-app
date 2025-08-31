from flask import Flask
import os

port = os.getenv('PORT', 4999)

app = Flask(__name__)

@app.route('/health')
def health():
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
