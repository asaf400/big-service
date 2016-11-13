from flask import Flask

import counter

# initialize flask application class with static folder override
app = Flask(__name__)

# route '/'  to invoke count() when method is GET
@app.route('/', methods=["GET"])
def count():
    # return count attribute of a new counter.counter instance
    return str(counter.counter().count)


if __name__ == '__main__':
    app.run()
