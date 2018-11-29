from flask import flask

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return 'INDEX'

if __name__ == '__main__':
    app.run()
