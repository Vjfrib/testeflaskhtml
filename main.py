

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-message')
def get_message():
    return 'gott mit uns'

if __name__ == '__main__':
    app.run()

