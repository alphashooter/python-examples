from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return 'hello, world!'


@app.route('/hello/<name>')
def hello(name):
    return 'hello, %s!' % name


@app.route('/template/<string:name>')
def template(name):
    return render_template('jinja2-template.html', name=name)


if __name__ == "__main__":
    app.run(debug=True, port=8888)
