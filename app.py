from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('MyResume/index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=5000)
