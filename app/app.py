import hashlib
import random
import string
from flask import Flask, jsonify, request, Response, Blueprint


app = Flask(__name__)


def generate_random_string(length=32):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choices(characters, k=length))
    return random_string


@app.route('/', methods=['GET'])
def get_subgets():
    num = request.args.get("num", 1)
    hash_ = ""
    for i in range(int(num)):
        hash_ += hashlib.sha256(f"{generate_random_string()}-{i}".encode()).hexdigest()
    return jsonify({'res': hash_}), 200


if __name__ == '__main__':
    app.run(debug=True)
