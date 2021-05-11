from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello Worlddd!'


@app.route('/about')
def about():
    return 'About project!'


@app.route('/history')
def history():
    return 'History grouppp'


if __name__ == '__main__':
    app.run(debug=True)