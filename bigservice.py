from flask import Flask

import counter

app = Flask(__name__)


@app.route('/', methods=["GET"])
def count():
    return str(counter.counter().count)


if __name__ == '__main__':
    app.run()
